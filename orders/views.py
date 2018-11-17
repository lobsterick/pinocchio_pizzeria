from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import *
from django.http import HttpResponseNotFound
from decimal import *
from django.contrib import messages
from .add_menu import add_menu


def delete_all_user_orders(username):
    Sub.objects.filter(add_by=username).filter(already_ordered=False).delete()
    Pasta.objects.filter(add_by=username).filter(already_ordered=False).delete()
    Salad.objects.filter(add_by=username).filter(already_ordered=False).delete()
    Platter.objects.filter(add_by=username).filter(already_ordered=False).delete()
    Pizza.objects.filter(add_by=username).filter(already_ordered=False).delete()
    return True


def calculate_cart_price(username):
    price_all = 0
    for obj in Sub.objects.filter(add_by=username).filter(already_ordered=False):
        price_all += obj.price
    for obj in Pasta.objects.filter(add_by=username).filter(already_ordered=False):
        price_all += obj.price
    for obj in Salad.objects.filter(add_by=username).filter(already_ordered=False):
        price_all += obj.price
    for obj in Platter.objects.filter(add_by=username).filter(already_ordered=False):
        price_all += obj.price
    for obj in Pizza.objects.filter(add_by=username).filter(already_ordered=False):
        price_all += obj.price
    return price_all


def welcome_page(request):
    return render(request, 'orders/welcome.html')


def register_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("index")
        else:
            form = RegistrationForm()
        context = {"form": form}
        return render(request, 'registration/register.html', context)
    else:
        return redirect("index")


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if next is not None:
                        return redirect("index")
                    else:
                        return redirect("index")
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'registration/login.html', context)
    else:
        return redirect("index")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")


@login_required
def cart_view(request):
    price_all = Decimal(calculate_cart_price(request.user))
    context = {}
    context.update({"price_all": price_all})
    context.update({"Sub": Sub.objects.filter(add_by=request.user).filter(already_ordered=False)})
    context.update({"Pasta": Pasta.objects.filter(add_by=request.user).filter(already_ordered=False)})
    context.update({"Salad": Salad.objects.filter(add_by=request.user).filter(already_ordered=False)})
    context.update({"Platter": Platter.objects.filter(add_by=request.user).filter(already_ordered=False)})
    context.update({"Pizza": Pizza.objects.filter(add_by=request.user).filter(already_ordered=False)})

    return render(request, 'orders/cart.html', context)


@login_required()
def menu_view(request):
    form_pizza = PizzaAddForm(request.POST or None)
    if form_pizza.is_valid():
        form_pizza_size = form_pizza.cleaned_data["pizza_size"]
        form_pizza_type = PizzaType.objects.get(name=request.POST["pizzatype"])
        form_pizza_toppings = form_pizza.cleaned_data["toppings"]
        form_pizza_add_by = request.user
        new_pizza = Pizza(add_by=form_pizza_add_by, pizza_size=form_pizza_size, pizzatype=form_pizza_type)
        new_pizza.save()
        new_pizza.toppings.set(form_pizza_toppings)
        new_pizza.calculate_price()
        new_pizza.save()
        messages.add_message(request, messages.INFO, "Pizza added!")
        form_pizza = PizzaAddForm()

    context = {}
    context.update({"Sub": SubType.objects.all()})
    context.update({"Pasta": PastaType.objects.all()})
    context.update({"Salad": SaladType.objects.all()})
    context.update({"Platter": PlatterType.objects.all()})
    context.update({"Pizza": PizzaType.objects.all()})
    context.update({"PizzaToppings": PizzaTopping.objects.all()})
    context.update({"form_pizza": form_pizza})
    return render(request, 'orders/menu.html', context)


@login_required()
def add_to_cart(request, item_type, item_id, item_bigger, add_cheese):

    if item_type == "sub":
        item_id = SubType.objects.get(id=item_id)
        new_sub = Sub(subtype=item_id, additional_cheese=add_cheese, subsize=item_bigger, add_by=request.user)
        new_sub.calculate_price()
        new_sub.save()
        messages.add_message(request, messages.INFO, "Sub added!")

    elif item_type == "platter":
        item_id = PlatterType.objects.get(id=item_id)
        new_platter = Platter(plattertype=item_id, plattersize=item_bigger, add_by=request.user)
        new_platter.calculate_price()
        new_platter.save()
        messages.add_message(request, messages.INFO, "Platter added!")

    elif item_type == "pasta":
        item_id = PastaType.objects.get(id=item_id)
        new_pasta = Pasta(pastatype=item_id, add_by=request.user)
        new_pasta.calculate_price()
        new_pasta.save()
        messages.add_message(request, messages.INFO, "Pasta added!")

    elif item_type == "salad":
        item_id = SaladType.objects.get(id=item_id)
        new_salad = Salad(saladtype=item_id, add_by=request.user)
        new_salad.calculate_price()
        new_salad.save()
        messages.add_message(request, messages.INFO, "Salad added!")

    else:
        return HttpResponseNotFound('<h1>Product not found</h1>')

    return redirect(menu_view)


@login_required()
def make_order(request):
    new_proper_order = ProperOrder()
    new_proper_order.order_client = request.user
    new_proper_order.order_price = calculate_cart_price(request.user)
    new_proper_order.save()

    for item in Sub.objects.filter(add_by=request.user).filter(already_ordered=False):
        item.already_ordered = True
        item.in_order = new_proper_order
        item.save()

    for item in Pasta.objects.filter(add_by=request.user).filter(already_ordered=False):
        item.already_ordered = True
        item.in_order = new_proper_order
        item.save()

    for item in Salad.objects.filter(add_by=request.user).filter(already_ordered=False):
        item.already_ordered = True
        item.in_order = new_proper_order
        item.save()

    for item in Platter.objects.filter(add_by=request.user).filter(already_ordered=False):
        item.already_ordered = True
        item.in_order = new_proper_order
        item.save()

    for item in Pizza.objects.filter(add_by=request.user).filter(already_ordered=False):
        item.already_ordered = True
        item.in_order = new_proper_order
        item.save()

    messages.add_message(request, messages.INFO, f"Order number {new_proper_order.id} send! If you have questions, contact us: 617-876-4897")
    return redirect(user_orders_view)


@staff_member_required
def all_orders_view(request):
    context = {"orders": reversed(ProperOrder.objects.all())}
    return render(request, 'orders/all_orders.html', context)


@login_required
def user_orders_view(request):
    context = {"orders": reversed(ProperOrder.objects.filter(order_client=request.user))}
    return render(request, 'orders/my_orders.html', context)


@staff_member_required
def mark_order_as_done(request, order_id):
    marked = ProperOrder.objects.get(id=order_id)
    marked.order_done = True
    marked.save()
    return redirect(all_orders_view)


@login_required
def clear_cart(request):
    delete_all_user_orders(request.user)
    return redirect("cart_view")


@staff_member_required()
def fill_menu(request):
    add_menu()
    return redirect(welcome_page)

from django.urls import path

from .views import welcome_page, register_view, login_view, logout_view, cart_view, menu_view, add_to_cart, make_order, all_orders_view, mark_order_as_done, user_orders_view, clear_cart, fill_menu

urlpatterns = [
    path("", welcome_page , name="index"),
    path("register", register_view, name="register_view"),
    path("login", login_view, name="login_view"),
    path("logout", logout_view, name="logout_view"),
    path("cart", cart_view, name="cart_view"),
    path("menu", menu_view, name="menu_view"),
    path("add/<str:item_type>/<int:item_id>/<str:item_bigger>/<int:add_cheese>", add_to_cart, name="add_to_cart"),
    path("finalize", make_order, name="make_order" ),
    path("all_orders", all_orders_view, name="all_orders_view"),
    path("order/<int:order_id>/done", mark_order_as_done, name="mark_order_as_done"),
    path("my_orders", user_orders_view, name="user_orders_view"),
    path("clear_cart", clear_cart, name="clear_cart"),
    path("fill_menu", fill_menu, name="fill_menu")
]

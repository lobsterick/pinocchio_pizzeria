from orders.models import *
from decimal import Decimal


def add_menu():
    '''Function filling database with standard menu.

    Function importing standard Pinocchio's menu from http://www.pinocchiospizza.net/menu.html to connected database. Run only once, when database is empty.
    If there are records in database from Pinocchio's menu, it will delete it and and again.'''

    # Get by [item for item in PizzaTopping.objects.values("name")]
    toppings = [{'name': 'Pepperoni'}, {'name': 'Sausage'}, {'name': 'Mushrooms'}, {'name': 'Onions'}, {'name': 'Ham'}, {'name': 'Canadian Bacon'}, {'name': 'Pineapple'}, {'name': 'Eggplant'}, {'name': 'Tomato and Basil'}, {'name': 'Green Peppers'}, {'name': 'Hamburger'}, {'name': 'Spinach'}, {'name': 'Artichoke'}, {'name': 'Buffalo Chicken'}, {'name': 'Barbecue Chicken'}, {'name': 'Anchovies'}, {'name': 'Black Olives'}, {'name': 'Fresh Garlic'}, {'name': 'Zucchini'}]

    # Get by PizzaType.objects.values("name", "price_sm_0","price_sm_1", "price_sm_2", "price_sm_3", "price_sm_4","price_lg_0","price_lg_1", "price_lg_2","price_lg_3", "price_lg_4")
    pizza_types = [{'name': 'Regular', 'price_sm_0': Decimal('12.20'), 'price_sm_1': Decimal('13.20'), 'price_sm_2': Decimal('14.70'), 'price_sm_3': Decimal('15.70'), 'price_sm_4': Decimal('17.25'), 'price_lg_0': Decimal('17.45'), 'price_lg_1': Decimal('19.45'), 'price_lg_2': Decimal('21.45'), 'price_lg_3': Decimal('23.45'), 'price_lg_4': Decimal('25.45')}, {'name': 'Sicilian', 'price_sm_0': Decimal('23.45'), 'price_sm_1': Decimal('25.45'), 'price_sm_2': Decimal('27.45'), 'price_sm_3': Decimal('28.45'), 'price_sm_4': Decimal('29.45'), 'price_lg_0': Decimal('37.70'), 'price_lg_1': Decimal('39.70'), 'price_lg_2': Decimal('41.70'), 'price_lg_3': Decimal('43.70'), 'price_lg_4': Decimal('44.70')}]

    # Get by [item for item in SubType.objects.values("name", "small_price", "large_price")]
    sub_types = [{'name': 'Cheese', 'small_price': Decimal('6.50'), 'large_price': Decimal('7.95')}, {'name': 'Italian', 'small_price': Decimal('6.50'), 'large_price': Decimal('7.95')}, {'name': 'Ham + Cheese', 'small_price': Decimal('6.50'), 'large_price': Decimal('7.95')}, {'name': 'Meatball', 'small_price': Decimal('6.50'), 'large_price': Decimal('7.95')}, {'name': 'Tuna', 'small_price': Decimal('6.50'), 'large_price': Decimal('7.95')}, {'name': 'Turkey', 'small_price': Decimal('7.50'), 'large_price': Decimal('8.50')}, {'name': 'Chicken Parmigiana', 'small_price': Decimal('7.50'), 'large_price': Decimal('8.50')}, {'name': 'Eggplant Parmigiana', 'small_price': Decimal('6.50'), 'large_price': Decimal('7.95')}, {'name': 'Steak', 'small_price': Decimal('6.50'), 'large_price': Decimal('7.95')}, {'name': 'Steak + Cheese', 'small_price': Decimal('6.95'), 'large_price': Decimal('8.50')}, {'name': 'Sausage, Peppers and Onions', 'small_price': None, 'large_price': Decimal('8.50')}, {'name': 'Hamburger', 'small_price': Decimal('4.60'), 'large_price': Decimal('6.95')}, {'name': 'Cheeseburger', 'small_price': Decimal('5.10'), 'large_price': Decimal('7.45')}, {'name': 'Fried Chicken', 'small_price': Decimal('6.95'), 'large_price': Decimal('8.50')}, {'name': 'Steak + Cheese + Mushrooms', 'small_price': Decimal('7.45'), 'large_price': Decimal('9.00')}, {'name': 'Steak + Cheese + Green Peppers', 'small_price': Decimal('7.45'), 'large_price': Decimal('9.00')}, {'name': 'Steak + Cheese + Onions', 'small_price': Decimal('7.45'), 'large_price': Decimal('9.00')}, {'name': 'Steak + Cheese + Mushrooms + Green Peppers', 'small_price': Decimal('7.95'), 'large_price': Decimal('9.50')}, {'name': 'Steak + Cheese + Mushrooms + Onions', 'small_price': Decimal('7.95'), 'large_price': Decimal('9.50')}, {'name': 'Steak + Cheese + Green Peppers + Onions', 'small_price': Decimal('7.95'), 'large_price': Decimal('9.50')}, {'name': 'Steak + Cheese + Mushrooms + Green Peppers + Onions', 'small_price': Decimal('8.45'), 'large_price': Decimal('10.00')}]

    #Get by [item for item in PastaType.objects.values("name", "price")]
    pasta_types = [{'name': 'Baked Ziti w/Chicken', 'price': Decimal('9.75')}, {'name': 'Baked Ziti w/Meatballs', 'price': Decimal('8.75')}, {'name': 'Baked Ziti w/Mozzarella', 'price': Decimal('6.50')}]

    #Get by [item for item in SaladType.objects.values("name", "price")]
    salad_types = [{'name': 'Garden Salad', 'price': Decimal('6.25')}, {'name': 'Greek Salad', 'price': Decimal('8.25')}, {'name': 'Antipasto', 'price': Decimal('8.25')}, {'name': 'Salad w/Tuna', 'price': Decimal('8.25')}]

    # Get by [item for item in PlatterType.objects.values("name", "small_price", "large_price")]
    platter_types = [{'name': 'Garden Salad', 'small_price': Decimal('35.00'), 'large_price': Decimal('60.00')}, {'name': 'Greek Salad', 'small_price': Decimal('45.00'), 'large_price': Decimal('70.00')}, {'name': 'Antipasto', 'small_price': Decimal('45.00'), 'large_price': Decimal('70.00')}, {'name': 'Baked Ziti', 'small_price': Decimal('35.00'), 'large_price': Decimal('60.00')}, {'name': 'Meatball Parm', 'small_price': Decimal('45.00'), 'large_price': Decimal('70.00')}, {'name': 'Chicken Parm', 'small_price': Decimal('45.00'), 'large_price': Decimal('80.00')}]

    # Import All PizzaToppings
    PizzaTopping.objects.all().delete()
    for topping in toppings:
        new_topping = PizzaTopping(name=topping["name"])
        new_topping.save()
        print(f"Added {topping} to PizzaTopping")

    # Import all PizzaTypes
    PizzaType.objects.all().delete()
    for pizza in pizza_types:
        new_pizza = PizzaType(name=pizza["name"], price_sm_0=pizza["price_sm_0"],price_sm_1=pizza["price_sm_1"], price_sm_2=pizza["price_sm_2"], price_sm_3=pizza["price_sm_3"], price_sm_4=pizza["price_sm_4"], price_lg_0=pizza["price_lg_0"],price_lg_1=pizza["price_lg_1"], price_lg_2=pizza["price_lg_2"],price_lg_3=pizza["price_lg_3"], price_lg_4=pizza["price_lg_4"])
        new_pizza.save()
        print(f"Added {pizza} to PizzaTypes")

    # Import all SubTypes
    SubType.objects.all().delete()
    for sub in sub_types:
        new_sub = SubType(name=sub["name"], small_price=sub["small_price"], large_price=sub["large_price"])
        new_sub.save()
        print(f"Added {sub} to SubTypes")

    # Import all PastaTypes
    PastaType.objects.all().delete()
    for pasta in pasta_types:
        new_pasta = PastaType(name=pasta["name"], price=pasta["price"])
        new_pasta.save()
        print(f"Added {pasta} to PastaTypes")

    # Import all SaladTypes
    SaladType.objects.all().delete()
    for salad in salad_types:
        new_salad = SaladType(name=salad["name"], price=salad["price"])
        new_salad.save()
        print(f"Added {salad} to SaladTypes")

    # Import all PlatterTypes
    PlatterType.objects.all().delete()
    for platter in platter_types:
        new_platter = PlatterType(name=platter["name"], small_price=platter["small_price"], large_price=platter["large_price"])
        new_platter.save()
        print(f"Added {platter} to PlatterTypes")

    return True

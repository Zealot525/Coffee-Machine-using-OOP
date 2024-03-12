from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


to_continue = True
while to_continue:
    user_input = input(f"What would you like? {menu.get_items()}:")
    if user_input == "off":
        to_continue = False
    elif  user_input == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif user_input =="espresso" or user_input == "latte" or user_input == "cappuccino":
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"The cost of {user_input} is ${drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("An error occured, please try again.")   

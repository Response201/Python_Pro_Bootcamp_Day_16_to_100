from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

machine_on=True
machine = CoffeeMaker()
payment = MoneyMachine()
menu= Menu()


while machine_on:
    get_drinks= menu.get_items()
    choice = input(f"What would you like? ({get_drinks}):")


    if choice == "off":
        # turn off machine -> stop while-loop
        print("Goodbye! The coffee machine is now resting.")
        machine_on = False


    elif choice == "report":
        # Show current resources
        print("Current resource values:")
        machine.report()
        payment.report()


    else:

        drink = menu.find_drink(choice)

        # Check if enough resources to make the drink
        if machine.is_resource_sufficient(drink):

            # Make drink if enough money
            if payment.make_payment(drink.cost):

                machine.make_coffee(drink)

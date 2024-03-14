from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off_machine = False
coffee_menu = Menu()
coffee_maker = CoffeeMaker()
coffee_money_machine = MoneyMachine()

selected_drink = 'no drink selected'

while not turn_off_machine:
    user_input = input('Please select a drink:\snl = latte\ne = espresso\nc = cappuccino\nEnter your selection: ')

    if user_input.lower() == 'off':
        turn_off_machine = True
        break

    if user_input.lower() == 'report':
        print(coffee_maker.report())
        print(coffee_money_machine.report())

    if user_input == 'l':
        selected_drink = 'latte'
    elif user_input == 'e':
        selected_drink = 'espresso'
    elif user_input == 'c':
        selected_drink = 'cappuccino'

    existing_drink = coffee_menu.find_drink(selected_drink)

    coffee_money_machine.money_received = float(input(f'Your drink cost {existing_drink.cost}\nPlease enter your money: '))

    if existing_drink:
        enough_resources = coffee_maker.is_resource_sufficient(existing_drink)
    
        if enough_resources:
            enough_money = coffee_money_machine.make_payment(existing_drink.cost)

            if enough_money:
                coffee_maker.make_coffee(existing_drink)
    
    
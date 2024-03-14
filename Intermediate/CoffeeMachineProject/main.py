# import all dependencies.
from art import logo
from data import coffee_machine_full_capacity
from data import MENU
import os
import math

# lambda to clear the console
clear = lambda:os.system('clear')

current_inventory = coffee_machine_full_capacity
coffee_selection = MENU

# we need to be able to print out the report of the current inventory that is in the machine.
def print_report():
    """Prints out the current inventory of the coffee machine."""
    print(current_inventory)


# we need a function that checks the existing resources within the coffee machine and prints out if it is possible or not to make the selected drink.
def check_inventory(drink):
    """This function takes in the drink that is passed in as the parameter, checks the ingredients that is required for creating the drink and then confirms if the coffee machine has enough ingredient to make the drink."""
    global current_inventory
    temporary_copy_of_inventory = current_inventory
    enough_ingredients = True
    for ingredient in coffee_selection[drink]['ingredients']:
        if current_inventory[ingredient] < coffee_selection[drink]['ingredients'][ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            enough_ingredients = False
            break
        else:
            temporary_copy_of_inventory[ingredient] -= coffee_selection[drink]['ingredients'][ingredient]
        
    if enough_ingredients == True:
        current_inventory = temporary_copy_of_inventory
    
    return enough_ingredients


def process_coin(money):
    """This function takes in money from the user and returns the amount of coins that is needed to be returned back to the user."""
    amount_of_coin_to_return = {
        'quarter' : 0,
        'dime' : 0,
        'nickle' : 0,
        'penny' : 0
    }
    
    while money > 0:
        if money > .25:
            amount_of_quarters = int(money/.25)
            amount_of_coin_to_return['quarter'] = amount_of_quarters
            money -= round(amount_of_quarters * .25, 2)
        elif money > .10:
            amount_of_dimes = int(money/.10)
            amount_of_coin_to_return['dime'] = amount_of_dimes
            money -= round(amount_of_dimes * .10, 2)
        elif money > .05:
            amount_of_nickles = int(money/.05)
            amount_of_coin_to_return['nickle'] = amount_of_nickles
            money -= round(amount_of_nickles * .05, 2)
        elif money > .01:
            amount_of_pennies = int(round(money/.01))
            amount_of_coin_to_return['penny'] = amount_of_pennies
            money = 0
    return amount_of_coin_to_return


def successful_transaction(input_money, cost_of_drink, drink):
    # if the input money is higher than the cost of the drink
    global current_inventory
    is_success = True

    if input_money >= cost_of_drink:
        if check_inventory(drink) == True:
            if input_money > cost_of_drink:
                coin_change = round(input_money - cost_of_drink, 2)
                current_inventory['money'] += input_money
                print(process_coin(coin_change))
            print(f'Here is your {drink}. Enjoy!')
        else:
            print('Sorry, there is not enough ingredient. Returning money.')
            is_success = False
    else:
        print('Sorry, that is not enough money')
        is_success = False
    
    return is_success
        






        



# we need to prompt the user to see what coffee does the user wants. This will require us to give the different options and take in the input.

#user_input = input('Please enter your coffee selection:\ne = espresso\nl = latte\nc = cappuccino')


# setting the stopping point for the coffee machine run time if the user enter off

coffee_machine_running = True

print('Welcome to the coffee machine.')

while coffee_machine_running:
    user_choice = input('Select a coffee to create:\ne = espresso\nl = latte\nc = cappuccino\n')

    if user_choice == 'off':
        coffee_machine_running = False
    elif user_choice == 'report':
        print_report()
    else:
        selected_drink = str
        if user_choice == 'e':
            selected_drink = 'espresso'
        elif user_choice == 'l':
            selected_drink = 'latte'
        elif user_choice == 'c':
            selected_drink = 'cappuccino'

        cost_of_coffee = coffee_selection[selected_drink]['cost']

        user_money = round(float(input(f'please enter {cost_of_coffee}\n')), 2)

        if successful_transaction(input_money = user_money, cost_of_drink = cost_of_coffee, drink = selected_drink):
            continue_operation = input('Would you like another cup of coffee?\ny = yes\nn = no\n')
            if continue_operation == 'n':
                coffee_machine_running = False

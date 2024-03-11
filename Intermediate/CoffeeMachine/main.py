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
    enough_ingredients = True
    for ingredient in coffee_selection[drink]['ingredients']:
        if current_inventory[ingredient] < coffee_selection[drink]['ingredients'][ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            enough_ingredients = False
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


# we need to prompt the user to see what coffee does the user wants. This will require us to give the different options and take in the input.

#user_input = input('Please enter your coffee selection:\ne = espresso\nl = latte\nc = cappuccino')


# setting the stopping point for the coffee machine run time if the user enter off
clear()
print('hello')
print(process_coin(1.32))
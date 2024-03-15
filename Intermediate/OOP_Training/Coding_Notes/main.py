# import turtle
# import another_module
# # print(another_module.another_variable)

# # this is how a new object is constructed
# from turtle import Turtle, Screen

# # creating a new object from blueprint
# timmy = Turtle()q

# print(timmy)
# timmy.shape('turtle') # calling methods within the object.
# timmy.color('chartreuse3')

# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight) # tapping into object attribute.
# my_screen.exitonclick()

# python3 -m pip install PrettyTable | to install package
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Pokemon', 'Type']
table.add_rows([
    ['Pikachu', 'Electric'],
    ['Chikorita', 'Grass'],
    ['Charmander', 'Fire'],
])

table.align = 'r'

print(table)
## Coffee machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
os.system('cls' if os.name == 'nt' else 'clear')
## Coffee Machine

# money = 0
machine_on = True
#

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
drink = Menu()

# print report about resources left
while machine_on:
    options = drink.get_items()
    flavour = input(f"What would you like? {options}: ").lower()
    if flavour=='off':
        os.system('cls' if os.name == 'nt' else 'clear')
        machine_on = False
    elif flavour == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    elif flavour in options:
        # check resources are sufficient
        choice = drink.find_drink(flavour)
        if my_coffee_maker.is_resource_sufficient(choice):
            if my_money_machine.make_payment(choice.cost):
                my_coffee_maker.make_coffee(choice)


            # my_money_machine.process_coins()
            # if cost(flavour):
            #     print(f"Here is your {flavour}\u2615 ENJOY!")
            # else:
            #     print("you have paid less amount, please take it back...")
        # else:
        #     pass
        #     # machine_on = False
    else:
        print("Please enter correct choice...")



# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electrical", "Water", "Fire"])
# table.align = "l"
# print(table)


# import turtle
# mano = turtle.Turtle()
# mano.shape("turtle")
# mano.color("blue")
# mano.turtlesize(stretch_wid=5, stretch_len=5, outline=0.5)
# print(mano)
# mano.forward(200)
# my_screen = turtle.Screen()
# my_screen.bgcolor("red")
#
# print(my_screen.canvwidth)
# my_screen.exitonclick()

# # This is a sample Python script.
#
# # Press Ctrl+F5 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

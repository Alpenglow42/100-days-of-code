            # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.fd(100)
# timmy.lt
# timmy.fd(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type" ,["Electric","Water","Fire"])

table.align = "l"

print(table)
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('chocolate1')
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Pokemon Name", "Type"]
x.add_row(['Pikachu', 'Electric'])
x.add_row(['Squirtle', 'Water'])
x.add_row(['Charmander', 'Fire'])
print(x)
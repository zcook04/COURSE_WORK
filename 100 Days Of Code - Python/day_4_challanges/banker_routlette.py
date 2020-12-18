# Problem taken from Angelas 100 Days Of Code - The complete Python Pro Bootcamp 2021

# Instructions
# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the command the next name.

# Example Output
# Michael is going to buy the meal today!

# My Solution -------------------------------------------------------------

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

people_qty = len(names)

choice = names[random.randint(0, (people_qty - 1))]

print(f'Names: {names}\nAmount of People: {people_qty}\nWho Pays: {choice}')

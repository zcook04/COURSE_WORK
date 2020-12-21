# Create a random password generator randomized version

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def generate_letters():
    selected_letters = ''
    for letter in range(0, nr_letters):
        selected_letters += letters[random.randint(0, len(letters)-1)]
    return selected_letters


def generate_symbols():
    selected_symbols = ''
    for symbol in range(0, nr_symbols):
        selected_symbols += symbols[random.randint(0, len(symbols)-1)]
    return selected_symbols


def generate_numbers():
    selected_numbers = ''
    for number in range(0, nr_numbers):
        selected_numbers += numbers[random.randint(0, len(numbers)-1)]
    return selected_numbers


def randomize_pw(s):
    randomized_pw = ''
    s_list = list(s)
    random.shuffle(s_list)
    return randomized_pw.join(s_list)


def generate_password():
    return randomize_pw(generate_letters() + generate_numbers() + generate_symbols())


print(generate_password())

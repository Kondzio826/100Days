import string
import random

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

password = []
password_string = ""

print("Welcome in password Generator:")
letters_number = int(input("How many letters in password?\n"))
numbers_number = int(input("How many numbers in password?\n"))
symbols_number = int(input("How many symbols in password?\n"))

for i in range(letters_number):
    password.append(letters[random.randint(0,len(letters)-1)])

for i in range(numbers_number):
    password.append(numbers[random.randint(0,len(numbers)-1)])

for i in range(symbols_number):
    password.append(symbols[random.randint(0,len(symbols)-1)])

random.shuffle(password)

for letter in password:
    password_string +=letter

print(f"Your password is: {password_string}")
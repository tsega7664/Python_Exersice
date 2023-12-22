import random

letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','1','2','3','4','5','6','7','8','9']
symbol = ['!','#','$','%','^','&','*','(',')','+']
print("Welcome to PyPasword Generator!")
nr_letters = int(input(f"How may letters would you like in your password?\n"))
nr_numbers = int(input(f"How may numbers would you like?\n"))
nr_symbols = int(input(f"How may symbols would you like?\n"))

password = ""
for n in range (0,nr_letters + 1):
    rand_let = random.choice(letter)
    password = password + rand_let

for l in range (0,nr_numbers + 1):
    rand_let = random.choice(number)
    password = password + rand_let

for n in range (0,nr_symbols + 1):
    rand_let = random.choice(symbol)
    password = password + rand_let
print(f"Your Password is {password}")
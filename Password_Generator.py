# Made with ♥ By Ranim

import random

Uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*()-_+=<>?/[]{}|:;'~,. "

upper, lower, num, sym = True, True, True, True

print("Answer the questions with yes(y) or no (n)")
is_upper = input("Do you want your password to contain Uppercase letters? ")
if is_upper.lower() == "yes":
    upper = True
else:
    lower = False
is_lower = input("Do you want your password to contain Lowercase letters? ")
if is_lower.lower() == "yes":
    lower = True
else:
    lower = False
is_num = input("Do you want your password to contain Numbers? ")
if is_num.lower() == "yes":
    num = True
else:
    num = False
is_sym = input("Do you want your password to Special Characters? ")
if is_sym.lower() == "yes":
    sym = True
else:
    sym = False

#upper, lower, num, sym = True, True, True, True

all = ""

if upper:
    all += Uppercase_letter
if lower:
    all += lowercase_letter
if num:
    all += digits
if sym:
    all += symbols



lenght = input("How many charachter do you wan your password to have: ")
amount = input("How many passwords do you want: ")

for x in range(int(amount)):
    password = "".join(random.sample(all, int(lenght)))
    print(password)
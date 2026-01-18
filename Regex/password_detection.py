"""Checks the password is strong or not."""
import re

upper_re = re.compile(r'[A-Z]')
lower_re = re.compile(r'[a-z]')
digit_re = re.compile(r'\d')

password = input("Enter the password: ")

if len(password) < 8:
    print("Password must 8 characters long.")
else:
    if upper_re.search(password) and lower_re.search(password) and digit_re.search(password):
        print("Your password is strong.")
    else:
        print("Your password is weak.")

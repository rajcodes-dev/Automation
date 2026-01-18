"""Checks the password is strong or not."""
#  user input the password
# then it checks and tell the password is weak or not.

import re

pass_re = re.compile(r"""(
                     ([a-z])+
                     ([A-Z])+
                     ([0-9])+
                     )""", re.VERBOSE)

password = input("Enter the password: ")
if len(password) != 8:
    print("Password must 8 characters long.")
else:
    strong_pass = pass_re.findall(password)
    if strong_pass == []:
        print("Your password is weak.")
    else:
        print("Your password is strong.")

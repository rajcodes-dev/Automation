"""Cleaning dates in the standard format."""
import re
import pyperclip
from humre import *

dates_re = re.compile(r"""(
                      (\d{2}|\d{4}) # First digits
                      (-|\.|/) # separator
                      (\d{2}|\d{4}) # Second date
                      (-|\.|/) # separator
                      (\d{2}|\d{4}) # third digit
                      )""", re.VERBOSE)

text = pyperclip.paste()

std_dates = []
for groups in dates_re.findall(text):
    if len(groups[1]) == 4:
        std_dates.append('-'.join([groups[1],groups[3], groups[5]]))
    if len(groups[1]) == 2:
        print(groups)
        std_dates.append("-".join([groups[5], groups[1], groups[3]]))

if len(std_dates) > 0:
    pyperclip.copy('\n'.join(std_dates))
    print("Copied to clipboard.")
    print('\n'.join(std_dates))
else:
    print("No dates were found.")

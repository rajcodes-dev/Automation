"""Checking phone number without using regular expression."""
"""
def is_phone_number(text):
    if len(text) != 12:
        return False

    for num in range(0,3):
        if not text[num].isdecimal():
            return False

    if text[3] != '-':
        return False

    for num in range(4,7):
        if not text[num].isdecimal():
            return False

    if text[7] != '-':
        return False

    for num in range(8,12):
        if not text[num].isdecimal():
            return False
    return True


message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for num in range(len(message)):
    segment = message[num:num+12]
    if is_phone_number(segment):
        print("Phone Number Found: " + segment)
print('Done')
"""

"""Checking phone number using regular expression."""


import pyperclip, re

text = input("Enter the text: ")

cleaned = re.sub(r'\b\d{3}-?\d{2}-?\d{4}\b', "[SSN_REMOVED]", text)
cleaned = re.sub(r'\b(?:\d[ -]*?){13,16}\b', "[CARD_REMOVED]", cleaned)

print("\nCleaned text: ")
print(cleaned)

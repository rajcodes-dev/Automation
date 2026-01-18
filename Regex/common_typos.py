import re

text = input("Enter the text: ")

text = re.sub(r"\s{2,}"," ",text)
text = re.sub(r"\b(\w+)\s+\1\b", r"\1", text)
text = re.sub(r"!{2,}", "!", text)

print(text)

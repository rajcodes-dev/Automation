import pyperclip, re

text = pyperclip.paste()

URLs_re = re.compile(r"""(
                     ((http://|https://)\S+)
                     )""", re.VERBOSE)

matches = []
for groups in URLs_re.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy(matches)
    print("Copied to clipboard.")
    print('\n'.join(matches))
else:
    print('No URLs found.')

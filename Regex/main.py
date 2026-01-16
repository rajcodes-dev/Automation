import re
# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# match = pattern.search('my phone number is 323-239-9833.')
# print(match.group())

vowel_pattern = re.compile(r"[^aeiouAEIOU]")
# vowel_pattern = re.compile(r"[aeiouAEIOU]")
print(vowel_pattern.findall('consistency matters'))

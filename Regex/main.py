import re
from humre import *
# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# match = pattern.search('my phone number is 323-239-9833.')
# print(match.group())

# vowel_pattern = re.compile(r"[^aeiouAEIOU]")
# # vowel_pattern = re.compile(r"[aeiouAEIOU]")
# print(vowel_pattern.findall('consistency matters'))


"""Phone number extractor using humre module"""

phone_regex = group(
    optional_group(either(exactly(3, DIGIT), # Area code
                          OPEN_PAREN + exactly(3, DIGIT) + CLOSE_PAREN)),
    optional(group_either(WHITESPACE,'-',PERIOD)), # Separator
    group(exactly(3, DIGIT)), # First three digits
    group_either(WHITESPACE, '-', PERIOD), # Separator
    group(exactly(4, DIGIT)), # Last four digits
    optional_group( # Extension
        zero_or_more(WHITESPACE),
        group_either('ext', 'x', r'ext\.'),
        zero_or_more(WHITESPACE),
        group(between(2, 5, DIGIT))
        )
    )

pattern = re.compile(phone_regex)
match = pattern.search('my phone is 234-239-2398.')
print(match.group())

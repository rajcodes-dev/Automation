"""Regex version of strip() function."""
import re

def regex_strip(text, chars = None):
    if chars is None:
        return re.sub(r'^\s+|\s+$','',text)
    else:
        pattern = '^[' + chars + ']+' + '|[' + chars + ']+$'
        return re.sub(pattern, '', text)

print(regex_strip('*****sdfjk****', '*'))

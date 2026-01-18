"""Regex version of strip() function."""
import re

def regex_strip(text):
    return re.sub(r'^\s+|\s+$','',text)

print(regex_strip('  sdf  jk    '))

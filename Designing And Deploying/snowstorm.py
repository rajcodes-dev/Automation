import os, random, time, sys

TOP = chr(9600)
BOTTOM = chr(9604)
FULL = chr(9608)

DENSITY = 4 # Default snow density set to 4
if len(sys.argv) > 1:
    DENSITY = int(sys.argv[1])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear() # To clear the terminal window.

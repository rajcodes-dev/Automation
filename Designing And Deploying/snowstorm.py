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

# Main loop over each row and column.
    for y in range(20):
        for x in range(40):
            if random.randint(0, 99) < DENSITY:
                print(random.choice([TOP, BOTTOM]), end='')
            else:
                print(' ', end='')
        print()
    

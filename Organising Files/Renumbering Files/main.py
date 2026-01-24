"""Program which renumber the files name."""
import os
from pathlib import Path

os.chdir("D:\PROGRAMMES\Code Arena\Automation\Organising Files\Renumbering Files")
for i in range(1, 121):
    if i not in (42, 86, 103):
        with open(f'spam{str(i).zfill(3)}.txt', 'w') as file:
            pass

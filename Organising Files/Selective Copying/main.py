from pathlib import Path
import os, re
import shutil

p = Path(r"D:/PROGRAMMES/Code Arena/Automation/Organising Files/Selective Copying")
h = Path(r"D:/PROGRAMMES/Code Arena/Automation/Organising Files/new_folder")
for filename in p.glob("*.pdf"):
    shutil.copy(filename, h)

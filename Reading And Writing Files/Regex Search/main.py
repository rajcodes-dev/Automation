from pathlib import Path
import os, re

text = re.compile(r"hi everyone.")

p = Path(r"D:\PROGRAMMES\Code Arena\Automation\Reading And Writing Files\Regex Search")
os.chdir(p)
pattern = re.compile(r"(\.txt)$")
dirs = os.listdir(p)
print(dirs)

for dir in dirs:
    if pattern.search(dir) is not None:
        with open(dir, 'r', encoding='utf-8') as file:
            content = file.readlines()
            if text.search(content) is not None:
                print(dir)

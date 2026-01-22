from pathlib import Path
import re

text = re.compile(r"hi everyone\.")

p = Path(r"D:\PROGRAMMES\Code Arena\Automation\Reading And Writing Files\Regex Search")

if p.exists():
    for file_path in p.glob('*.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if text.search(line):
                    print(f"Match Found: {file_path.name}")
                    print(f"line content: {line.strip()}")
else:
    print("The specified path does not exist!")

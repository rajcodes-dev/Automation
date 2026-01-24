"""Program which renumber the files name."""
import re, os
from pathlib import Path

p = Path("D:\PROGRAMMES\Code Arena\Automation\Organising Files\Renumbering Files")
# os.chdir(p)
# for i in range(1, 121):
#     if i not in (42, 86, 103):
#         with open(f'spam{str(i).zfill(3)}.txt', 'w') as file:
#             pass

pattern = re.compile(r'^(.*?)(\d+)\.txt$')

files = sorted(list(p.glob('spam*.txt')))

for idx, file_path in enumerate(files):
    match = pattern.search(file_path.name)
    if not match:
        continue

    prefix = match.group(1)
    old_num_str = match.group(2)
    correct_num = idx + 1

    new_num_str = str(correct_num).zfill(len(old_num_str))
    new_name = f"{prefix}{new_num_str}.txt"
    new_path = p / new_name

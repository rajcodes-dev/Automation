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

    if file_path.name != new_name:
        print(f"Renameing {file_path.name} to {new_name}")
        file_path.rename(new_path)

print("Program runs successfully!")

def insert_gap(folder_path, prefix, start_at):
    p = Path(folder_path)
    pattern = re.compile(f"^{prefix}(\\d+)\\.txt$")

    files = sorted(list(p.glob(f"{prefix}*.txt")),reverse = True)

    for file_path in files:
        num = int(pattern.search(file_path.name).group(1))

        if num >= start_at:
            new_num = str(num + 1).zfill(3)
            new_name = f"{prefix}{new_num}.txt"
            file_path.rename(p / new_name)
            print(f"Bumped {file_path.name} to {new_name}")

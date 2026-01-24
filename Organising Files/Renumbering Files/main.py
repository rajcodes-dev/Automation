"""Program which renumber the files name."""
import re, os
from pathlib import Path

p = Path("D:\PROGRAMMES\Code Arena\Automation\Organising Files\Renumbering Files")
# os.chdir(p)
# for i in range(1, 121):
#     if i not in (42, 86, 103):
#         with open(f'spam{str(i).zfill(3)}.txt', 'w') as file:
#             pass
# pattern = re.compile(r'(\w+)(\d{3})\.txt')
# for idx, file_name in enumerate(p.glob("spam*.txt")):
#     file_name = file_name.parts[-1]
#     f_name = file_name
#     num = pattern.search(file_name)
#     file_name = num.group(1)
#     num = num.group(2)
#     if int(num) != idx+1:
#         os.rename(p / f_name, f"{file_name}{idx+1}.txt")
#     print("Program runs successfully")

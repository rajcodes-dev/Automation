import shutil, os
from pathlib import Path
p = Path("d:/PROGRAMMES/Code Arena/Automation/Organising Files")

for folder_name, subfolders, filenames in os.walk(p/'spam'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER of ' + folder_name + ':' + subfolder)

    for filename in filenames:
        print('FILE INSIDE' + folder_name + ':' + filename)
        c = Path(folder_name)
        shutil.move(c/filename, c/filename.upper())

    print('')

"""main.py - A search term finder which search in all excel files."""
import os
from pathlib import Path

current_path = Path(r"D:\PROGRAMMES\Code Arena\Automation\Projects\Search Term Finder")
def find_in_excel(search_text):
    for folder, subfolders, file_names in os.walk(current_path):
        print(file_names)

find_in_excel("name")

from pathlib import Path
import re

target_dir = Path(r"d:\PROGRAMMES\Code Arena\Automation\Reading And Writing Files\Mad Libs")
mad_path = target_dir / "mad_lib.txt"
file_path = target_dir / "final.txt"

if mad_path.exists():
    content = mad_path.read_text(encoding='utf-8')
else:
    print("File was not found.")
    exit()

keywords = ['ADJECTIVE','NOUN','VERB','ADVERB']

new_text = content

for word in re.findall(r'ADJECTIVE|NOUN|VERB|ADVERB', content):
    user_text = input(f"Enter a {word.lower()}: \n")
    new_text = new_text.replace(word, user_text, 1)

print("\nFinal Story:")
print(new_text)

file_path.write_text(new_text, encoding='utf-8')
print(f"\nSaved to {file_path}")

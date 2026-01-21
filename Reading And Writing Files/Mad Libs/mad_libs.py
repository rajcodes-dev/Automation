from pathlib import Path

target_dir = Path("d:\PROGRAMMES\Code Arena\Automation\Reading And Writing Files\Mad Libs")
file_path = target_dir / "final.txt"
mad_path = target_dir / "mad_lib.txt"

target_dir.mkdir(parents=True, exist_ok=True)

mad_file = open(mad_path, "r", encoding='utf-8')
final_file = open(file_path, "w", encoding="utf-8")

mad_text = mad_file.read()
mad_text = mad_text.split()
adjective = input("Enter an adjective:\n").strip().title()
noun = input("\nEnter a noun:\n").strip().title()
verb = input("\nEnter a verb:\n").strip().title()
noun2 = input("\nEnter the noun:\n").strip().title()

for idx, text in enumerate(mad_text):
    if text == "ADJECTIVE":
        mad_text[idx] = adjective
    elif text == "NOUN":
        mad_text[idx] = noun
    elif text == "VERB":
        mad_text[idx] = verb
    elif text == "NOUN2":
        mad_text[idx] = noun2

final_file.write(' '.join(mad_text))
mad_file.close()
final_file.close()

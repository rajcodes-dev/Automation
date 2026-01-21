from pathlib import Path

target_dir = Path("d:\PROGRAMMES\Code Arena\Automation\Reading And Writing Files\Mad Libs")
file_path = target_dir / "final.txt"
mad_path = target_dir / "mad_lib.txt"

target_dir.mkdir(parents=True, exist_ok=True)

mad_file = open(mad_path, "r", encoding='utf-8')
final_file = open(file_path, "w", encoding="utf-8")

mad_text = mad_file.read()
mad_text = list(mad_text)
adjective = input("Enter an adjective:\n")
noun = input("\nEnter a noun:\n")
verb = input("\nEnter a verb:\n")
noun2 = input("\nEnter the noun:\n")



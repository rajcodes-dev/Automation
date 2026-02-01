import openpyxl
import os
import sys

if len(sys.argv) != 4:
    print("Usage: python blankRowInserter.py <N> <M> <filename>")
    sys.exit()
try:
    start_row = int(sys.argv[1])
    num_rows = int(sys.argv[2])
    filename = sys.argv[3]
except ValueError:
    print("N and M must be integers.")
    sys.exit()

if not os.path.exists(filename):
    print(f"Error: File {filename} not found!")
    sys.exit()

print(f"Opening {filename}...")
wb = openpyxl.load_workbook(filename)
sheet = wb.active

new_wb = openpyxl.Workbook()
new_sheet = new_wb.active

print(f"Inserting {num_rows} blank row at row {start_row}...")

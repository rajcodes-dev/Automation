"""
multiplication_table.py - program which display multiplication table
on excel from command line arguments.
"""
import sys, openpyxl
from openpyxl.styles import Font

TABLE = 0
BOLD_FONT = Font(name='Times New Roman', bold=True)
if int(sys.argv[1]) >= 1:
    TABLE = int(sys.argv[1])
else:
    print("Argument must be integer")
    sys.exit()

wb = openpyxl.Workbook()
sheet = wb['Sheet']
sheet.title = 'Multiplication Table'

for row_num in range(2, TABLE + 2):
    sheet.cell(row=row_num, column=1).value = row_num - 1
    sheet.cell(row=row_num, column=1).font = BOLD_FONT

for col_num in range(2, TABLE + 2):
    sheet.cell(row=1, column=col_num).value = col_num - 1
    sheet.cell(row=1, column=col_num).font = BOLD_FONT

for row_num in range(2, TABLE + 2):
    for col_num in range(2, TABLE + 2):
        sheet.cell(row=row_num, column=col_num).value = (row_num - 1) * (col_num - 1)

wb.save(F'Excel Spreadsheets/Projects/Table{TABLE}.xlsx')

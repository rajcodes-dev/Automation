"""
multiplication_table.py - program which display multiplication table
on excel from command line arguments.
"""
import sys, openpyxl

TABLE = 0
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
for col_num in range(2, TABLE + 2):
    sheet.cell(row=1, column=col_num).value = col_num - 1

wb.save(F'Excel Spreadsheets/Projects/Table{TABLE}.xlsx')

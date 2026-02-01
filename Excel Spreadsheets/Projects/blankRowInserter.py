import sys, openpyxl

if len(sys.argv) != 4:
    print("enter min. 4 arguments")
    sys.exit()
N = int(sys.argv[1])
M = int(sys.argv[2])
file_name = sys.argv[3]
print(file_name)
wb = openpyxl.load_workbook(file_name)
sheet = wb.active
sheet.insert_rows(idx=N, amount=M)
wb.save(f"ChangeTable.xlsx")

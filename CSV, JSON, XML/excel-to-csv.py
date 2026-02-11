# excel-to-csv.py --> Convert excel file to csv file
import openpyxl
import csv
import os

for excel_file in os.listdir('.'):
    if not excel_file.endswith('.xlsx'):
        continue

    print(f"  Converting {excel_file} ....")

    try:
        wb = openpyxl.load_workbook(excel_file, data_only=True)
    except Exception as e:
        print(f"Could not load {excel_file}: {e}")
        continue

    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]

        excel_title = excel_file[:-5]
        csv_filename = f"{excel_title}_{sheet_name}.csv"

        

import ezsheets

ss = ezsheets.Spreadsheet("1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg")
sheet = ss.sheets[0]

print("Scanning rows for error....")

for rowNum in range(2, sheet.rowCount + 1):
    row_data = sheet.getRow(rowNum)

    if row_data[0] == '':
        break

    beans_per_jar = int(row_data[0])
    jars = int(row_data[1])
    total_beans = int(row_data[2])

    if beans_per_jar * jars != total_beans:
        print(f"Mistake found at row {rowNum}!")
        print(f"Calculation: {beans_per_jar} * {jars} should be {total_beans}")
        break

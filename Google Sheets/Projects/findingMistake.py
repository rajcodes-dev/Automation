import ezsheets

ss = ezsheets.Spreadsheet("1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg")
mistake_row = []
for rowNum in range(2, ss.sheets[0].rowCount + 1):
    if int(ss.sheets[0].getRow(2)[0]) * int(ss.sheets[0].getRow(2)[1]) != int(ss.sheets[0].getRow(2)[2]) :
        mistake_row.append(rowNum)

print(mistake_row)

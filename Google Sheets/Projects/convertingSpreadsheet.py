import ezsheets
ss = ezsheets.upload('my_excel.xlsx')

ss.downloadAsExcel()
ss.downloadAsCSV()
ss.downloadAsTSV()
print("Files are download in different format.")

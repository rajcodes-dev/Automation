import ezsheets

ss = ezsheets.Spreadsheet("1Bi-5W9Q8NDZVsgoxRjSM8iyiHm_R3obyu4wp6NW1K3w")
sheet = ss.sheets[0]

sheet.columnCount = 6
sheet.rowCount = 5

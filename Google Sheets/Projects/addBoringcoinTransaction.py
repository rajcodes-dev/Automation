import ezsheets, sys

if len(sys.argv) > 4:
    print("Usage: python addBoringcoinTransaction.py sender recipient amount")
    sys.exit()

sender, recipient, amount = sys.argv[1:]

ss = ezsheets.Spreadsheet("1-b2V7rztAhvIvH6Rzf_rX6CUaFwf3viwlf_YCrOFnOk")
sheet = ss.sheets[0]

sheet.rowCount += 1
sheet[1, sheet.rowCount] = sender
sheet[2, sheet.rowCount] = recipient
sheet[3, sheet.rowCount] = amount

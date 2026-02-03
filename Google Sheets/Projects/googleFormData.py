import ezsheets

ss = ezsheets.Spreadsheet("1Bi-5W9Q8NDZVsgoxRjSM8iyiHm_R3obyu4wp6NW1K3w")
sheet = ss.sheets[0]

email_lst = []
for num in range(2, sheet.rowCount + 1):
    email = sheet[f'C{num}']
    if email not in email_lst:
        email_lst.append(email)
print("These are email who attempted quiz.\n", email_lst)

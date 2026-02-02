"""auditBoringcoin.py - Audit the fake blockchain"""
import ezsheets
ss = ezsheets.Spreadsheet("1-b2V7rztAhvIvH6Rzf_rX6CUaFwf3viwlf_YCrOFnOk")
accounts = {}

# Each row is a transactions, loop over each row.
for row in ss.sheets[0].getRows():
    sender, recipient, amount = row[0], row[1], int(row[2])
    if sender == 'PRE-MINE':
        accounts.setdefault(recipient, 0)
        accounts[recipient] += amount
    else:
        accounts.setdefault(sender, 0)
        accounts.setdefault(recipient, 0)
        accounts[sender] -= amount
        accounts[recipient] += amount

print(accounts)

TOTAL = 0
for amount in accounts.values():
    TOTAL += amount
print("Total Boringcoins:", TOTAL)

import ezsheets
ss = ezsheets.Spreadsheet('https://autbor.com/boringcoin')
accounts = {}

# Each row is a transactions, loop over each row.
for row in ss.sheets[0].getRows():
    sender, recipient, amount = row[0], row[1], row[2]
    if sender == 'PRE-MINE':
        accounts.setdefault(recipient, 0)
        accounts['recipient'] += amount
    else:
        accounts.setdefault(sender, 0)
        accounts.setdefault(recipient, 0)
        accounts[sender] -= amount
        accounts[recipient] += amount

print(accounts)

total = 0
for amount in accounts.values():
    total += amount
print("Total Boringcoins:", total)

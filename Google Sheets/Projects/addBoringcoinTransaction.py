import ezsheets, sys

if len(sys.argv) > 4:
    print("Usage: python addBoringcoinTransaction.py sender recipient amount")
    sys.exit()

sender, recipient, amount = sys.argv[1:]

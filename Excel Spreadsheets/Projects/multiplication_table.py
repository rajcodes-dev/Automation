"""
multiplication_table.py - program which display multiplication table
on excel from command line arguments.
"""
import sys, openpyxl

TABLE = 0
if int(sys.argv[1]) >= 1:
    TABLE = int(sys.argv[1])

print(TABLE)

"""cat_vaccination_checker.py - analysis the db and check the vaccinations."""

import sqlite3

conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

print("--- Cat Missing Vaccines ---")

query_missing = """
SELECT name FROM cats
WHERE rowid NOT IN (SELECT cat_id FROM vaccinations WHERE vaccine = 'rabies')
    OR rowid NOT IN (SELECT cat_id FROM vaccinations WHERE vaccine = 'FeLV')
    OR rowid NOT IN (SELECT cat_id FROM vaccinations WHERE vaccine = 'FVRCP')
"""

for row in conn.execute(query_missing):
    print(f"- {row[0]}")

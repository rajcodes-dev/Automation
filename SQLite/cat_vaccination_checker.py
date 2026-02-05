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

print("\n--- DATABASE ERROR --- ")

query_error = """
SELECT cats.name, vaccinations.vaccine, vaccinations.date_administered, cats.birthdate
FROM cats
JOIN vaccinations ON cats.rowid = vaccinations.cat_id
WHERE vaccinations.date_administered < cats.birthdate;
"""

for row in conn.execute(query_error):
    print(f"ERROR: {row[0]} got {row[1]} on {row[2]} but was born {row[3]}")

conn.close()

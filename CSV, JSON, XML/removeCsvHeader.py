# Removes the header line from csv file

import os, csv

os.makedirs('headerRemoved', exist_ok=True)

for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue
    print('Removing header from ' + csv_filename + '...')


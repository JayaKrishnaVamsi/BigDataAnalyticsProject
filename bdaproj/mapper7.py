#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)
header = True

for row in reader:
    if header:
        header = False
        continue
    try:
        if row[0].strip() != "":  # Check Income not null
            city = row[4].strip()
            income = float(row[0])
            disposable = float(row[18])  # Column index for Disposable_Income
            if city.startswith("Tier"):
                print "%s\t%s\t%s" % (city, disposable, 1)
    except:
        continue


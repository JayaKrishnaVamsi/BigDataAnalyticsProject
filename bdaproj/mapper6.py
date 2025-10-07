#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)
header = True

for row in reader:
    if header:
        header = False
        continue
    if len(row) > 4:
        city_tier = row[4].strip()
        if city_tier.startswith("Tier"):
            print "%s\t1" % city_tier


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, csv

reader = csv.reader(sys.stdin)
header = next(reader, None)  # skip header

for row in reader:
    try:
        tier = row[4]
        er = float(row[30])  # Expense_Ratio
        sys.stdout.write("%s\t%f\t1\n" % (tier, er))
    except:
        continue


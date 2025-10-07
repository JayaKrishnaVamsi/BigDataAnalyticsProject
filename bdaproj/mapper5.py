#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys, csv
reader = csv.reader(sys.stdin)
for i, row in enumerate(reader):
    if i == 0:  # header
        continue
    try:
        occ = row[3]                 # Occupation
        er  = float(row[31])         # Expense_Ratio
    except:
        continue
    if occ == '' or er != er:
        continue
    print('%s\t%s\t%s' % (occ, 1, er))


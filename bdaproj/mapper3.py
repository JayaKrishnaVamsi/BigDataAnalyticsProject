#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, csv
cats = ["Groceries","Transport","Eating_Out","Entertainment","Utilities","Healthcare","Education","Miscellaneous"]
reader = csv.reader(sys.stdin)
next(reader, None)
for row in reader:
    try:
        tier = row[4]
        for i,cat in enumerate(cats):
            spend = float(row[11+i])
            sys.stdout.write("%s|%s\t%f\n" % (tier, cat, spend))
    except:
        continue


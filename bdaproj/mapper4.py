#!/usr/bin/env python2
import sys, csv
r = csv.reader(sys.stdin)
for i,row in enumerate(r):
    if i==0: continue
    try:
        tier = row[4]; occ = row[3]
    except:
        continue
    if tier and occ:
        print('%s|%s\t1' % (tier, occ))


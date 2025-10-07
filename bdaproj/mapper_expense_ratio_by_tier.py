#!/usr/bin/env python3
import sys,csv
def f(x):
    try: return float(x)
    except: return None
for line in sys.stdin:
    row = next(csv.reader([line.strip()]))
    if not row: continue
    inc = f(row[0]) if len(row)>0 else None
    if inc is None: continue
    city = row[4].strip() if len(row)>5 else ""
    er = f(row[31]) if len(row)>31 else None
    if er is None: continue
    print(f"{city}\t{er}\t1")


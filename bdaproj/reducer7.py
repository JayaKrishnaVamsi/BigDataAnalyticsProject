#!/usr/bin/env python
import sys

current_key = None
sum_disposable = 0.0
count = 0

for line in sys.stdin:
    try:
        line = line.strip()
        key, value, one = line.split("\t")
        value = float(value)
        one = int(one)

        if key == current_key:
            sum_disposable += value
            count += one
        else:
            if current_key:
                avg = round(sum_disposable / count, 2)
                print "%s\t%.2f" % (current_key, avg)
            current_key = key
            sum_disposable = value
            count = one
    except:
        continue

if current_key:
    avg = round(sum_disposable / count, 2)
    print "%s\t%.2f" % (current_key, avg)


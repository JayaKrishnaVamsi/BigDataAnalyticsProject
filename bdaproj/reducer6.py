#!/usr/bin/env python
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    try:
        line = line.strip()
        key, value = line.split("\t")
        value = int(value)

        if current_key == key:
            current_count += value
        else:
            if current_key:
                print "%s\t%d" % (current_key, current_count)
            current_key = key
            current_count = value
    except:
        continue

if current_key == key:
    print "%s\t%d" % (current_key, current_count)


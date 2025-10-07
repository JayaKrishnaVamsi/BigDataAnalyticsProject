#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

cur_key = None
sum_v = 0.0
cnt = 0

for line in sys.stdin:
    parts = line.rstrip("\n").split("\t")
    if len(parts) != 3: 
        continue
    key, v, one = parts
    try:
        v = float(v); one = int(one)
    except:
        continue

    if cur_key == key:
        sum_v += v; cnt += one
    else:
        if cur_key is not None and cnt > 0:
            sys.stdout.write("%s\t%.4f\n" % (cur_key, sum_v / cnt))
        cur_key = key
        sum_v = v; cnt = one

if cur_key is not None and cnt > 0:
    sys.stdout.write("%s\t%.4f\n" % (cur_key, sum_v / cnt))


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
cur = None; n = 0; s = 0.0
for line in sys.stdin:
    k, cnt, val = line.rstrip('\n').split('\t')
    cnt = int(cnt); val = float(val)
    if k != cur and cur is not None:
        avg = s / n if n else 0.0
        print('%s\t%d\t%.4f' % (cur, n, avg))
        n = 0; s = 0.0
    cur = k; n += cnt; s += val
if cur is not None:
    avg = s / n if n else 0.0
    print('%s\t%d\t%.4f' % (cur, n, avg))


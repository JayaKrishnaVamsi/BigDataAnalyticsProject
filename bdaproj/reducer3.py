#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
cur = None; max_cat=None; max_val=-1
for line in sys.stdin:
    k,v = line.strip().split("\t")
    try: v = float(v)
    except: continue
    if cur is None:
        cur = k.split("|")[0]
    tier,cat = k.split("|")
    if tier != cur:
        if max_cat is not None:
            sys.stdout.write("%s\t%s\t%.2f\n" % (cur,max_cat,max_val))
        cur = tier; max_cat = cat; max_val = v
    else:
        if v > max_val:
            max_cat = cat; max_val = v
if max_cat is not None:
    sys.stdout.write("%s\t%s\t%.2f\n" % (cur,max_cat,max_val))


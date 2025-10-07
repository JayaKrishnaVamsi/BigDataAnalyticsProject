#!/usr/bin/env python3
import sys
cur=None; s=0.0; c=0
def flush():
    if cur is not None and c>0:
        print(f"{cur}\t{(s/c):.4f}")
for line in sys.stdin:
    parts=line.strip().split("\t")
    if len(parts)<3: continue
    k,val,cnt = parts[0], parts[1], parts[2]
    try:
        val=float(val); cnt=int(cnt)
    except: continue
    global cur,s,c
    if k!=cur:
        flush(); cur=k; s=0.0; c=0
    s+=val; c+=cnt
flush()


#!/usr/bin/env python2
import sys
cur=None; n=0
for line in sys.stdin:
    k,c = line.rstrip('\n').split('\t'); c=int(c)
    if k!=cur and cur is not None:
        print('%s\t%d' % (cur, n)); n=0
    cur=k; n+=c
if cur is not None:
    print('%s\t%d' % (cur, n))


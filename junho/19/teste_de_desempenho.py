#!/usr/bin/env python

from time import time


l = list()
t = time()
for e in xrange(1000):
	l.insert(0, e)
	#l.append(e)

#l.reverse()
t = time() - t

print t

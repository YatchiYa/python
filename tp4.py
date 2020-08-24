#!/usr/bin/env python

# Import modules
import math

a = int(7)
i = int(1)

print "les multiple de 7 avec etoile (*) sur les multiple de 3"
print
print

while (i < 20):
    a = 7 * i
    print a,
    quotien = a % 3
    if (quotien == 0):
        print "*",
    i = i + 1
#!/usr/bin/python

for a in range(1,1001):
    # Only try b > a, b < 1001-a
    for b in range(a,1001-a):
        # Find only possible matching C
        c = 1000 - (a+b)
        # Is this the correct answer?
        if a**2 + b**2 == c**2:
            print "%s ^ 2 + %s ^ 2 = %s ^ 2, and %s + %s + %s = 1000" % (a,b,c,a,b,c)
            print "%s * %s * %s = %s" % (a,b,c,a*b*c)


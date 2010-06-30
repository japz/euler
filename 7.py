#!/usr/bin/python

from utils import *

primes = [2]
i=1
while len(primes) <= 10001:
    i+=2
    factors = find_factors(i, primes)
    if len(factors) == 0:
        # Add this newly found prime to our list
        print "%s is a prime #%s" % (i, len(primes))
        primes.append(i)

print primes
print primes[10000]

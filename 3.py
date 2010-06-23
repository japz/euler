#!/usr/bin/python

#target = 16
target = 600851475143

nexttarget = target
i = 2
primes = []

def find_factors(number, primes):
    factors = []
    for i in primes:
        if number % i == 0:
            factors.append(i)
    return factors


while i <= nexttarget:
    factors = find_factors(i, primes)
    if len(factors) == 0:
        # Add this newly found prime to our list
        #print "%s is a prime" %i
        primes.append(i)

        # See if our target number divides by our prime, and re-set our target
        while nexttarget % i == 0:
            oldtarget = nexttarget
            nexttarget = nexttarget / i
            print "Target %s is divisable by %s, new target is %s" % (oldtarget, i, nexttarget)

    
    #print "%s factors to %s" % (i, factors)
    i += 1

print find_factors(target, primes)
print primes

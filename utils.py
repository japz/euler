#!/usr/bin/python

def find_factors(number, primes):
    # Returns prime factors of number, given a list of primes
    factors = []
    for i in primes:
        if number % i == 0:
            factors.append(i)
    return factors


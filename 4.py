#!/usr/bin/python

def is_palindrome(number):
    forward = str(number)
    reverse = forward[::-1]
    return forward == reverse

#palindromes = {}
palindromes = []
    
for i in range(100,1000):
    for j in range(i,1000):
        if is_palindrome(i*j):
            #palindromes["%s * %s" % (i,j)] = i*j
            palindromes.append(i*j)

print sorted(palindromes)

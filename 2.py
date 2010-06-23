#!/usr/bin/python

sequence = [1,2]
sums = [2]
lastsum = 2
lastnumber = 2

while lastnumber <= 4000000:
    nextnumber = sequence[len(sequence)-1] + sequence[len(sequence)-2]
    sequence.append(nextnumber)
    if sequence[len(sequence)-1] % 2 == 0 and sequence[len(sequence)-1] < 4000000:
        sums.append(lastsum + nextnumber)
        print "Adding %s" % nextnumber
    lastsum = sums[len(sums)-1]
    lastnumber = sequence[len(sequence)-1]

print sequence
print sums


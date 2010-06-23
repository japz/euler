#!/usr/bin/pyhton

sum_of_squares = 0
sum = 0
target = 100

for i in range(1,target+1):
    sum_of_squares += i**2
    sum += i

square_of_sum = sum**2
print "sum_of_squares: %s" % sum_of_squares
print "square_of_sum: %s" % square_of_sum

print abs(square_of_sum - sum_of_squares)

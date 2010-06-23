#!/usr/bin/python

def check_answer(number,test_range):
    for i in test_range:
        if number % i != 0:
            return False
    return True

answer = 0
i=1

range_max = 2
target_range_max = 20
last_range_answer = 1

target_range = range(1, target_range_max + 1)
current_range = range(1, range_max + 1)

while range_max <= target_range_max:
    if check_answer(i, current_range):
        print "%s was the answer for range %s" % (i, range_max)
        range_max += 1
        current_range = range(1,range_max+1)
        last_range_answer = i
    else:
        i += last_range_answer

print last_range_answer

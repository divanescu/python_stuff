#!/usr/bin/env python
count = 0
sum = 0
print "before", count, sum
for value in [5,12,34,53,29, 1.5]:
    count = count +1
    sum = sum + value
    print count, sum, value
print "after", count, float(sum), sum/count

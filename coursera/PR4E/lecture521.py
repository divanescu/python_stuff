#!/usr/bin/env python
largest_so_far = -1
print "before", largest_so_far
for num in [9, 41, 15, 74, 24, 82]:
    if num > largest_so_far:
        largest_so_far = num
    print largest_so_far, num
print "after", largest_so_far

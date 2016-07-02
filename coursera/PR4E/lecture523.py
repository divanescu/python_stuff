#!/usr/bin/env python
smallest_so_far = None
print "before", smallest_so_far
for num in [9, 41, 15, 74, 24, 82]:
    if smallest_so_far is None:
        smallest_so_far = num
    elif num < smallest_so_far:
        smallest_so_far = num
    print smallest_so_far, num
print "after", smallest_so_far

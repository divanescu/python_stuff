word = raw_input("Enter string: ")
low = word.lower()
d = dict()
for c in low:
    if c in low:
        d[c] = d.get(c, 0) + 1
print "String: ", word 
print d

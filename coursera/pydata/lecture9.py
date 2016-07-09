counts = dict()
print "Enter a line:"
line = raw_input("")

words = line.split()
print "Words:", words

print "Counting..."
for word in words:
    counts[word] = counts.get(word, 0) + 1
for key,value in counts.items():
    print key,value

print "Counts: ", counts 

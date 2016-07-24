from itertools import islice
fname = raw_input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print "File cannot be opened:", fname
    exit()
nr_of_lines = int(raw_input("Enter number of lines to read (0 for full file): "))
with fhand as myfile:
    head = list(islice(myfile, nr_of_lines))

if nr_of_lines == 0:
    text = open(fname)
else:
    text = head

counts = dict()

for line in text:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print counts

#sorting the keys by saving them in a list first
lst = counts.keys()
print "sorted list of keys=================="
lst.sort()
print lst
print "keys and values, sorted:"
for key in lst:
    print key, counts[key]

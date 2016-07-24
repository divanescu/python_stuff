#Exercise 2   Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with From, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
from itertools import islice
fname = raw_input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print "Cannot open file:", fname
    exit()
nr_of_lines = int(raw_input("Enter number of lines to read (0 for full file): "))

with fh as myfile:
    head = list(islice(myfile, nr_of_lines))

    if nr_of_lines == 0:
        text = open(fname)
    else:
        text = head


counts = dict()

for line in text:
    words = line.split()
    #print words
    
    if len(words) > 0:
        if words[0] == "From":
            #print words, words[1]
            counts[words[1]] = counts.get(words[1], 0) + 1
        #print words[0]
        
    else:
        #print "out of index"
        continue

#print counts
maximum = None
max_email = None
for mail, amount in counts.items():
    #print mail, amount
    if maximum is None or maximum < amount:
        maximum = amount
        max_email = mail
print max_email, maximum


#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

#fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    #print "line", line.strip()
    words = line.split()
    print words
    #print "line",  line
    #if len(words) > 0 and words[0] != "From" : continue
    #print words[1]
    
    for word in words:
        #print "for word in words", word
        #print words
        if len(words)!= 0 and words[0] != "From" : continue
        print word[0] 
        count = count +1
            
print count


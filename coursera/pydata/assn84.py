#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
#fname = raw_input("Enter file name: ")
fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    print line.rstrip()
    words = line.split()
    print words
    length = len(lst)
    print length
    for word in words:
        for i in length :
            print i
        
        print word
         
        #lst.append(word)



print lst
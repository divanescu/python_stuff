#Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesnt matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
fname = "words.txt"
fh = open(fname, 'r')
text = fh.read()
words = text.split()
dct = dict()
total_len = len(words) 
#check if the word is already in the dictionary, if it's not, add it with the value 1, if it is, increment the value
for word in words:
    print word
    dct[word] = dct.get(word, 0) + 1

print total_len
print len(dct)
print words
print dct

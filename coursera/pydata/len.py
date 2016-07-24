fname = "text.txt"
fh = open(fname)
text = fh.read()
text.strip()
words = text.split()
dct = dict()
print words, len(words)
for word in words:
    print word
    if word in dct:
        dct[word] = dct.get(word, 0) + 1
    else:
        dct[word] = 1
print dct, len(dct)

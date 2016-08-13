import re
fh = open('mbox-short.txt')
counts = dict()
for line in fh:
    line = line.strip()
    if re.search('^F.*m:', line):
        print line

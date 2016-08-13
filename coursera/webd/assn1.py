import re
fn = 'regex_sum_286898.txt'
fh = open(fn, 'r')
numbers = list()
total = 0
total_line = 0
for line in fh:
    nums_on_line = re.findall('[0-9]+', line)
    if len(nums_on_line) == 0: continue
        

    numbers.append(nums_on_line)
    
for item in numbers:
    for string in item:
        total = total + int(string)
print total

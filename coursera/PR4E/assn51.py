#Write a program which repeatedly reads numbers until the user enters 'done'. Once 'done' is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
count = 0
total = 0.0
average = 0.0

while True:
        line = raw_input("Enter a number: ")
        if line == 'done':
            print int(total), count, average
            break
        else:
            try:
                test = float(line)
                count = count + 1
                total = total + float(line)
                average = float(total / count)
            except:
                print "Invalid input!"


 


#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
count = 0
small = None
large = None
while True:
        input = raw_input("Enter a number: ")
        if input == 'done':
            print "Maximum is", large
            print "Minimum is", small
            break
        else:
            try:
                line = int(input)
                if small is None:
                    small = line
                elif input < small:
                    small = line
                elif large is None:
                    large = line
                elif input > large:
                    large = line
                else:
                    continue
                count = count + 1

            except:
                print "Invalid input"


 


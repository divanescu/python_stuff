#Exercise 6   Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters done. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
lst = list()

while True:
    input = raw_input("Enter a number: ")
    
    if input == 'done':
        print "Maximum is: ", max(lst)
        print "Minumum is: ",  min(lst)
        break
    else:
        try:
            number = float(input)
            lst.append(number)
        except:
            print "Bad input."
print "Full list: ",lst

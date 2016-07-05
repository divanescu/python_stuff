#Exercise 1  
#Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

#Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
def chop(lst):
    del lst[0]
    del lst[len(lst) - 1]
    return None

def middle(lst):
    del lst[0]
    del lst[len(lst) - 1]
    new = lst
    print "Middle:", new 

lst1=[0,1,2,3,4,5]
print "Original:", lst1
chop(lst1)
print "Chopped:", lst1
lst2 = [0,1,2,3,4,5]
middle(lst2)


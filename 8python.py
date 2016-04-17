#!/usr/bin/env python
#for loop, the script will validate a list of numbers inputed

userInput = raw_input('Enter a list of numbers between 1 and 100, separated bypaces: ')
nums = userInput.split()

for strNum in nums:
	if not strNum.isdigit():
		print 'Not a number:', strNum
	elif int(strNum) < 1:
		print 'Number is less than 1:', strNum
	elif int(strNum) > 100:
		print 'Number is greater than 100:', strNum
	else:
		print 'Number is valid:', strNum


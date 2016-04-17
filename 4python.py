#!/usr/bin/env python
# Some secure script that uses security
import sys

validPassword = 'secret' #this is the password.

inputPassword = raw_input('Please enter password: ')

if inputPassword == validPassword:
	print 'You have access!'
else:
	print 'Access denied!'
	sys.exit(0)

print 'Welcome!'

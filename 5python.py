#!/usr/bin/env python
# Years till retirement - args/variables
import sys

if len(sys.argv) > 1:
	name = sys.argv[1]
else:
	name = raw_input('Enter name:')

if len(sys.argv) > 2:
	age = int(sys.argv[2])
else:
	age = int(raw_input('Enter age:'))

sayHello = 'Hello ' + name + ','

if age == 67:
	sayAge = 'You just retired, old bastard'
elif age < 67:
	sayAge = 'You will retire in ' + str(67 - age) + ' years'
else:
	sayAge = 'You retired ' + str(age - 67) + ' years ago'

print sayHello, sayAge 

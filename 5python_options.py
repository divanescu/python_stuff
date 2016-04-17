#!/usr/bin/env python
# Years till retirement - args/variables
import sys
import optparse


parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='Your Name')
parser.add_option('-a', '--age', dest='age', help='Your Age', type=int)

(options, args) = parser.parse_args()

if options.name is None:
	options.name = raw_input('Enter Name:')

if options.age is None:
	options.age = int(raw_input('Enter Age:'))
	
sayHello = 'Hello ' + options.name + ','

if options.age == 67:
	sayAge = 'You just retired, old fart'
elif options.age == 66:
        sayAge = 'You will retire next year'
elif options.age == 68:
        sayAge = 'You retired last year'
elif options.age < 67:
	sayAge = 'You will retire in ' + str(67 - int(options.age)) + ' years'
else:
	sayAge = 'You retired ' + str(int(options.age) - 67) + ' years ago'

print sayHello, sayAge 

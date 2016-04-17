#!/usr/bin/env python
#counter script that runs until you press ctrl+c to end it 
#and it displays how long it was running, every second
import time

counter = 0

while 1:
	time.sleep(1)
	counter += 1

	print 'Script was looping for ', counter, 'seconds...'

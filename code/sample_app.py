#! /usr/bin/python
import os
import sys
import time

if len(sys.argv) == 2:
    print sys.argv[1]
else:
    print "NO External arguments were given"

for key, values in os.environ.items():
    print key
    print values


print "Code will go to sleep for 30 seconds and then will exit!"
time.sleep(30)
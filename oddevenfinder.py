#!/usr/bin/python
import os
from sys import argv
#a=input("Enter Number: ")
a = int(argv[1])

if a % 2 == 0:
	print "A is even"
else:
	print "A is odd"

#!/usr/bin/python
"""
This script shows number is odd or even.
./oddevenfinder.py <number>
"""
import os
from sys import argv
#a=input("Enter Number: ")
a = int(argv[1])

if a % 2 == 0:
	print "even"
	return "even"
else:
	print "odd"
	return "odd"

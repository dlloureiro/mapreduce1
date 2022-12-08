#!/usr/bin/python

import sys

maxSales = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
        	continue

	thisKey, thisSale = data_mapped

	if oldKey and oldKey != thisKey:
		print(oldKey+"\t"+str(maxSales))
		oldKey = thisKey;
		maxSales = 0
	oldKey = thisKey

	if float(maxSales) < float(thisSale):
		maxSales = thisSale

if oldKey != None:
	print(oldKey+"\t"+str(maxSales))

#!/usr/bin/python

import sys

maxPayment = {}

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
        	continue

	thisKey, thisSale = data_mapped

	if thisKey not in maxPayment.keys():
		maxPayment[thisKey] = float(thisSale)
	else:
		maxPayment[thisKey] += float(thisSale) 

for key, value in maxPayment.items():
	print(key + "\t" + str(value))

#!/bin/python

import sys
def birthdayCakeCandles(n, ar):
	max_height = max (ar)
	count = 0
	for i in ar:
		if (i == max_height):
			count += 1
	return count
	
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)

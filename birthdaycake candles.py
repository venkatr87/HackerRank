#!/bin/python

import sys
def birthdayCakeCandles(n, ar):
	max_height = max (ar)
	return ar.count(max_height)
	
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
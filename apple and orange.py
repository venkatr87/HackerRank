#!/bin/python

import sys



s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
i, j, count_apple, count_orange = 0, 0, 0, 0

while (i < len(apple)):
	if (a + apple[i] >= s and a + apple[i]<=t):
		count_apple += 1
	i += 1
print count_apple

while (j < len(orange)):
	if (b + orange[j] <= t and b + orange[j] >= s):
		count_orange += 1
	j += 1
print count_orange



		

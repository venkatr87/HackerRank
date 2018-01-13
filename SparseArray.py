import sys
import re

# initialization of variables
str, query = [], []
countq = 0

# Get the Number of strings
N = int(raw_input())

# Get the String list
for i in range(N):
	str.append(raw_input())
	
# Get the number of queries and query list
Q = int(raw_input())
for i in range(Q):
	query.append(raw_input())

# count the query in the string list
for j in range(Q):	
	for i in range(N):
		if re.search(r'\b' + query[j] + r'\b', str[i]):
			countq += 1
	print countq
	countq = 0
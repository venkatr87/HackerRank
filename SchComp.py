import sys
import re

pairs, templist, firstsection, secondsection, = [], [], [], []
i, j, k = 0, 1, 0

# Get the value for N for number of Students, P for number of pairs and the pairs of students studying in same section
N, P = map(int, raw_input().split(' '))
pairs = raw_input().strip('\(|\)')
p = re.split('\)\(|\s|',pairs)

# Temp array for firstsection is configured by comparing elements of input pairs
templist.insert(i, p[i])
templist.insert(j, p[j])
while (i < P):
	temp = p[i]
	while (j <= P):
		if (temp == p[j]):
			templist.append(p[j+1])	
		j += 1
	i += 1
	j = i + 1
	
# first section is configured from temp array after removing repeated elements
firstsection.insert(0, templist[k])
for k in templist:
	if k not in firstsection:
		firstsection.append(k)
		
# Secondsection is complement of input pairs with firstsection
for k in p:
	if k not in templist:
		if k not in secondsection:
			secondsection.append(k)

# print the output with all the combinations
for a in firstsection:
	for b in secondsection:
		print '(%s %s)' %(a, b),
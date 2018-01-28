import sys
import re
# Variable Initialization
count = 0

# Input the Number of waiting list passenger and queue status
N, Queue = raw_input().split(' ')
Q = re.split(',', Queue)
i = int(N)

# Counting of Swapping request
while(i > 1):
	if (i == 2):
		temp1 = Q[i-1]
		Q[i-1] = Q[i-2]
		Q[i-2] = temp1
		count += 1 
	else:
		temp1 = Q[i-1]
		#temp2 = Q[i-1]
		Q[i-1] = Q[i-2]
		Q[i - 2] = Q[i -3]
		Q[i - 3] = temp1
		count += 2
	i -= 3
print 'Number of requests = %d' %count
	
	

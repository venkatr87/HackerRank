import sys

a = []
LastAnswer = 0
seq = []

#Get the value for N and number of queries
N, Q = map(int, raw_input().split())

#Create Sequence List of N empty sequences
seq = [[] for i in range(N)]

# Get the query list, find index and print LastAnswer
for i in range(Q):
	Q, x, y = map(int, raw_input().split())
	index = (x ^ LastAnswer) % N
	if (Q == 1):
		seq[index].append(y)
	else:
		size = len(seq[index])
		pos = y % size
		LastAnswer = seq[index][pos]
		print LastAnswer


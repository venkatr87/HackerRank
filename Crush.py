import sys

# Initialization
seq = []
OperList = []

# Get the input size and number of operations
n, m = map(int, raw_input().split(' '))

# Create a list of 0 
for i in range(n):
	seq.append(0)

# Get the operations and create Operation List
for j in range(m):
	a, b, k = map(int, raw_input().split(' '))
	while (a <= b):
		seq[a-1] += k
		a += 1

# Find the max value in Operation List and print the max value
max = max(seq)
print max
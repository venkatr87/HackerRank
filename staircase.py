import sys

no_steps = int(raw_input().strip())
n_space = no_steps-1
n_hash = 1
for i in range(no_steps):
	for j in range(n_space):
		sys.stdout.write(' ')
	n_space -= 1
	for j in range(n_hash):
		sys.stdout.write('#')
	n_hash +=1
	print ''
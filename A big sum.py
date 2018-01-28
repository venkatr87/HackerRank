#print "Enter the number of inputs"
No_input = raw_input()
input = raw_input().split(' ')
sum = 0
for n in input:
	sum = sum + long(n)
print sum

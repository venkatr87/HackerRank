import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

j, sum1, sum2 = 0, 0, 0
m = n-1

for i in xrange(n):
	sum1 += a[i][j]
	j += 1
	sum2 += a[i][m]
	m -= 1
dif = abs(sum1 - sum2)
print dif
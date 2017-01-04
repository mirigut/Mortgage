def build_tribonachi(n):
	tri = [0,2,4,7]
	for i in xrange(4,n):
		tri.append(tri[i-1] + tri[i-2] + tri[i-3])
	return tri


n = 40
tri = build_tribonachi(n)
tri[0] = 1

n = 30
ans = 0
for loc in xrange(n+1):
	
	if loc == 0:
		cur = tri[n]
		first_part_size = 0
		second_part_size = n
	else:
		first_part_size = loc - 1
		second_part_size = n - loc
	cur = tri[first_part_size] * tri[second_part_size]
	ans += cur
	print "loc is",loc,"first",first_part_size,"second",second_part_size, cur
print ans


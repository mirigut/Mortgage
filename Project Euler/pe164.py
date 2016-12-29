def rec(level,n,arr):
	if (level == n):
		return 1
	prev_sum = 0
	if level == 0:
		prev_sum = 0
	elif level == 1:
		prev_sum = arr[0]
	else:
		prev_sum = arr[level-2] + arr[level-1]
	
	if prev_sum > 9:
		return 0
	ans = 0
	for j in xrange(10 - prev_sum):
		if (level == 0 and j == 0):
			continue

		arr[level] = j

		ans += rec(level+1,n,arr)
	return ans

n = 20
print rec(0,n,[0]*n)

import math

def isLamina(s,l,n):
	return l*l - s*s == n


def allDivisors(n):
	s = int(math.ceil(math.sqrt(n)))
	count = 0
	pairs = set()
	for i in xrange(2,s+1):
		if (n % i == 0):
			a = (i + n/i)/2
			b = n/i - a
			if (a !=0 and b!= 0 and a%2 == b%2):
				if (a < b):
					if (b*b - a*a == n):
						pairs.add(str(a) + "," + str(b))
				else:
					if (a*a - b*b == n):
						pairs.add(str(b) + "," + str(a))
			
				count += 1
	return pairs


def allUnder(n):

	all_pairs = set()
	for i in xrange(2,n+1):
		if i % 1000 == 0:
			print i
		s = allDivisors(i)
		all_pairs = all_pairs.union(s)

	
	#for a in all_pairs:
	#	print a
	print len(all_pairs)

	

allUnder(1000001)

#a^2 - b^2 = 32
#(a+b)(a-b) = 32
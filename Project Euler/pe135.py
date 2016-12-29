import math

def find(n):
	print "-"*15 + " " +  str(n) + " " + "-"*15
	print " "
	for y in xrange(2,n*n*n):
		d = float(n + y*y) / float(4 * y)
		if (d == math.floor(d)):
			x = int(y + d)
			z = int(y - d)
			x = int(x)
			s= str(x)+"^2 - "+str(y)+"^2 - "+str(z)+"^2 = "+str(n)
			print s
	print " "

# ---------------------------------------------------------------------------------

def getDivisors(n,l):
	lim = int(math.sqrt(n)) + 1
	flag = False
	newset = set()
	for i in xrange(2,lim):
		if n % i == 0:
			oldset = l[n/i]
			newset = set()
			newset.add(i)
			for s in oldset:
				newset.add(s)
				newset.add(s*i)
			flag = True
			break
	if len(newset) == 0:
		newset = {n}
	l.append(newset)

	return l

def findAllDivisors(last_val):
	l = list()
	l.append({0})
	l.append({1})
	l.append({2})
	for n in xrange(3,last_val):
		l = getDivisors(n,l)
		
	return l

def findSolsOld(n,divs):
	if (len(divs) < 10):
		return 0
	c = 0
	for div in divs:
		for d in xrange(1,n):
			x = div + d
			y = div
			z = div - d
			if z <= 0:
				continue
			if x*x - y*y - z*z == n:
				c += 1
	return c

def findSols(n,divs):
#	if (len(divs) < 10):
#		return 0
	c = 0
	for y in divs:
		d = float(n + y*y)/float(4*y)
		if (math.floor(d) == d and int(y)!=int(d) and y-d > 0):
			c += 1
		
	return c

n = 1000000
divs = findAllDivisors(n+6)

#print findSols(1155,divs[1155])
#print "-"*50
#print findSolsOld(1155,divs[1155])

count = 0
for i in xrange(2,n):
	c = findSols(i, divs[i])
	if c == 10:
		count += 1
		print i, count
print "count is ", str(count)



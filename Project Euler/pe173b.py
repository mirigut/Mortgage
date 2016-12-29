import math

def checkDivs(n,i):
	if (n % i != 0):
		return False
	j = n / i
	print "divisors:",str(i), "," ,str(j)
	if (i + n/i) % 2 == 1:
		print "Different signs of divisors"
		return False
	a = (i + n/i)/2
	b = n/i - a
	print "Thus a and b are",str(a),",",str(b)
	if (a*a - b*b != n):
		print "Big Problem!"
		return False
	if (a%2 != b%2):
		print "Bad since a != b (mod 2)"
		return False
	return True

def allPairs(n):
	print " "
	print "*"*20
	print n
	print "*"*20
	for i in xrange (2,int(math.sqrt(n))+1):
		if n % i == 0:
			boo1 = checkDivs(n,i)
			boo2 = i % 2 == 0 and (n/i) % 2 == 0
			if (boo1 == boo2 and not boo1):
				print "V both flase"
			elif (boo1 == boo2 and boo1):
				print "V both true"
			else:
				print "WOWOWOWOW"
				return


#for n in xrange(12,501,4):
#	allPairs(n)




#----------------------------------

def howManyDivisorPairs(n):
	lim = int(math.ceil(math.sqrt(n)))
	count = 0
	for i in xrange (1,lim):
		if n % i == 0:
			count += 1
	return count

c = 0
for i in xrange(2,1000001):
	if i % 4 == 0:
		c += howManyDivisorPairs(i / 4)
		print i,howManyDivisorPairs(i / 4)

print c
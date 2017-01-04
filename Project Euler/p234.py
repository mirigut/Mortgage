import math

def isPrime(n):
	lim = int(math.sqrt(n))
	for i in xrange(2,lim + 1):
		if n % i == 0:
			return False
	return True

def firstNPrimes(n):
	primes = []
	for i in xrange(2,n + 1):
		if isPrime(i):
			primes.append(i)
	return primes


def sumOfAllMultiplesInRange(start,fin,n):
	rstart = int(math.ceil(start / float(n))) * n
	rfin = int(math.floor(fin / float(n))) * n
	num_of_n_div = (rfin - rstart)/n + 1
	return	max((rfin + rstart) * num_of_n_div/2.0, 0)

def allSquaresBetween(k,l,top):
	if (k*k > top):
		return 0	
	the_top = min(top,l*l-1)

	sl = sumOfAllMultiplesInRange(k*k+1,the_top,l)	
	sk = sumOfAllMultiplesInRange(k*k+1,the_top,k)

	if (k*l > top):
		sboth = 0
	else:
		sboth = 2*k*l
	return int(sk + sl - sboth)



top = 999966663333
sqtop = int(math.ceil(math.sqrt(top)))*2
primes =  firstNPrimes(sqtop)
s = 0
for i in xrange(1,len(primes)):
	s += allSquaresBetween(primes[i-1],primes[i],top)

print s





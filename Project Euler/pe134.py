import math
import time


def isPrime(n):
	lim = int(math.sqrt(n))
	for i in xrange(2,lim + 1):
		if n % i == 0:
			return False
	return True

def firstNPrimes(n):
	primes = []
	for i in xrange(4,n + 1):
		if isPrime(i):
			primes.append(i)
	return primes

def findS(p1,p2):
	flag = False
	i = 0
	ten_pow = int(math.pow(10,int(math.log(p1)/math.log(10) + 1)))
	while (not flag):
		i += 1
		if (p2 * i % ten_pow == p1):
			return i * p2

n = 1000000
start_time = time.time()
primes = firstNPrimes(n)
print (primes)


print("--- finished finding the primes %s seconds ---" % (time.time() - start_time))
print("--- found %s primes ---" % len(primes))

s = 0
for i in xrange(len(primes)-1):
	if i % 1000 == 0:
		print ("--- now in %s ---" % i)
	p1 = primes[i]
	p2 = primes[i+1]
	s += findS(p1,p2)

print s


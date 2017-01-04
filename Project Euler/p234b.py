import math

a = 31
b = 37

divA = 0
divB = 0
divBoth = 0
s = 0
top = 1000
for i in xrange(a*a+1,min(b*b-1,top)):
	if i%a == 0:
		divA += i
	if i%b == 0:
		divB += i
	if i%a == 0 and i%b ==0:
		divBoth += i
	if (i%a == 0 and i%b !=0) or (i%b ==0 and i%a != 0):
		s += i




print divA
print divB
print divBoth
print "---"
print s


#5394
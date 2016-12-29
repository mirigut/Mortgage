import numpy
import math

nper = 5
rate = 0.04
pv = 500000
inflation = 0.025

first_payment = -numpy.pmt(rate / 12, nper * 12, pv)

balance = [0]
rate_return = [0]
fund_return = [0]
total_return = [0]
final_balance = [0]


balance.append(pv*(inflation/12+1))
rate_return.append(balance[1]*rate/12)
total_return.append(-numpy.pmt(rate / 12, nper * 12 - 1 + 1, balance[1]))
fund_return.append(total_return[1] - rate_return[1])
final_balance.append((balance[1] - fund_return[1])*(inflation/12+1))

#for i in xrange(2,nper * 12):
for i in xrange(2,nper * 12 + 1):
	balance.append(final_balance[i-1])
	rate_return.append(balance[i]*rate/12)
	if balance[i] <= 0:
		total_return.append(0)
	else:
		total_return.append(-numpy.pmt(rate / 12, nper * 12 - i + 1, balance[i]))
	fund_return.append(total_return[i] - rate_return[i])
	if balance[i] <= 0:
		final_balance.append(0)
	else:
		final_balance.append((balance[i]-fund_return[i])*(inflation/12+1))

for i in xrange(1,nper * 12 + 1):
	if (i % 15 == 0):
		print "Month ; Balance ; Rate return ; Func return ; Total Return"
	print i,";",balance[i],";",rate_return[i],";",fund_return[i],";",total_return[i]

print ""
print ""
paid_money = sum(total_return)
print "Loan sum:               ",pv
print "Total paid:             ",paid_money
print "First monthly payment:  ", min(total_return[1:])
print "Max monthly payment:    ", max(total_return)
print "Average monthly payment:", numpy.mean(total_return)


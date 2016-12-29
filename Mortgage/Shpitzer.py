import numpy

nper = 20
rate = 0.04
pv = 300000
inflation = 0.02

first_payment = -numpy.pmt(rate / 12, nper * 12, pv)

print first_payment

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
	print i,balance[i],rate_return[i],fund_return[i]



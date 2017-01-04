import numpy
import math

def build_table(months,rate,pv,inflation):
	balance = [0]
	rate_return = [0]
	fund_return = [0]
	total_return = [0]
	final_balance = [0]


	balance.append(pv*(inflation/12+1))
	rate_return.append(balance[1]*rate/12)
	total_return.append(-numpy.pmt(rate / 12, months - 1 + 1, balance[1]))
	fund_return.append(total_return[1] - rate_return[1])
	final_balance.append((balance[1] - fund_return[1])*(inflation/12+1))

	for i in xrange(2,months + 1):
		balance.append(final_balance[i-1])
		rate_return.append(balance[i]*rate/12)
		if balance[i] <= 0:
			total_return.append(0)
		else:
			total_return.append(-numpy.pmt(rate / 12, months - i + 1, balance[i]))
		fund_return.append(total_return[i] - rate_return[i])
		if balance[i] <= 0:
			final_balance.append(0)
		else:
			final_balance.append((balance[i]-fund_return[i])*(inflation/12+1))

	'''for i in xrange(1,nper * 12 + 1):
		if (i % 15 == 0):
			print "Month ; Balance ; Rate return ; Func return ; Total Return"
		print i,";",balance[i],";",rate_return[i],";",fund_return[i],";",total_return[i]
	'''

	paid_money = sum(total_return)
	print "Loan period in months:  ",months, "(" , months/12.0,"years )"
	print "Loan sum:               ",pv
	print "Total paid:             ",paid_money
	print "First monthly payment:  ", min(total_return[1:])
	print "Max monthly payment:    ", max(total_return)
	print "Average monthly payment:", numpy.mean(total_return)


nper = 30
rate = 0.036
pv = 440000
inflation = 0.025
wanted_pmt = 10000

first_payment = -numpy.pmt(rate / 12, nper * 12, pv)

needed_months = int(math.ceil(numpy.nper(rate / 12, -wanted_pmt, pv)))

build_table(needed_months,rate,pv,inflation)
import datetime
from dateutil.relativedelta import relativedelta

def yearsBetweenDates(start_date, end_date):
     return relativedelta(end_date, start_date).years


def monthsBetweenDates(start_date, end_date):
    return relativedelta(end_date, start_date).years*12 + relativedelta(end_date, start_date).months

def getNetWorthFbStocks(buy_date):
    fb_grants = [73558.70, 4163.70, 48156.56]
    fb_grants_dates = [datetime.date(2015, 12, 15),datetime.date(2016, 3, 15),datetime.date(2017, 3, 15)]

    total = 0

    fb_number_of_stocks = [770, 40, 344]

    fb_stock_price = 179.36
    usd_in_nis = 3.39

    fb_grants_current_value = [x * fb_stock_price for x in fb_number_of_stocks]
    fb_grants_after_taxes = []
    for i in xrange(len(fb_grants)):
        fb_grants_after_taxes.append((fb_grants[i] * 41/100) + max(0,fb_grants_current_value[i]-fb_grants[i])*75/100)
        years_since_granted = min(yearsBetweenDates(fb_grants_dates[i], buy_date),4)
        if (years_since_granted >= 2):
            total += (fb_grants_after_taxes[i]/4)*years_since_granted

    return total*usd_in_nis

def getSavingsSmart(buy_date, yearly_interest, saving_per_month):
    monthly_interest = yearly_interest/12.0
    months = monthsBetweenDates(datetime.date.today(), buy_date)
    money = getBase()
    for i in xrange(months):
        money = money + money*(monthly_interest) + saving_per_month
    return money

def getBase():
    return 547426.82 + 247126.63

def getMoney(date, yearly_interst, saving_per_month ,isStock):
    total = getSavingsSmart(date, yearly_interst, saving_per_month)
    if (isStock):
        total += getNetWorthFbStocks(date)

    return round(total,2)


def print_table(table):
    wi = 15
    sep = "-"*48
    spe_sep = ("-"*15 + "|")*3
    print sep
    for i in xrange(len(table[0])):
        stri = ""
        for j in xrange(len(table)):
            table[i][j] = "  " + table[i][j]
            stri = stri + table[i][j] + " "*(wi - len(table[i][j])) + "|"
        print stri
        print spe_sep


# ----------------------------------------------------------------

months_from_now = 24
buy_date = datetime.date.today() + relativedelta(months=+months_from_now)
yearly_interest = 0.03
saving_per_month = 15000

print "=" * 200
print ""
print "Current savings:", getBase()
print "In", round(monthsBetweenDates(datetime.date.today(), buy_date)/12.0,2),"years (" + str(months_from_now),"months):"
print "-"*48
print "Yearly interest: " + str(yearly_interest*100) + "%"
print "Monthly savings: " + str(saving_per_month)

stock_no_int = str(getMoney(buy_date, 0, saving_per_month, True))
stock_int = str(getMoney(buy_date, yearly_interest, saving_per_month, True))

no_stock_no_int = str(getMoney(buy_date, 0, saving_per_month, False))
no_stock_int = str(getMoney(buy_date, yearly_interest, saving_per_month, False))

w, h = 3, 3;
table = [["a" for x in range(w)] for y in range(h)]
table[0][0] = ""
table[0][2] = "No Stock"
table[0][1] = "Stock"
table[1][0] = "No interest"
table[2][0] = "Interest"
table[1][2] = no_stock_no_int
table[1][1] = stock_no_int
table[2][2] = no_stock_int
table[2][1] = stock_int

print_table(table)

print ""
print "=" * 200

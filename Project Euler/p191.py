
LATE   = "L"
ONTIME = "O"
ABSENT = "A"

def copyArr(a):
	b = []
	for el in a:
		b.append(el)
	return b

def checkIfGoodReport(report):
	late_ocasions = 0
	consec_absent = 0
	for r in report:
		if r == ABSENT:
			consec_absent += 1
			if consec_absent > 2:
				return False
		elif r == ONTIME:
			consec_absent = 0
	return True

def checkDays(level,maxLevel,report,late_ocasions,consec_absent):
	if level == maxLevel:
		if checkIfGoodReport(report):
			print report
			return 1

		else:
			return 0
	s = 0
	if (consec_absent < 2):
		new_report = copyArr(report)
		new_report.append(ABSENT)
		s += checkDays(level+1,maxLevel,new_report,late_ocasions,consec_absent + 1)
	new_report = copyArr(report)
	new_report.append(ONTIME)
	s += checkDays(level+1,maxLevel,new_report,late_ocasions,0)

	return s

print checkDays(0,5,[],0,0)

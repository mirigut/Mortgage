
LATE   = 0
ONTIME = 1
ABSENT = 2

def copyArr(a):
	b = []
	for el in a:
		b.append(el)
	return b

def checkIfGoodReport(report):
	late_ocasions = 0
	consec_absent = 0
	for r in report:
		if r == LATE:
			late_ocasions += 1
			consec_absent = 0
			if late_ocasions > 1:
				return False
		elif r == ABSENT:
			consec_absent += 1
			if consec_absent > 2:
				return False
		elif r == ONTIME:
			consec_absent = 0
	return True

def checkDays(level,maxLevel,report,late_ocasions,consec_absent):
	if level == maxLevel:
		if checkIfGoodReport(report):
			return 1
		else:
			return 0
	s = 0
	# LATE
	if (late_ocasions == 0):
		new_report = copyArr(report)
		new_report.append(LATE)
		s += checkDays(level+1,maxLevel,new_report,late_ocasions + 1,0)
	if (consec_absent < 2):
		new_report = copyArr(report)
		new_report.append(ABSENT)
		s += checkDays(level+1,maxLevel,new_report,late_ocasions,consec_absent + 1)
	new_report = copyArr(report)
	new_report.append(ONTIME)
	s += checkDays(level+1,maxLevel,new_report,late_ocasions,0)

	return s

print checkDays(0,30,[],0,0)

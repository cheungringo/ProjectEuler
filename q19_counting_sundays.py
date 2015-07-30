'''
Stated problem:
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Main problem: 
Need day fo week for Jan 1st, 1901
Count from January 1st 1901 all the way until December 31st 2000 while keeping track of day of the week
Solution: Store the number of days in the month in an array, begin each year by checking if leap and if so replacing the 28 in February with 29
Runtime: # of days in the century so O(n)
'''

Months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def CheckLeap(year):
	'''
	Returns True if the year is a leap year and False if it is not.
	'''
	if year % 100 == 0:
		if year % 400 == 0:
			return True
	elif year % 4 == 0:
		return True
	else:
		return False

def GetDayOfWeek(month, dayOfWeek):
	for day in range(Months[month]):		
		if dayOfWeek == 7:
			dayOfWeek = 1
		else:
			dayOfWeek += 1
	return dayOfWeek


def CountSundays(start, end, dayOfWeek):
	'''
	Returns the number of Sundays landing on the first of the month.
	start is the first year and end is the last year.
	It is assumed that this problem begins on the first day of the first year and ends
	on the last day of the last year.
	'''
	sundays = 0
	for year in range(start, end + 1):
		if CheckLeap(year):
			Months[1] = 29
		else:
			Months[1] = 28
		for month in range(len(Months)):
			if dayOfWeek == 7:
				sundays += 1
			dayOfWeek = GetDayOfWeek(month, dayOfWeek)
	return sundays

def GetStart(dayOfWeek, start, end):
	'''
	Returns the day of week of the first day of the end year
	using the day of week of the first day of the start year
	'''
	for year in range(start, end):
		if CheckLeap(year):
			Months[1] = 29
		else:
			Months[1] = 28
		for month in range(len(Months)):
			dayOfWeek = GetDayOfWeek(month, dayOfWeek)
	return dayOfWeek

print(CountSundays(1901, 2000, GetStart(1, 1900, 1901)))

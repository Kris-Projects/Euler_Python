"""
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
"""

###################################SOLUTION###############################
import datetime
from calendar import monthrange
import calendar

begin = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)
count = 0
while begin <= end:
    if begin.weekday() == 6:
        count += 1
    begin += datetime.timedelta(days=monthrange(begin.year, begin.month)[1])

print(count)
##############################################################
count2 = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if calendar.monthrange(i, j)[0] == 6:
            count2 += 1
print(count2)

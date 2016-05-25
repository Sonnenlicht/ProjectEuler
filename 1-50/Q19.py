#Counting Sundays
#Problem 19
#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import time
from datetime import date, timedelta

#def parse_date(date_string):
#    return datetime.strptime(date_string, "%Y-%m-%d")

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

date1 = date(1901, 1, 1)
date2 = date(2000, 12, 31)

time_diff = abs(date2 - date1)
print(time_diff.days)
print(date1.weekday())

total = 0
for single_date in daterange(date1, date2):
    #print(single_date.strftime("%Y-%m-%d"))
    #print(single_date.day)
    if single_date.day == 1:
        if single_date.weekday() == 6:
            #print(single_date.strftime("%Y-%m-%d"))
            total += 1
print(total)
    #time.sleep(1)

#for n in range(time_diff.days):
#    currdate = date1 + timedelta(n)
#    weekday = currdate.weekday()
#    print(date1.day)
#    print(date1 + timedelta(n))
#    time.sleep(1)
    

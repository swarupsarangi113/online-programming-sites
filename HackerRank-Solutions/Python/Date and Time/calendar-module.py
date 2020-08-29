# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
# import calendar

# week = ('MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY')

# m,d,y = map(int,input().split())
# weekday = calendar.weekday(y,m,d)
# print(week[weekday])

import datetime

m,d,y = map(int,input().split())
print(datetime.date(y,m,d).strftime('%A').upper())

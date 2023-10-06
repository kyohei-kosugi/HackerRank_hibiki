import calendar

month, day, year = map(int, input().split())
date = (year, month, day)
weekday = calendar.weekday(*date)
weekday_string = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
result = weekday_string[weekday].upper()

print(result)
from calendar import day_name, weekday


month, day, year = map(int, input().split())

# Get name of the weekday specified by the given date.
week_day = day_name[weekday(year, month, day)]
print(week_day.upper())

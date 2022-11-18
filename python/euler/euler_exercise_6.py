months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

start, end = 1901, 2000

years = range(start, end)
leap_years = range(1904, 2001, 4)

Sundays = 0
days = 1
for year in years:
  if year in leap_years:
    months[2] = 29 
  else:
    months[2] = 28

  for month in range(1, 13):
    for day in range(1, months[month]+1):
      if days == 7:
        if day == 1:
          print(year, month, day)
          Sundays += 1
        days = 1
      else:
        days += 1


print(Sundays)
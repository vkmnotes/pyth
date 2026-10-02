from datetime import datetime,date
import calendar
import time
print("Current date and time:",datetime.now())
d1=date(2026,1,1)
d2=date(2026,7,31)
print("Difference in days:",(d2-d1).days)
print("\nCalendar for July 2026:")
print(calendar.month(2026,7))
start=time.time()
total=sum(range(1000000))
end=time.time()
print("Sum of 1M numbers:",total)
print("Time taken:",round(end-start,6),"seconds")
dates=[date(2026,5,10),date(2026,1,15),date(2026,3,22)]
print("\nSorted dates:",sorted(dates))

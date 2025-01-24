#first day in caleday is set as sunday
import calendar
c = calendar.TextCalendar(calendar.SUNDAY) 

str = c.formatmonth(2025,6)
print("calender:")
print(str)
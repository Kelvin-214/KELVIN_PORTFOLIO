import calendar

# Create a plain text calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
# Display the calendar for a specific month and year
print(cal.formatmonth(2024, 9))

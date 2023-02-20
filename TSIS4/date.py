import datetime
today = datetime.datetime.now()

#Write a Python program to subtract five days from current date.
day_5 = today - datetime.timedelta(days = 5) 
# print (day_5) # today (2023.02.19) ouput 2023-02-14 19:30:01.727583

#Write a Python program to print yesterday, today, tomorrow.
tomorrow = today + datetime.timedelta(days = 1)
yesterday = today - datetime.timedelta(days = 1)
i = 0
# print (yesterday)
# print (today)
# print (tomorrow)

#Write a Python program to drop microseconds from datetime.
delete_microseconds = today - datetime.timedelta(microseconds = today.microsecond)
# print (delete_microseconds)

#Write a Python program to calculate two date difference in seconds.
from datetime import datetime
date_1 = '2023-2-20 23:26:08'
date_2 = '2023-2-17 11:45:18'
date_format_str = '%Y-%m-%d %H:%M:%S'
start = datetime.strptime(date_1, date_format_str)
end = datetime.strptime(date_2, date_format_str)
diff = abs(end - start)
# print(diff.total_seconds())
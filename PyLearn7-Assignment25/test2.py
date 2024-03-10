from datetime import datetime

# current date and time
date_time = datetime.now()
print(date_time)
# format specification
format = '%H:%M:%S'

# applying strftime() to format the datetime
string = date_time.strftime(format)

# print('Date and Time:', string)

# Output:
# Date and Time: 2022-06-30 15:30:00

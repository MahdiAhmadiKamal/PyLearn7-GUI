import time
import pytz
from datetime import datetime

a=pytz.timezone('Asia/Tehran')
b = datetime.now(a).strftime('%H:%M:%S')
print(b)


c=pytz.timezone('Europe/Berlin')
d = datetime.now(c).strftime('%H:%M:%S')
print(d)

e=pytz.timezone('US/Eastern')
f = datetime.now(e).strftime('%H:%M:%S')
print(f)
print(type(f))

g = pytz.all_timezones
print(g)
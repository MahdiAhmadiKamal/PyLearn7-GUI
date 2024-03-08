import time
import pytz
from datetime import datetime

a=pytz.timezone('Asia/Tehran')
b = datetime.now(a).strftime('%H:%M:%S')
print(b)


c=pytz.timezone('Europe/Berlin')
d = datetime.now(c).strftime('%H:%M:%S')
print(d)

e=pytz.timezone('US/Central')
f = datetime.now(e).strftime('%H:%M:%S')
print(f)
print(type(f))
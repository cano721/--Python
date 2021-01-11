import time
import datetime

t = time.time()
print(t) # 1970. 1. 1~ 현재까지의 초
localtime = datetime.datetime.now()
print(localtime)
print(type(localtime))

print(localtime.year)
print(localtime.month)
print(localtime.day)
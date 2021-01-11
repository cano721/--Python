import time

start = time.time()
for i in range(1,100):
    print(i)
    time.sleep(0.05)

end = time.time()

print(end- start)
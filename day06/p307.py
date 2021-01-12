print('start....')
f = None
try:
    f = open('live.txt','rt',encoding = 'UTF-8')
    for text in f:
        print(f, end = '')
    print(text)
except:
    print('Error....')
finally:
    if f != None:
        f.close()

print('end....')
print('start...')
f = None
try:
    f = open('live.txt','rt')
    text = f.read()
    print(text)
except:
    print("File Not Found....")
finally:
    if f != None:
        print('close....')
        f.close()
print('end')



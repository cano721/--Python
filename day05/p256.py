d =[1,2,3]

def f1(a):
    a[0] =100
    return a

c = f1(d)

print(d)
print(c)

if(d is c):
    print('ok')
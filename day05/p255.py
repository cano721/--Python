a = 10;

def f1(c):
    c += 5;
    return c

b = f1(6)
print(a)
if( a == b):
    print('ok')
if( a is b):
    print('ok')

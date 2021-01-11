data =100;

def calcsum(n):
    sum = 0;
    for d in n:
        sum += d;
    return sum;

def f1():
    data = 100;
    return data;

def f2(s, e):
    sum =0;
    for data in range(s, e+1):
        sum += data;
    avg = sum / (e-s+1);
    return avg;

def f3(s, e):
    sum =0;
    for data in range(s, e+1):
        sum += data;
    avg = sum / (e-s+1);
    print('Result: ');
    print(avg);

def f4(*n):
    sum = 0;
    for d in n:
        sum += d;
    return sum;

def f5(m, *n):
    sum = 0;
    for d in n:
        sum += d;
    return sum+ m;

def f6(begin, end, step=1):
    """begin 시작 숫자, end는 끝 숫자, step은 몇증가씩으로 할건지 1로둔건 초기값"""

    sum = 0;
    for d in range(begin, end+1, step):
        sum += d;
    return sum;

def f7(**args):
    b = args['b'];
    e = args['e'];
    s = args['s'];
    sum = 0;
    for d in range(b, e+ 1, s):
        sum += d;
    return sum;

def f8(n, *m, **args):
    print('test');
    print(n);
    print(m);
    print(args);
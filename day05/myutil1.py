def sum(a,b):
    result = a+b
    return result

def calc(n):
    if n <= 0:
        raise ValueError;
    result = 10 / n;
    return result;

def input(n):
    if n == 10000:
        raise ValueError
    return n
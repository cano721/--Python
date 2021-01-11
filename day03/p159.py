data =20;
def calcsum(n):
    sums = 0;
    for d in range(n+1):
        sums += d;
    return sums+data;

result = calcsum(10);
print(result);

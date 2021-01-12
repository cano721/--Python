import math
from array import array
from decimal import Decimal
from fractions import Fraction

n = 0.1
n = Decimal(str(n))
sum = 0
for i in range(10):
    sum += n
print(sum)

result = 1/3
result = round(result, 3)
print(result)

resultf1 = Fraction(1,3)
resultf2 = Fraction(1,4)
print(resultf1 + resultf2 + 0.0)

data = [1,2,3,6,5,4,3]
ar = array('i',data)
ar[1] =100
ar.append(200)
del ar[0]
for i in ar:
    if i%2 ==0:
        print(i, end=',')
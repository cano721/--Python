import random;

#0.0~ 0.999999999999(1.0미만)
rn = random.random();
print(rn);
sum =[];

for i in range(1,8):
    lotto = random.randint(1,45);
    sum.append(str(lotto));
print(sum);


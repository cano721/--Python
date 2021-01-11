import random

score = (10,20,30,40)
print(score[0])
score = score + (50,60,70)
print(score)
scoreList = list(score);
print(scoreList)

t =[];
for i in range(1,7):
    temp = random.randint(1,3)
    t.append(temp);

print(t)

tp = tuple(t);
print(tp);
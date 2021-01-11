score = [];
score1= [10,20,30,40,50,60,70,80];
temp = score1[1:5];
print(temp);

sum = 0;
for i in score1:
    sum += i;

print('Result: %d %10.2f' % (sum,sum/len(score1)));

score2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]];
#print(score2[1]);

total = 0;
totalcnt = 0;

for i in score2:
    sum2 = 0;
    cnt2 = 0;
    for d in i:
        print(d,end=' ');
        sum2 +=d;
        cnt2 +=1;
        totalcnt +=1;
    print();
    total += sum2;
    avg2 = sum2/cnt2;
    print("리스트의 합: %d" % sum2)
    print("리스트의 평균: %.2f" %avg2)

avg1 = total/totalcnt;
print("전체 리스트의 합 : %d" %total)
print("전체 리스트의 평균: %.2f" %avg1)


# 각 리스트의 합 평균을 출력하고
# 전체 합과 평균을 출력 하시오
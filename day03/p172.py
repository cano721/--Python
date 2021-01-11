str1 = 'python';

print(len(str1));
print(str1[0]);
print(str1[-3]);

for i in str1:
    print(i, end=',');

print();

for i in range(len(str1)):
    print(str1[len(str1)-i-1], end=',');

print();


#str1[1]= 'e';
print(str1);
print(str1[3:]);
print(str1[:3]);
print(str1[2:-2]);
print(str1[0:4:2]);

filename = '20210104-1324.jpg';
# 2021년 1월 4일
#1시 24분
#파일 형식 jpg
#함수로 만드시오

def slice(n):
    print(n[0:4]+ '년' + n[4:6]+'월' + n[6:8] + '일');

slice(filename);

num = 100;
hnum = '100';
str1 = 'result:';
str2 = 'won';
print('result: ' + str(num) + 'won');

print('%s %.2f %s' % (str1,num,str2));
print('%s %d %s' % (str1,num,str2));

print('%10d%%' % num);

nums1 = [1000,2000,30,210000];
for n in nums1:
    print('Price : %d Won' %n);
s = [];
s.append(20)
s.append(30)
s.append(10)
s.append(40)
s.append(50)
s.insert(2,99);
s[3] = [1,2,3];
del(s[0])
s.remove(50)
number = s.pop()
print(number)
print(s.index(99));
s.append(30)
print(s.count(30))
print(s)

str = ['A','B','C','D','D']

if 'A' in str:
    str.remove('A')
else:
    str.append('B');

print(str);
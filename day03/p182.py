str = '         python        ';
str = str.upper();
print(str);
print(str.lstrip());
print(str.rstrip());
print(str.strip());

s1 = 'a b c d';
s2 = 'a - b - c - d';
r1 = s1.split(' ');
r2 = s2.split('-');

for i in r2:
    print(i.strip());

s3 = '[python]';
s4 = s3.replace('[','').rstrip();
s4 = s4.replace(']','').rstrip();
print(s4);
s = 'python programming';
print(type(s));
print(type(s[0]));

print(len(s));
print(s.find('o'));
print(s.rfind('o'));
print(s.index('o'));
print(s.rindex('o'));
print(s.count('o'));

print('a' in s);
print('a' not in s);

if('a' in s):
    print('Ok');
else:
    print('No');

if str.startswith('p'):
    print('OK');


if str.endswith('g'):
    print('OK');

    
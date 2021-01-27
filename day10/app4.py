str = '3+4+5'
strList = '[1,2,3,4,5]'

print(eval(str))
print(strList)

for i in eval(strList):
    print(i)

user ="""[{'id':'id01', 'name':'james'},
{'id':'id01', 'name':'james'},
{'id':'id01', 'name':'james'}
      ]"""

us = [{'id':'id01', 'name':'james'},
{'id':'id01', 'name':'james'},
{'id':'id01', 'name':'james'}
      ]

usstr = repr(us)
print(usstr)
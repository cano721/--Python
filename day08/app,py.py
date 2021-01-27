from sqlitedb import *;
from value import *;

print('start ...')
sqldb = sqliteDb('udb.db')
sqldb.makeTable()
u = User('id03','pwd01','james',28)
userList = sqldb.select()
for us in userList:
    print(us.id + ' ' + us.name + ' '+ str(us.age))
print('---------------------------------')
userone = sqldb.selectone('id01')
print(userone)
sqldb.delete('id02')
print('end ...')
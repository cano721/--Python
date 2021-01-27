from sqlitedb import *

sqliteDb = sqliteDb('udb.db')
userList = sqliteDb.select()
for u in userList:
    print(u)
print('---------------------')
userList = sqliteDb.select()
for u in userList:
    print(u)
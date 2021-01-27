from userdb import *
from itemdb import *
from value import *
import pymysql;


# 1. 사용하고자하는 데이터베이스 이름을 이용한다.
# sqlitedb = SqliteDb('shopdb.db')
udb = UserDb('shopdb.db')
# 2. 테이블을 생성한다. 단, 존재 하지 않으면
udb.makeTable()

# 3. 사용자 테이블을 사용하기 위해 userdb 객체를 이용하여 CRUD 진행
user = User('id01','pwd01','james',20)
# udb.insert(user)

userList = udb.select()
print(userList)
for u in userList:
    print(u)

# idb = ItemDb('shopdb.db')
# item = Item('it01','pants',10000)
# idb.insert(item)
# itemList = idb.select()
# for it in itemList:
#     print(it)
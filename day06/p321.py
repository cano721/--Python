import sqlite3
import dbutil

print('Start ...')
try:
    #1. sqlite에 접속한다.
    dbutil.connectDB('hb.db')
    #2. 테이블을 만든다
    dbutil.makeTable()
    #3. 사용자 정보를 입력 한다.
    user = ['id07','pwd07','홍말숙','01077776666','경기',20]
    #dbutil.insertUser(user)

    #3-1. 한명 조회
    oneUser = dbutil.selectOneUser('id02')
    print(oneUser)

    #3-2. 수정
    user = ['id01', 'pwd01', '이말숙', '01077776666', '경기', 20]
    dbutil.updateUser(user)

    #3-3. 삭제
    dbutil.deleteUser('id07')


    #4. 사용자 정보를 조회 한다.
    allusers = dbutil.selectUser()
    #[[],[],[]]
    for u in allusers:
        print("%s,%s,%s,%s,%s,%d" % (u[0],u[1],u[2],u[3],u[4],u[5]))
    #5. sqlite에 close 한다.
except sqlite3.IntegrityError:
    print("Duplicated ID Except ...")
finally:
    dbutil.closeDB()
print('End...')
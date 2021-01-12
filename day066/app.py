import sqlite3
import dbutil

print('Start ....')
while True:
    dbutil.connectDB('hb.db')
    try:
        menu = input('***DB만들기***\n'
                     '테이블만들기(m)\n'
                     '사용자정보추가(i)\n'
                     '사용자전체정보조회(a)\n'
                     '사용자정보조회(s)\n'
                     '사용자정보삭제(d)\n'
                     '사용자정보수정(u)\n'
                     '나가기(q)');
        menu = menu.lower()
        if menu == 'q':
            print('Bye')
            break
        #테이블 만들기
        if menu == 'm':
            name = input('만드실 테이블 명을 적어주십시오')
            dbutil.makeTable(name)
        #사용자정보추가
        if menu == 'i':
            user = input('테이블이름과 추가할 사용자의 정보를 입력하세요\n'
                         'tableName,id,pwd,name,phone,addr,age\n'
                         '(띄어쓰기기준)')
            user = user.split(' ')
            userdata = []
            for u in user:
                userdata.append(u)
            dbutil.insertUser(userdata)
        #사용자전체정보조회
        if menu =='a':
            table = input("조회하실 테이블명을 선택해주세요")
            allusers = dbutil.selectUser(table)
            for u in allusers:
                print("%s,%s,%s,%s,%s,%s" % (u[0],u[1],u[2],u[3],u[4],u[5]))
        #사용자정보조회
        if menu == 's':
            id = input('조회하실 테이블명과 id를 입력해주세요')
            id = id.split(' ')
            oneUser = dbutil.selectOneUser(id)
            print(oneUser)
        #사용자정보삭제
        if menu == 'd':
            id = input('삭제하실 테이블명과 id를 입력해주세요')
            id = id.split(' ')
            dbutil.deleteUser(id)
        if menu == 'u':
            id2 = input('수정하실 테이블명과 id 및 정보를 입력해주세요\n'
                       'tableName,id,pwd,name,phone,addr,age\n'
                         '(띄어쓰기기준)')
            id2 = id2.split(' ')
            userdata = []
            for u in id2:
                userdata.append(u)
            dbutil.updateUser(userdata)
    except:
        print("에러가 발생했습니다...")
    finally:
        dbutil.closeDB()


print('End ....')
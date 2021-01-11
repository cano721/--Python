# ​
#
# < 2조 현관문 도어락 프로그램 >
#
# ​
#
# ​
#
# 1. 프로그램 기획
#
# - 4자리 비밀번호의 현관문 도어락 프로세스 구현.
#
# ​
#
# ​
#
# 2. 시나리오
#
# 1) 도어락을 열기위해 사용자가 숫자 4개 입력,
#
# 2) 미리 정해진 비밀번호 4자리와 일치하면 문이 열린다.
#
# 3) 불일치하면 경고음이 울린다. 재시도 가능.
#
# 4) 시도 가능 횟수 4번 중 모두 불일치 하는 경우, 1분간 재시도 불가.
#
# ​
#
# ​
#
# 3. 프로세스
#
# ​
#
# 0) 도어락 '관리자'가 비밀번호를 설정한다.(입력 받는다.)
#
# ​
#
# 1) 일반 사용자로부터 4자리 숫자를 입력 받도록 대기한다.
#
# ​
#
# 2) 사용자가 숫자 입력한다. 시도한다.
#
# ​
#
# 3) 비밀번호와 사용자 입력 값의 일치 여부 확인
#
# ​
#
# 3-1) 숫자의 값과 순서가 일치 한다면, - 4)로 진행
#
# ​
#
# 3-2) 불일치 한다면, ('비밀번호가 잘못되었습니다.')
#
#       3-2-1) 시도횟수가 3번 이하 일 때, 1)로 돌아간다
#
#       3-2-2) 시도횟수가 4번 이상 일 때,
#
#                재시도가 불가능한 잠금상태가 된다.
#
#                1분 카운트다운이 다되면 1로 돌아간다
#
# ​
#
# 4) 문이 열린다. ('삐리릭~ 문이 열렸습니다.')
#
# ​
#
# 5) 위의 절차를 계속 반복한다.

#------------------------------------------------------
import time

#전역변수
doorLock = []  #도어락 비밀번호
adminId = {'admin':1234} #관리자 아이디와 비밀번호




#비밀번호 설정 함수
def adminLogin():
    global adminId
    global doorLock
    while True:
        id = input("관리자 id를 입력해주세요")
        if id in adminId.keys(): #관리자 id 체크
            pwd = input("비밀번호를 입력해주세요")
            if int(pwd) == adminId[id]: #관리자 비밀번호 체크
                secretNumSetting() #도어락설정
                break
            else:
                print("pwd가 다릅니다.")
        else:
            print("id가 다릅니다.")


#도어락 비번 설정 함수
def secretNumSetting():
    while True:
        try:
            num = input("설정하실 도어락 비밀번호 4자리를 입력해주세요")
            if num.isdecimal() and len(num) == 4: #4자리 및 숫자 체크
                num = int(num)
                doorLock.append(num // 1000)                  #도어락 비번 설정
                doorLock.append((num % 1000) // 100)
                doorLock.append(((num % 1000) % 100) // 10)
                doorLock.append(((num % 1000) % 100) % 10)
                print("설정된 도어락 비밀번호: %s" % doorLock)
                break;
            else:
                print("4자리 숫자로 입력해주십시오")
        except:
            print("잘못 입력하셨습니다.")


#비밀번호와 사용자 입력값 비교 함수
def password():
    cnt =0;
    password = [] #사용자 입력 비밀번호
    while True:
        try:
            pNum = input("비밀번호를 입력해주세요")
            if pNum.isdecimal() and len(pNum) == 4:
                pNum = int(pNum)
                password.append(pNum // 1000)
                password.append((pNum % 1000) // 100)
                password.append(((pNum % 1000) % 100) // 10)
                password.append(((pNum % 1000) % 100) % 10)
                if password == doorLock: #도어락 비밀번호와 사용자 입력값 비교
                    print("뾰로롱~ 문이 열립니다.")
                    break
                else:x
                    cnt +=1; #불일치시 횟수 증가
                    print("비밀번호가 불일치합니다.")
                    password = []
                    if cnt==4: #4회 이상 틀렸을 시
                        cnt=0
                        print("도어락이 비활성화되었음.")
                        print("1분 후 다시 시도해주십시오")
                        for i in range(59,0,-1):
                            time.sleep(1)
                            print("%d초" %i)

            else:
                print("4자리 숫자로 입력해주십시오")
        except:
            print("잘못 입력하셨습니다.")




#구현부
#----------------------------------
while True:
    choice = input("1.비밀번호 설정 2.비밀번호 입력 3.나가기")
    if choice == '1':
        adminLogin()
    elif choice == '2':
        password()
    elif choice == '3':
        exit()
    else:
        print("잘못 입력하셨습니다.")



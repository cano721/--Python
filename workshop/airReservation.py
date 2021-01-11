# 항공예매 시스템

#-----------------------------------------------------------------------------------------
from datetime import datetime
import time

#항공편리스트 DB(고정)
#(추후 관리자로 들어갈 시 DB추가기능도 구현하면 좋을 것 같음.)
# 항공편, 날짜 및 시간, 출발지(서울), 도착지(제주),좌석종류(Economy,Business,First)
airPlaneDb = [['KE1234','2021-01-11 13:00','서울','제주','Economy'],
           ['KE1235','2021-01-13 15:00','서울','제주','Economy'],
           ['KE1245','2021-01-15 09:00','서울','제주','Business'],
           ['KE1876','2021-01-18 18:00','서울','제주','Economy'],
           ['KF1835','2021-01-19 14:00','서울','제주','First'],
           ['KG8205','2021-01-19 16:00','서울','제주','First'],
           ['KH5132','2021-01-22 22:00','서울','제주','Economy'],
           ['KQ1513','2021-01-23 11:00','서울','제주','Business'],
           ['KZ5132','2021-01-24 15:00','서울','제주','Economy'],
           ['KH1521','2021-01-25 19:00','서울','제주','Business'],
           ['KT1523','2021-01-26 21:00','서울','제주','First']]


#전역변수 목록
airPlaneRe = [] #현금결제 예약 리스트
airPPlaneRe =[] #포인트결제 예약 리스트
economy = 50_000 #이코노미석 가격
business = 100_000 #비즈니스석 가격
first = 200_000 #퍼스트석 가격
pointMoney = 50_000 #포인트
money = 5_000_000 #현금

#항공권 예약 함수
def re():
    #전역변수를 사용 및 수정하기 위한 global 지정
    global pointMoney
    global airPlaneRe
    global airPPlaneRe
    global money
    print("----------------")
    print("항공편 예약")
    # 현재 DB에 담긴 내용을 번호를 붙여서 출력
    for i in enumerate(airPlaneDb,1):
        print(i)
    print("----------------")
    #현재 시각 출력
    print("현재시각:",end="")
    print(datetime.now())
    # 앞에 출력된 번호에서 예약하기 원하는 번호값을 reNum에 저장(실제 사용시엔 str로 저장됨으로 int형 치환)
    reNum =input("어떤 항공편을 예약하시겠습니까? (번호를 입력해주십시오)")
    # 좌석에따른 가격이 다름으로 선택한 항공편리스트에 'Economy' 확인
    if 'Economy' in airPlaneDb[int(reNum)-1]:
        print("결제금액은 %d원입니다." % economy)
        #포인트,현금 부족시나 잘못 입력시 반복
        while True:
            pNum  = input("포인트로 결제(1)\n 현금 결제(2)")
            #포인터 결제 시
            if pNum =='1':
                #포인트금액이 이코노미석가격보다 같거나 많으면
               if pointMoney >= economy:
                  pointMoney -= economy #포인트금액 가격만큼 차감
                  print("예약완료 %s" % airPlaneDb[int(reNum)-1]) #선택한 항공편 예약완료 출력
                  airPPlaneRe.append(airPlaneDb[int(reNum)-1]) #선택한 항공편 포인트예약리스트에 추가
                  airPlaneDb.pop(int(reNum)-1) #선택한 항공편 항공편DB에서 삭제
                  print("남은포인트: %d" % pointMoney) #남은 포인트 출력
                  break;
                #포인트금액이 이코노미가격보다 적으면
               else:
                   print("포인트가 부족합니다.")
                   continue
            #현금 결제 시
            elif pNum =='2':
                #현금이 이코노미석가격보다 같거나 많으면
                if money >= economy:
                   print("예약완료 %s" % airPlaneDb[int(reNum) - 1]) #선택한 항공편 예약완료 출력
                   airPlaneRe.append(airPlaneDb[int(reNum)-1]) #선택한 항공편 포인트예약리스트에 추가
                   airPlaneDb.pop(int(reNum) - 1) #선택한 항공편 항공편DB에서 삭제
                   pointMoney += economy*0.1 #포인트적립
                   money -= economy #현금에서 좌석값 차감
                   print("잔액: %d" %money) #현금잔액 출력
                   break;
                #현금 부족시
                else:
                    print("금액이 부족합니다.")
                    continue
            #포인트결제(1), 현금결제(2) 제외 키 누를시
            else:
                error()
                continue
    # 선택한 항공편리스트에 'Business' 확인
    elif 'Business' in airPlaneDb[int(reNum)-1]:
        print("결제금액은 %d원입니다." % business)
        while True:
            pNum  = input("포인트로 결제(1)\n 현금 결제(2)")
            if pNum =='1':
               if pointMoney >= business:
                  pointMoney -= business
                  print("예약완료 %s" % airPlaneDb[int(reNum)-1])
                  airPPlaneRe.append(airPlaneDb[int(reNum)-1])
                  airPlaneDb.pop(int(reNum)-1)
                  print("남은포인트: %d" % pointMoney)
                  break;
               else:
                   print("포인트가 부족합니다.")
                   continue
            elif pNum == '2':
                if money >= business:
                   print("예약완료 %s" % airPlaneDb[int(reNum) - 1])
                   airPlaneRe.append(airPlaneDb[int(reNum) - 1])
                   airPlaneDb.pop(int(reNum) - 1)
                   pointMoney += business * 0.1
                   money -= business
                   print("잔액: %d" % money)
                   break;
                else:
                   print("금액이 부족합니다.")
                   continue
            else:
                error()
                continue
    # 선택한 항공편리스트에 'First' 확인
    elif 'First' in airPlaneDb[int(reNum)-1]:
        print("결제금액은 %d원입니다." % first)
        while True:
            pNum  = input("포인트로 결제(1)\n 현금 결제(2)")
            if pNum =='1':
               if pointMoney >= first:
                  pointMoney -= first
                  print("예약완료 %s" % airPlaneDb[int(reNum)-1])
                  airPPlaneRe.append(airPlaneDb[int(reNum)-1])
                  airPlaneDb.pop(int(reNum)-1)
                  print("남은포인트: %d" % pointMoney)
                  break;
               else:
                   print("포인트가 부족합니다.")
                   continue
            elif pNum =='2':
               if money >= first:
                  print("예약완료 %s" % airPlaneDb[int(reNum) - 1])
                  airPlaneRe.append(airPlaneDb[int(reNum)-1])
                  airPlaneDb.pop(int(reNum) - 1)
                  pointMoney += first * 0.1
                  money -= first
                  print("잔액: %d" % money)
                  break;
               else:
                  print("금액이 부족합니다.")
                  continue
            else:
                error()
                continue
    #3개의 좌석이 다 없을 경우
    else:
        error()

#항공권 예약확인 함수
def reCheck():
    print("----------------")
    print("예약된 항공편")
    #포인트예약리스트와 현금예약리스트 합치기
    reCheckre = airPPlaneRe + airPlaneRe
    #합친 리스트 날짜 및 시간순대로 정리
    reCheckre.sort(key=lambda x:x[1])
    #정리된 리스트 번호 붙여서 출력
    for i in enumerate(reCheckre,1):
        print(i)
    print("----------------")

#포인트 잔액 확인 함수
def pCheck():
    """포인트 확인 함수"""
    print("----------------")
    print("포인트 잔액: %d" %pointMoney)
    print("----------------")

#항공권 예약 취소 함수
def reCancel():
    """항공 예약취소 함수"""
    print("----------------")
    print("예약된 항공편")
    global pointMoney
    global money
    #예약된 항공권이 없을 경우를 대비한 cnt
    cnt =0
    # 포인트예약리스트와 현금예약리스트 합치기
    reCheckre = airPPlaneRe + airPlaneRe
    # 합친 리스트 날짜 및 시간순대로 정리
    reCheckre.sort(key=lambda x: x[1])
    # 정리된 리스트 번호 붙여서 출력
    for i in enumerate(reCheckre, 1):
        #예약된 건당 cnt 1씩 증가
        cnt +=1
        print(i)
    print("----------------")
    #예약한 항공편이 없을 경우 아래 내용 출력
    if cnt == 0:
        print("예약된 항공편이 없습니다.")
    #예약한 항공편이 있을 경우
    else:
        #취소할 항공편 선택
        cNum = input("취소할 항공편을 선택해주세요")
        #예약되어있는 항공편리스트 내 선택했을 경우
        if int(cNum)<=cnt:
            # 선택한 항공편이 현금예약리스트에 있을 시
            if reCheckre[int(cNum) - 1] in airPlaneRe:
                #선택한 항공편이 현금예약리스트의 몇번째 있는지 확인
                rtNum = airPlaneRe.index(reCheckre[int(cNum) - 1])
                #Economy일시 포인트 차감 및 현금 환불
                if 'Economy' in airPlaneRe[rtNum]:
                    pointMoney -= economy*0.1
                    money += economy
                # Business일시 포인트 차감 및 현금 환불
                elif 'Business' in airPlaneRe[rtNum]:
                    pointMoney -= business*0.1
                    money += business
                # First일시 포인트 차감 및 현금 환불
                elif 'First' in airPlaneRe[rtNum]:
                    pointMoney -= first*0.1
                    money += first
                #선택한 항공편 현금예약리스트에서 삭제
                airPlaneRe.pop(rtNum)
            # 선택한 항공편이 포인트예약리스트에 있을 시
            elif reCheckre[int(cNum) - 1] in airPPlaneRe:
                rtNum = airPPlaneRe.index(reCheckre[int(cNum) - 1])
                if 'Economy' in airPPlaneRe[rtNum]:
                    pointMoney += economy
                elif 'Business' in airPPlaneRe[rtNum]:
                    pointMoney += business
                elif 'First' in airPPlaneRe[rtNum]:
                    pointMoney += first
                airPPlaneRe.pop(rtNum)
            #예약되어있는 항공편리스트 내 선택했을 경우 공통 진행되야할 사항
            airPlaneDb.append(reCheckre[int(cNum) - 1])
            airPlaneDb.sort(key=lambda x: x[1])
            print("취소완료 %s" % reCheckre[int(cNum) - 1])
            print("현재잔액: %d" %money)
        # 예약되어있는 항공편리스트를 넘는 숫자를 입력했거나 다른 키 입력 시
        else:
            error()

# 잘못 입력했을 시 출력 함수
def error():
    print("잘못 입력하셨습니다.")

#---------------------------------------------------------------------



#구현부
while True:
    print("★★★★★★★★★★★★★항공편 예약시스템★★★★★★★★★★★★★")
    time.sleep(1)
    choice = input("①항공권 예약 ②항공권 예약확인 ③포인트 확인 ④예약 취소 ⑤나가기")
    if choice == '1':
        re()
    elif choice == '2':
        reCheck()
    elif choice == '3':
        pCheck()
    elif choice == '4':
        reCancel()
    elif choice == '5':
        exit()
    else:
        error()
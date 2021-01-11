# <카드 전용 자판기>
#
# ​
#
# 1. 프로그램 기획
#
# -> 카드 전용 자판기 구현
#
#
# 2. 시나리오
#
# 1) 카드 투입, 잔액 입력
#
# 2) 메뉴 선택. 메뉴가 품절일 경우 품절 안내 문구 출력
#
# 3) 잔액이 모자를 경우 메뉴 선택 단계로 다시 이동
#
# 4) 잔액이 충족되면 물건 제공
#
#
#
# 3. 프로세스
#
# 0. 카드에 충전할 금액 입력 input -> int(정상 카드) / char(이상한 카드)
#
#
# 1. 카드 투입 시 -> 이상한거, 잘못 넣은 카드는 반환
#
# 2. 메뉴: 과자5개, 수량 랜덤(0~5개), 가격(랜덤 1~50하고 *100 아래 단위 없애기)
#
# 메뉴 = dict, 하위에 이름, 수량, 가격
#
#
# 3. 매진 메뉴 선택 시 예외처리(다른 것 선택하라는 문구 뜨게)
#
# 메뉴.수량 ==0 ~~
#
#
# 4. 카드 잔액과 메뉴 가격 비교: 적으면 [잔액부족] 문장 출력+ 메뉴 선택 단계로. 아니면 물건 제공
#
# 메뉴.가격 <, > 비교해서


#--------------------------------------
import random
import time


#전역변수
card = 0; #카드 충전금액이 담겨 있음
menu = {} #메뉴 딕셔너리형태 {과자이름:[수량(랜덤),가격(랜덤)]}
menuChoice = ''; #선택된 과자

#메뉴 생성 함수
#메뉴이름:c 가격:price 수량:piece
def cMenu(c):
    menuPiece = random.randint(0,5) #과자수량에 랜덤숫자 대입
    menuPrice = (random.randint(1,50)*100) #과자가격에 랜덤숫자 대입
    menu[c] = [menuPiece,menuPrice] #매개변수에 입력한 과자이름키값에 리스트[과자수량,과자가격] 대입
                                    #{c:[랜덤과자수량,랜덤과자가격]}


# 카드 충전 및 카드확인 함수
# 정상카드(숫자),이상한카드(한글 및 영어),잘못된 카드(그외 예시.특수문자)
def cardCharge():
    #전역변수 사용
    global card
    while True:
        charge = input("카드에 충전할 금액을 입력하시오") #카드에 충전할 금액 입력
        print("카드가 투입중...")
        for i in range(3): #0.5초 간격으로 프린트 3번
            print("....")
            time.sleep(0.5)
        if charge.isdecimal(): #충전 금액이 숫자일시
            card = int(charge) #카드에 입력한 금액 대입
            print("충전완료 카드잔액:%d" % card)
            break
        elif charge.isalpha(): #한글 또는 영어 입력 시
            print("이상한 카드를 넣으셨습니다.")
        else: #그 외 입력시 (특수문자)
            print("잘못된 카드를 넣으셨습니다.")

#과자 선택 및 수량 확인
def pieceCheck():
    #전역변수 사용
    global menuChoice
    while True:
        for i in menu.keys(): #과자이름 출력
            print(i)
        try:
            menuChoice = input("과자를 선택해주세요(이름 입력)") #선택과자 입력
            if menu.get(menuChoice)[0] == 0: #선택과자가 수량이 0일시
                print("선택하신 과자는 품절입니다.. 다른것을 선택해주세요")
                continue
            elif menu.get(menuChoice)[0] > 0: #선택과자가 수량이 있을시
                break
        # 예외처리 과자이름이 아닌 별도의 것을 입력했을때
        except:
            print("잘못입력하셨습니다.")
            print("-------------")
            continue




#카드 잔액과 메뉴가격 비교
def priceCheck():
    #전역변수 사용
    global card
    if card >= menu.get(menuChoice)[1]: #카드 잔액이 선택과자가격보다 많거나 같을 시
        for i in range(3):
            print("....")
            time.sleep(0.5)
        print("계산되었습니다.")
        card -= menu.get(menuChoice)[1] # 카드 잔액에서 과자가격 차감
        menu.get(menuChoice)[0] -= 1
        print("카드 잔액: %d" %card)
        return False #반복문 탈출하기 위해
    else:                               # 카드 잔액이 적을 시
        print("카드 잔액이 부족합니다...")
        return True #반복문 돌리기 위해

#구현부
#------------------------------------------

#과자 db 생성
cMenu('꼬북칩 시나몬맛')
cMenu('빼빼로')
cMenu('포테이토칩')
cMenu('로투스')
cMenu('닭다리')
print("카드전용 과자 자판기")
# 카드 충전 및 카드확인 함수
cardCharge()

while True:
    sNum = input("1.자판기 이용 2.나가기") #자판기이용 또는 사용안함
    if sNum == '1':
        pieceCheck() #과자 선택 및 수량확인
        while priceCheck(): #카드 잔액 부족 시 과자선택 및 수량확인 반복
            pieceCheck()
            priceCheck() #카드 잔액 충분할 시 False값을 되돌려받아 반복문 탈출
    elif sNum == '2':
        exit() #자판기 사용안할 시 프로그램 종료
    else:
        print("잘못 입력하셨습니다.")




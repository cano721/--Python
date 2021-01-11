''' 코인토스

동전 던지기 게임으로 매 게임 시작전 베팅머니를 입력 받는다

동전의 앞뒷면에 배팅을 걸고, random 함수에 따라 승패가 정해진다.

매번마다 앞뒤를 선택할 수 있고, 승리시 배팅액의 2배씩 곱해서 얻을 자격이 주어진다.

이후 go stop을 선택할 수 있는데 stop을 선택할 경우 그때까지의 상금을 얻어간다.

'''

import random

#NumberGuess
#---------------------------------------
import random
money = {}

#전역변수
ctDealerAnswer= {} #유저별 딜러정답
ctAllPrizeMoney = {} #유저별 매판 상금
ctNum = 2 #상금을 정하기 위한 숫자
ctUserCoin ={} #유저별 추측숫자
gameEnd = {}


#사용자별 딜러의 숫자설정 함수
def dealerNum(userID): #input으로 입력받은 userID로 적용시키기위해
    answerNum = random.randint(1,2) #1을 앞,2를 뒤로 설정
    if answerNum==1:
        ctDealerAnswer[userID] = '앞'
    else:
        ctDealerAnswer[userID] = '뒤'#결정된 정답값을 유저에맞는 딜러 정답값으로 추가
    print(ctDealerAnswer[userID])

#사용자 배팅금액에 따른 상금 설정
def batingAmount(userID):
    global prize #전역변수 사용
    while True:
        try:
            bating = int(input("배팅금액: ")) #배팅금액 설정
            if bating <= money[userID]: #보유한 머니가 배팅금액보다 많으면 배팅성공
                money[userID] -= bating #배팅금액 머니에서 감소
                ctAllPrizeMoney[userID] = bating*ctNum #상금 설정
                break #제대로된 배팅금액 입력시 탈출
            else: #보유한 머니가 배팅금액보다 적으면 배팅 다시..
                print("머니가 부족합니다.")
        except: #숫자값이 아닌 다른걸 입력시.. 출력 및 반복
            error()


#플레이어 정답와 딜러 정답 비교
def comparison(userID):
    while True:
        try:
            ctUserCoin[userID] = input("동전 앞,뒤를 선택해주세요(앞,뒤)") #추측정답 입력
            if ctUserCoin[userID] == '앞':
                if ctUserCoin[userID] == ctDealerAnswer[userID]:
                    print("정답입니다!")
                else:
                    print("틀렸습니다...")
                    ctAllPrizeMoney[userID] = 0 #틀렸을시 상금 0
                break
            elif ctUserCoin[userID] == '뒤':
                if ctUserCoin[userID] == ctDealerAnswer[userID]:
                    print("정답입니다!")
                else:
                    print("틀렸습니다...")
                    ctAllPrizeMoney[userID] = 0
                break
            else:
                print("앞,뒤 중 입력해주세요")
        except:
            error()

#정답 확인 함수(상금)
def goStop(userID):
    if ctAllPrizeMoney[userID] >0:
        while True:
            gs = input("계속 진행하시려면 'go' 아니면 'stop'을 입력해주십시오")
            gameEnd[userID] = gs.lower()
            if gameEnd[userID] == 'go': #게임 계속 진행
                ctAllPrizeMoney[userID] *= 2 #상금 2배로 증가
                return True
            elif gameEnd[userID] == 'stop':
                money[userID] += ctAllPrizeMoney[userID] #종료시 상금을 머니에 입력
                print("상금: %d" %ctAllPrizeMoney[userID])
                print("보유머니: %d" % money[userID])
                return False
            else:
                print("잘못입력하셨습니다.")
    else:
        print("다음에 재도전해주세요~")
        return False

def error():
    print("잘못 입력하셨습니다")
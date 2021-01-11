# Number Guess
# 게임 설명 : 누구나 한 번은 해본 술게임: 간단하게 설명하면 소주병뚜껑에 있는 숫자 맞추기 게임입니다.
# 게임 방법 :
# 무작위 숫자 하나가 선정된다.(1~99)
# 사용자가 1~99 사이의 숫자를 입력한다.
# 틀릴 때에는 사용자가 입력한 숫자가 선정된 숫자보다 작으면 "UP"이라는 메시지를 통해 숫자를 키우라고 말하고, 숫자가 크면 "DOWN"이라는 메시지를 통해 숫자를 줄이라고 말한다.
# 한 번 틀릴 때마다 500만원씩 차감되며, 맞추게 되면 1000만원을 획득한다.
# 수정 사항 :
# 아직 함수가 어려워서 몇 가지 사항이 적용이 안된 것 같다.
# 글자를 입력했을 때 처리하는 방법을 잘 모르겠다.

#시나리오
#1.무작위 숫자 하나 선정
#2. 사용자 숫자입력
#3. 숫자와 비교

#NumberGuess
#---------------------------------------
import random
money = {}

#전역변수
ngDealerAnswer= {} #유저별 딜러정답
ngAllPrizeMoney = {} #유저별 상금
ngNum = 3 #상금을 정하기 위한 숫자
ngUserAnswer ={} #유저별 추측숫자
prize = {} #일정한 상금 감소를 위한 변수


#사용자별 딜러의 숫자설정 함수
def dealerNum(userID): #input으로 입력받은 userID로 적용시키기위해
    answerNum = random.randint(1, 99) #1~99까지 랜덤숫자
    ngDealerAnswer[userID] = answerNum #결정된 정답값을 유저에맞는 딜러 정답값으로 추가


#사용자 배팅금액에 따른 상금 설정
def batingAmount(userID):
    global prize #전역변수 사용
    while True:
        try:
            bating = int(input("배팅금액: ")) #배팅금액 설정
            if bating <= money[userID]: #보유한 머니가 배팅금액보다 많으면 배팅성공
                money[userID] -= bating #배팅금액 머니에서 감소
                ngAllPrizeMoney[userID] = bating*ngNum #상금 설정
                prize[userID] = ngAllPrizeMoney[userID]  # 상금감소를 일정하게하기위해 넣음
                break #제대로된 배팅금액 입력시 탈출
            else: #보유한 머니가 배팅금액보다 적으면 배팅 다시..
                print("머니가 부족합니다.")
        except: #숫자값이 아닌 다른걸 입력시.. 출력 및 반복
            error()


#플레이어 숫자와 딜러 숫자 비교
def comparison(userID):
    while True:
        try:
            num = int(input("숫자를 입력해주세요(1~99)")) #추측숫자 입력
            if num>0 and num<100: #1~99까지 숫자만 입력
                if num >ngDealerAnswer[userID]: #정답이 추측숫자보다 적을때
                    print("DOWN")
                elif num < ngDealerAnswer[userID]: #정답이 추측숫자보다 클때
                    print("UP")
                ngUserAnswer[userID] = num #유저 추측숫자에 입력값 넣기
                break
            else:
                print("1~99까지의 숫자를 입력해주세요")
        except:
            error()

#정답 확인 함수(상금)
def answerCheck(userID):
    if ngAllPrizeMoney[userID] >= 0: #상금이 아직 남아있을 경우
        if ngUserAnswer[userID] == ngDealerAnswer[userID]: #유저 추측숫자와 정답 일치
            money[userID] += ngAllPrizeMoney[userID] #유저머니에 상금을 추가
            print("축하드립니다~ 정답입니다!")
            print("상금: %d" % ngAllPrizeMoney[userID])
            print("현재 보유 머니: %d" % money[userID])
            return False #게임 종료하기위한 리턴값
        else: #정답 미일치 시 상금 감소
            ngAllPrizeMoney[userID] -= prize[userID] * (1 / (ngNum +12))
            return True #계속 비교하기위한 리턴값
    else: #상금이 바닥난 경우...
        print("기회가 다 소진되었습니다...")
        print("정답은 %s였습니다.." % ngDealerAnswer[userID])
        print("다음번에 또 이용해주세요~")
        print("현재 보유 머니: %d" % money[userID])
        return False #게임 종료하기위한 리턴값

def error():
    print("잘못 입력하셨습니다")
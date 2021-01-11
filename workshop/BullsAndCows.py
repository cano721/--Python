# Bulls and Cows
# * 개발자 : 경주
# 게임 설명 : 흔히 숫자야구라고 불리며 dealer가 random하게 제시한 4개의 숫자를 player가 맞추는 게임이다.
#
# 게임 방식 :
#
# dealer는 중복되지 않는 0~9의 숫자 4개를 고르고 임의로 배열한다.
#
# player에게 1억의 돈이 주어지고 게임이 시작된다.
#
# 게임은 player가 dealer의 숫자를 맞출 때까지 진행된다.
#
# player가 dealer의 숫자를 추측하는 행위를 한 턴이라고 할 때
#
# player는 한 턴당 1천만원을 잃게 된다.
#
# 매 턴, player는 4자리 숫자를 추측한다.
#
# player가 추측한 4자리 숫자와 dealer가 정한 4자리 숫자를 비교한다
#
# 자리와 숫자가 일치할 경우 strike이다.
# 자리는 틀렸지만 player가 추측한 숫자가 dealer가 정한 숫자 중에 있을 경우 ball이다.
# 4 strike일 경우 게임이 끝나고 상금을 타게 된다.


#시나리오
#1. 딜러의 숫자 3개 생성
#2. 플레이어의 배팅(배팅금액의 2배가 스타트 상금이라 가정시 1회 틀릴시 1/10씩 감소 5회에 맞출시 본전)
#3. 플레이어 추측 숫자와 딜러 숫자 비교(반복문을 통한 비교 반복)


#Bulls and Cows(숫자야구)
#---------------------------------------
import random
money = {}
#전역변수
bullAllDealerNum = {} #숫자야구 유저별 정답
bullAllPrizeMoney = {} #숫자야구 유저별 상금설정
bullAnswerNum = 4 #몇자리 숫자로 게임을 할건지 선택 (3자리,4자리 등)
bullUserAnswer ={} #스트라이크 볼 체크를 위한 딕셔너리
prize = {} #틀릴때마다 일정하게 상금을 감소시키기 위한 변수


#사용자별 딜러의 숫자설정 함수
def dealerNum(userID): #input으로 입력받은 userID로 적용시키기위해
    dealer_num = [] #정답값 리스트
    while len(dealer_num)!=bullAnswerNum: #몇자리 숫자게임(bullAnswerNum)에 맞는 정답값 뽑기
        d = random.randint(0, 9) #0~9까지 랜덤숫자
        if d in dealer_num: #중복값 제거를 위한 if문
            pass
        else:
            dealer_num.append(d) #중복값 없을 시 정답값 리스트에 추가
    bullAllDealerNum[userID] =dealer_num #결정된 정답값 리스트를 유저에맞는 딜러 정답값으로 추가

#사용자 배팅금액에 따른 상금 설정
def batingAmount(userID):
    global prize #전역변수 사용
    while True:
        try:
            bating = int(input("배팅금액: ")) #배팅금액 설정
            if bating <= money[userID]: #보유한 머니가 배팅금액보다 많으면 배팅성공
                money[userID] -= bating
                prizeMoney = bating*bullAnswerNum # 정답자리수에따른 상금 증가
                bullAllPrizeMoney[userID] = prizeMoney
                prize[userID] = bullAllPrizeMoney[userID]  # 상금감소를 일정하게하기위해 넣음
                break #제대로된 배팅금액 입력시 탈출
            else: #보유한 머니가 배팅금액보다 적으면 배팅 다시..
                print("머니가 부족합니다.")
        except: #숫자값이 아닌 다른걸 입력시.. 출력 및 반복
            error()


#플레이어 숫자와 딜러 숫자 비교
def comparison(userID):
    try:
        while True: #추측숫자 중복값 예외처리를 해야하는데 ㅠㅠ 못하겠네요
            num = input("4자리 숫자를 입력해주세요(0가능)") #추측숫자 입력
            bullNum = [] #플레이어 추측 숫자(리스트)
            bullUserAnswer[userID] = {'strike':0,'ball':0} #스트라이크 볼 초기화
            if num.isdecimal() and len(num) == bullAnswerNum:# 4자리 및 숫자 체크
                num = int(num) #스트링을 정수로 변환
                bullNum.append(num // 1000)  # 플레이어 추측 숫자를 리스트로 넣기 위한 코드
                bullNum.append((num % 1000) // 100)
                bullNum.append(((num % 1000) % 100) // 10)
                bullNum.append(((num % 1000) % 100) % 10)
                for i in range(bullAnswerNum): #딜러 정답값과 유저추측값 비교 코드
                    for j in range(bullAnswerNum):
                        if bullAllDealerNum[userID][i] == bullNum[j]:
                            if i==j: #자리까지 맞을 경우
                                bullUserAnswer[userID]['strike'] +=1
                            else: #숫자만 맞을경우
                                bullUserAnswer[userID]['ball'] +=1
                print("%d strike %d ball" % (bullUserAnswer[userID]['strike'],bullUserAnswer[userID]['ball']))
                break
            else:
                error()
    except:
        error()

#정답 확인 함수(상금)
def answerCheck(userID):
    if bullAllPrizeMoney[userID] > 0: #상금이 아직 남아있을 경우
        if bullUserAnswer[userID]['strike'] == bullAnswerNum: #스트라이크 갯수가 정답갯수와 일치
            money[userID] += bullAllPrizeMoney[userID] #유저머니에 상금을 추가
            print("축하드립니다~ 정답입니다!")
            print("상금: %d" % bullAllPrizeMoney[userID])
            print("현재 보유 머니: %d" % money[userID])
            return False #게임 종료하기위한 리턴값
        else: #스트라이크 갯수가 정답갯수와 미일치 시 상금 감소
            bullAllPrizeMoney[userID] -= prize[userID] * (1 / (bullAnswerNum * 4)) #4자리수12번 본전
            return True #계속 비교하기위한 리턴값
    else: #상금이 바닥난 경우...
        print("기회가 다 소진되었습니다...")
        print("정답은 %s였습니다.." % bullAllDealerNum[userID])
        print("다음번에 또 이용해주세요~")
        print("현재 보유 머니: %d" % money[userID])
        return False #게임 종료하기위한 리턴값


def error():
    print("잘못 입력하셨습니다")

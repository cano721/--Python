##Small Casino Project

# 1. 5가지의 미니게임 존재
# 2. 사용자는 초기에 X원을 갖고 시작
# 3. 게임별로 돈을 벌 수 있고 잃을 수도 있다.
# 4. userMoney를 전역변수로 설정
#   userMoney = 5천만원
# Game을 자유롭게 즐기되 가진 돈이 0원 밑으로 떨어질 경우 추방


# 게임의 종류
# 숫자야구, Number Guess, 잭팟!, 블랙잭, Coin Toss, 보물찾기, 도둑잡기, hang-man,

# Coin Toss : 재영님
# hang-man, 숫자야구, 전체 통합 : 경주
# Number Guess, 잭팟(try) : 상범님
# 블랙잭 : 현수님

#casino
#--------------------------------------------------------------
import BullsAndCows as bac
import NumberGuess as ng
import CoinToss as ct

#전역변수
money = {} #유저별 카지노 머니

#구현부
#------------------------------------------------------------
print("카지노에 오신걸 환영합니다!!!")
userID = input('아이디 입력: ')
try:
    money[userID] = int(input('카지노 머니 환전금액 입력: '))
except:
    bac.error()
while True:
    if money[userID] <= 0:
        print("머니 부족으로 게임을 더이상 진행할 수 없습니다")
        print("안녕히 가세요~")
        exit()
    choice = input("1. Bulls and Cows\n"
                   "2. Number Guess\n"
                   "3. Hangman\n"
                   "4. Coin Toss\n"
                   "5. 나가기")
    if choice == '1':
        bac.money[userID] = money[userID]
        print("Bulls and Cows!!!")
        bac.dealerNum(userID)
        bac.batingAmount(userID)
        bac.comparison(userID)
        while bac.answerCheck(userID):
            bac.comparison(userID)
        money[userID] = bac.money[userID]
    elif choice == '2':
        ng.money[userID] = money[userID]
        print("Number Guess!!!")
        ng.dealerNum(userID)
        ng.batingAmount(userID)
        ng.comparison(userID)
        while ng.answerCheck(userID):
            ng.comparison(userID)
        money[userID] = ng.money[userID]
    elif choice =='3':
        exit()
    elif choice =='4':
        ct.money[userID] = money[userID]
        print("Coin Toss!!!")
        ct.batingAmount(userID)
        ct.dealerNum(userID)
        ct.comparison(userID)
        while ct.goStop(userID):
            ct.dealerNum(userID)
            ct.comparison(userID)
        money[userID] = ct.money[userID]
    elif choice =='5':
        exit()
    else:
        bac.error()
# Lotto Game
# 개인별로 코드 올리기
# 함수를 이용
# 전역변수, 지역변수 활용 잘 해야됨

# 1. 시나리오 만들기
# 전제조건
# 당첨금은 랜덤하게 만든다
# 당첨 번호는 랜덤하게 만든다
# 순위에 따라 당첨금을 차등 지급한다
# 게임을 끝내고 다시 시작할 수 있다

# 로또 번호 6개 + 보너스1개
# 1등 당첨번호 6개 숫자일치
# 2등 당첨번호 5개 숫자일치
# 3등 당첨번호 5개 숫자일치
# 4등 당첨번호 4개 숫자일치
# 5등 당첨번호 3개 숫자일치
import random;

# 당첨 번호(전역변수)
answer = [];
# 상금(전역변수)
money = [];

# 당첨 번호 생성 함수
def makeAnswer(c):
    for i in range(1, 7):
        num = random.randint(1,int(c));
        while num in answer:  # answer가 lotto에 이미 존재하면,(중복되면)
            num = random.randint(1,int(c));  # 숫자 다시뽑자
        answer.append(num);

# 로또번호와 당첨번호 비교 함수
def compareNum(choice):
    answerCnt = 0;
    choice = choice.split(' ');
    print('입력한 로또번호: %s' % (choice));

    for i in range(0,6):
        for j in range(0,6):
            if answer[i] == int(choice[j]):
                answerCnt += 1;
    print('당첨번호: %s' % (answer));
    return answerCnt;

# 당첨금 랜덤생성 함수
def randomMoney():

    money.append(random.randint(1500000000, 2000000000));
    money.append(random.randint(10000000, 50000000));
    money.append(random.randint(1000000, 5000000));
    money.append(50000);
    money.append(5000);
    print("당첨금액 1등:%d원\n 당첨금액 2등:%d원\n 당첨금액 3등:%d원\n 당첨금액 4등:%d원\n 당첨금액 5등:%d원\n"
          % (money[0],money[1],money[2],money[3],money[4]));


# 당첨금 지급함수
def giveMoney(answerCnt):
    if answerCnt == 6:
        print('1등 당첨!  상금: %d원' % (money[0]));
    elif answerCnt == 5:
        print('2등 당첨!  상금: %d원' % (money[1]));
    elif answerCnt == 4:
        print('3등 당첨!  상금: %d원' % (money[2]));
    elif answerCnt == 3:
        print('4등 당첨!  상금: %d원' % (money[3]));
    elif answerCnt == 2:
        print('5등 당첨!  상금: %d원' % (money[4]));
    else:
        print('당첨 되지 않으셨습니다ㅠ');


print('start');

a = input('당첨 번호의 범위를 정하세요: ');
makeAnswer(a);

while True:
    inGame = input('게임 시작(s), 게임 종료(q)');

    if inGame == 'q':
        break;
    elif inGame == 's':
        choice = input("선택하신 번호 6개를 입력해주세요(1~%s)" % a)
        answerCnt = compareNum(choice);
        randomMoney();
        giveMoney(answerCnt);
    else:
        print('잘못 입력하셨습니다, 다시 입력하세요.');

print('end');


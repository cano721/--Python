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
def makeAnswer():
    for i in range(1, 7):
        num = random.randint(1, 20);
        while num in answer:  # answer가 lotto에 이미 존재하면,(중복되면)
            num = random.randint(1, 20);  # 숫자 다시뽑자
        answer.append(num);
    print('당첨번호: %s' % (answer));

# 로또번호와 당첨번호 비교 함수
def compareNum(choice):
    answerCnt = 0;
    choice = choice.split(' ');
    print('입력한 로또번호: %s' % (choice));

    for i in range(0,6):
        for j in range(0,6):
            if answer[i] == int(choice[j]):
                answerCnt += 1;
    return answerCnt;

def randomMoney():

    money.append(random.randint(1500000000, 2000000000));
    money.append(random.randint(10000000, 50000000));


#Number Guess Game
# 1. 두자리의 숫자 2개를 입력 받는다.(ex, 10 90)
# 2. 두 수 사이의 랜덤한 숫자를 발생 시킨다.
# 3. 넘버 게임을 시작 한다.
# 4. 숫자를 입력 받아 2번에서 만들어진 숫자를 기준으로 3가지의 조건을 출력 한다. 크다,작다, 맞다.
# 5. 게임 한 횟수를 화면에 출력 한다.(게임 횟수 제안을 둔다. 횟수는 10회)
# 6. 10회가 넘어가면 fail
# 7. 게임 다시 시작
# 8. 숫자가 맞으면 새로운 게임을 다시 만들어 시작

#한글입력, 두숫자 초과 입력, 스페이스아닌 다른 구분문자 입력시 예외처리...

import random;

while True:
    print('Number Guess Game!!!')

    number = input('Input Number a Number b\n(please put space between the numbers)')
    number = number.split(' ')
    if len(number) == 2:
        i1 = number[0]
        i2 = number[1]
        if i1.isdecimal() and i2.isdecimal():
            i1 = int(i1)
            i2 = int(i2)
            if(i1>9 and i1<100) and (i2>9 and i2<100):
                while True:
                    print('--------New Game--------')
                    answer = random.randint(int(number[0]), int(number[1]))
                    cnt = 0

                    gameexit = input('GameStart = s, exit = q')
                    if gameexit == 'q':
                        exit()
                    elif gameexit =='s':
                        while True:
                            if cnt==10:
                                print("fail...")
                                print("answer is %d" %answer)
                                break

                            choice = int(input('Input answer:'))

                            if choice == answer:
                                print("That's right!")
                                print("You won!")
                                break
                            elif choice > answer:
                                print("The answer is smaller")
                                cnt += 1
                                print("chance: %s"  % (10-cnt))
                            elif choice < answer:
                                print("The answer is bigger")
                                cnt += 1
                                print("chance: %s" % (10 - cnt))
                            else:
                                print("You've entered something wrong.")
                    else:
                        print("You've entered something wrong.")
            else:
                print("Please enter only two digits")
                print("--------------------")

        else:
            print("Please enter only numbers.")
            print("--------------------")
    else:
        print("You've entered something wrong.")
        print("--------------------")








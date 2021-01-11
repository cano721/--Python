import myutil1

d = 10000;
try:
    result = myutil1.input(d)
    print("입력금액은 %d 입니다." % (result))
except:
    print('숫자가 잘못 입력 되었습니다.')

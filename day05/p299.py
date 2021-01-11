import time;

try :
    print('네트워크 접속 시도')
    time.sleep(2);
    print('네트워크 접속 성공')
    time.sleep(2);
    print('네트워크 데이터 전송')
    time.sleep(2);
except:
    print('문제 발생!!')
finally:
    print('네트워크 접속 해지')

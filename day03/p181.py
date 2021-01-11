print('start .....');

while True:
    data = input('input number...?[q:quit]');
    if data.lower() == 'q':
        #.lower() 소문자로 변환
        #.upper() 대문자로 변환
        print('bye..');
        exit();
    if data.isdecimal():
        #data.isdecimal() 숫자냐
        #data.isalnum() 숫자 또는 문자냐
        result = int(data) * 1000;
        print(result);
        break;
    else:
        print('invalid nuber type... try again');


print('end .....');


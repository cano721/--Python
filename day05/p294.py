d = 'a'
result = 0
try:
    num = int(d)
    result = 10 /num;
except ValueError as e:
    # print(e) 에러 설명
    # print(e.with_traceback()) 에러 자세한 설명
    print('Invalid input character ....')
    exit()
except ZeroDivisionError:
    print('zero division error ....')
    exit()

print(result)

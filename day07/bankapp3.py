from bankapi import Account
import bankapi

acc = Account('1111',10000,3.4)
print(acc)
try:
    acc.withdraw(20000)
except bankapi.MinusError:
        print('입력금액이 음수 입니다.')
except bankapi.NotEnoghError:
        print('잔액 부족')

print(acc)

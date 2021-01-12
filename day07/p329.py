# account = ['01088889999',10000,5.8]
# accM = account[1]
# accM += 1000
# account[1] = accM

import math

math.cos()

class Account:
    def __init__(self, accNo, balance,rate):
        self.accNo = accNo
        self.balance = balance
        self.rate = rate

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

    def inquire(self):
        return self.balance

acc1 = Account('1111',20000,4.5)
print('잔액은 %d 입니다.' %(acc1.inquire()))

acc1.deposit(10000)
print('잔액은 %d 입니다.' %(acc1.inquire()))


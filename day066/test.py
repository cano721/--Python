import dbutil

user = input('추가할 사용자의 정보를 입력하세요\n'
                     'id,pwd,name,phone,addr,age\n'
                     '(띄어쓰기기준)')
user = user.split(' ')
userdata = []
for u in user:
    userdata.append(u)
    # if len(userdata) ==6:
    #     break
print(userdata)

def sum(a,b):
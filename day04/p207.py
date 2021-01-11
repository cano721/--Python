#CART 구현

#1. 상품이름,가격 개수
#2. 위의 항목을 입력 받아서 CART에 넣는다.

#Application
#1. menu (i) 카트에 넣기 (v) cart 정보 보기

# print("Cart Application!!")
# menu =input('(i) cart에 넣기 (v) cart 정보 보기')
# print()

import p207_1

print('Cart Application!!')
cart = [];
while True:
    menu =input('cart에 넣기(i) cart 정보 보기(v) 계산하기(c) 프로그램종료(q)')
    if menu =='i':
        # item = input('cart에 넣을 물건을 적어주세요(이름,가격,수량)\n예시) 가위 5000 2')
        # item = item.split(' ')
        cart.append(p207_1.putCart())
    elif menu =='v':
        print("현재 cart에 담겨있는 물건")
        for i in cart:
            print(i)
    elif menu =='c':
        sum =0;
        print("계산할 목록")
        for i in cart:
            print(i)
            sum += int(i[1])*int(i[2])
        print("계산된 총금액: %d" %sum)
        cart= [];

    elif menu =='q':
        print("프로그램을 종료합니다..")
        break
    else:
        print("잘못 입력했습니다.")




print('end')
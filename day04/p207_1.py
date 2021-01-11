def putCart():
    item = input('cart에 넣을 물건을 적어주세요(이름,가격,수량)\n예시) 가위 5000 2')
    item = item.split(' ')
    return item


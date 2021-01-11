def viewCart(c):
    ptotal = 0;
    for item in c:
        print("Item: %s %d %d" % (item[0], int(item[1]), int(item[2])))
        ptotal += int(item[1])*int(item[2]);
    print('total: %d원' % ptotal)

def putCart(c):
    item = input('Input Item(name,price,count)')
    item = item.split(' ')
    c.append(item)

def removeCart(c):
    itemname = input("삭제하고 하는 물건을 입력해주세요")
    for citem in c:
        if itemname in citem:
            c.remove(citem)
            print(citem[0] + "삭제 되었습니다.")
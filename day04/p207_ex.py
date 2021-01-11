import p207_exutil

print('start')
cart = []




while True:
    menu = input('Input menu(i,v,r,q)')
    if menu =='i':
       p207_exutil.putCart(cart)

    elif menu =='v':
        p207_exutil.viewCart(cart)

    elif menu=='r':
        p207_exutil.removeCart(cart)

    if menu =='q':
        print('bye')
        break

print('end')
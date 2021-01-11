import dbutil;

print('start');
while True:
    menu = input('input menu ...[i,s,sa,q]');
    if menu == 'q':
        print('bye');
        break;

    if menu == 'i':
        datas = input('Input information..[id,pwd,name,age]');
        datas = datas.split(' ');
        dbutil.insert(id=datas[0].strip(),
                      pwd=datas[1].strip(),
                        name=datas[2].strip(),
                        age=datas[3].strip());
    if menu == 'sa':
        users = dbutil.selectall(); # list 안에 list
        for user in users:
            print('User Info : %s %s %s %d' % (user[0],user[1],user[2],user[3]));

    if menu == 's':
        id = input('input id ...');
        userData = dbutil.select(id=id);
        print('User Info: %s %s %s %d ' % (user[0],user[1],user[2],user[3]));



print('end');
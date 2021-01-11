
def insert(**a):
    id = a['id'];
    pwd = a['pwd'];
    name = a['name'];
    age = a['age'];
    print('%s %s %s %s inserted .....' %(id,pwd,name,age));

def select(**a):
    id = a['id'];
    data = [];
    data.append(id);
    data.append('pwd01');
    data.append('이말숙');
    return data;

def selectall():
    data = [];
    data.append(['ide01', 'pwd01', '이말숙',25]);
    data.append(['ide02', 'pwd02', '김말숙',26]);
    data.append(['ide03', 'pwd03', '황말숙',27]);
    data.append(['ide04', 'pwd04', '정말숙',28]);
    data.append(['ide05', 'pwd05', '박말숙',29]);
    return data;


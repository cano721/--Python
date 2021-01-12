import sqlite3

con = None
cursor = None

def connectDB(dbName):
    "Connect SQLite..."
    global con,cursor
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    

def makeTable(name):
    "Make users Table"
    cursor.execute("""CREATE TABLE IF NOT EXISTS %s(
        id CHAR(16) PRIMARY KEY,
        pwd CHAR(16),
        name CHAR(10),
        phone CHAR(15),
        addr CHAR(20),
        age NUMBER(6)
         )""" % name)
    con.commit()

def insertUser(user):
    "Insert User Data"
    insertSQL = \
        """INSERT INTO %s VALUES('%s','%s','%s','%s','%s','%s')""" % \
        (user[0],user[1],user[2],user[3],user[4],user[5],user[6])
    cursor.execute(insertSQL)
    con.commit()

def selectUser(table):
    "Select User Data"
    allusers = []
    selectSQL = """SELECT * FROM %s""" % table
    users = cursor.execute(selectSQL)
    for u in users:
        user = []
        user.append(u[0])
        user.append(u[1])
        user.append(u[2])
        user.append(u[3])
        user.append(u[4])
        user.append(u[5])
        allusers.append(user)

    return allusers

def selectOneUser(id):
    "Select One User"
    user = []
    selectOneSQL = """SELECT * FROM %s WHERE id='%s'""" %(id[0],id[1])
    cursor.execute(selectOneSQL)
    userData = cursor.fetchone()
    user.append(userData[0])
    user.append(userData[1])
    user.append(userData[2])
    user.append(userData[3])
    user.append(userData[4])
    user.append(int(userData[5]))
    return user

def deleteUser(id):
    "Delete One User"
    deleteSQL = """DELETE FROM %s WHERE id = '%s'""" % (id[0],id[1])
    cursor.execute(deleteSQL)
    con.commit()

def updateUser(user):
    "Update One User"
    updateSQL = """UPDATE %s SET pwd='%s',name='%s',phone='%s',addr='%s',age=%d WHERE id='%s' """ \
                % (user[0],user[2],user[3],user[4],user[5],user[6],user[1])
    cursor.execute(updateSQL)
    con.commit()

def closeDB():
    "Close SQLite"
    if cursor != None:
        cursor.close()
    if con != None:
        con.close()
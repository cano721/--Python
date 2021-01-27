import sqlite3

class Sql:
    makeUserTb = """CREATE TABLE IF NOT EXISTS usertb(
                    id CHAR(10) PRIMARY KEY,
                    pwd CHAR(10),
                    name CHAR(10),
                    age CHAR(10))"""
    makeItemTb = """CREATE TABLE IF NOT EXISTS itemtb(
                    id CHAR(10) PRIMARY KEY,
                    name CHAR(10),
                    price CHAR(10))
                    """
    insertUser = """INSERT INTO usertb VALUES ('%s','%s','%s','%s')"""
    deleteUser = """DELETE FROM usertb WHERE id = '%s'"""
    selectUser = """SELECT * FROM usertb WHERE id= '%s'"""
    selectAllUser = """SELECT * FROM usertb"""
    updateUser = """update usertb set pwd='%s', name='%s', age=%d where id='%s'"""

    insertItem = """INSERT INTO itemtb VALUES ('%s','%s','%s')"""
    deleteItem = """DELETE FROM itemtb WHERE id = '%s'"""
    selectItem = """SELECT * FROM itemtb WHERE id= '%s'"""
    selectAllItem = """SELECT * FROM itemtb"""
    updateItem = """update itemtb set name='%s', price=%d where id='%s'"""

class SqliteDb:
    def __init__(self,dbName):
        self.__dbName = dbName

    def getConnect(self):
        con = sqlite3.connect(self.__dbName)
        cursor = con.cursor()
        # print(self.__dbName + 'Connected....')
        return {'con':con,'cursor': cursor}

    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close()
        if cc['con'] != None:
            cc['con'].close()

    def makeTable(self):
        "Make usertb Table"
        cc = self.getConnect()
        cc['cursor'].execute(Sql.makeUserTb)
        cc['cursor'].execute(Sql.makeItemTb)
        cc['con'].commit()
        self.close(cc)
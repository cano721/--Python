class Sql:
    insertUser = 'INSERT INTO USERDB'
    selectUser = 'SELECT * FROM USERDB'
    insertItem = 'INSERT INTO ITEMDB'
    selectItem = 'SELECT * FROM ITEMDB'

class UserDb:
    @staticmethod
    def insert():
        print(Sql.insertUser)
    @staticmethod
    def select():
        print(Sql.selectUser)

class ItemDb:
    @staticmethod
    def insert():
        print(Sql.insertItem)
    @staticmethod
    def select():
        print(Sql.selectItem)
    
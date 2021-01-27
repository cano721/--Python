from sqlitedb import *
from value import *

class ItemDb(SqliteDb):
    def insert(self,item):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.insertItem % (item.sqlmap()))
        cc['con'].commit()
        self.close(cc)

    def select(self):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.selectAllItem)
        result = cc['cursor'].fetchall()
        all = []
        for u in result:
            # ('','','',20) 튜플들의 리스트
            tu = Item(u[0], u[1], u[2])
            all.append(tu)
        self.close(cc)
        return all

    def selectone(self, id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.selectItem % (id))
        #('','','',39)
        obj = cc['cursor'].fetchone()
        result = Item(obj[0],obj[1],obj[2])
        self.close(cc)
        return result

    def delete(self,id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.deleteItem % (id))
        cc['con'].commit()
        self.close(cc)

    def update(self,u):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.updateItem % (u.name, u.price, u.id))
        cc['con'].commit()
        self.close(cc)
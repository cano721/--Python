class Human:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def __str__(self):
        return self.__id + ' ' + self.__name + ' ' + str(self.__salary)

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        if salary<= 0:
            return
        self.__salary = salary
    sal = property(getSalary,setSalary)


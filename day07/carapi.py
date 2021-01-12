class Car:
    serial = 1000
    def __init__(self, id, name, fsize, cfsize):
        self.__id = id
        self.__name = name
        self.__fsize = fsize
        self.__cfsize = cfsize
        self.__serial = Car.serial
        Car.serialCount()

    @classmethod
    def serialCount(cls):
        cls.serial +=1

    def print(self):
        return self.__id, self.__name, self.__fsize, self.__cfsize, self.__serial

    def setCfsize(self, size):
        self.__cfsize += size

# 1 Свойства property. Декоратор @property\
# 2 Дескрипторы (data descriptor и non-data descriptor)


# Свойства property. Декоратор @property\
# если в обьекте дублируются имя переменной и имя класса property
# old = 100 и  old = property(get_old,set_old)
# в первую очередь обращение будет к old = property(get_old,set_old)
class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self,old):
        self.__old = old


    old = property(get_old,set_old) # передалли в property ссылку на гетор и сеттор

p = Person()

# a = p.old     a = self,old
# при обращении a = p.old  вызавиться сетор

# p.old = 35    self,old = 35
# при записи вызавиться гетор и полноценно отработает

# p.old2 = 40 в обьекте p появиться локальное свойство p.old2 = 40
# если локальное свойство не заданно ранее то оно создаться
# если созданно то выбирается созданное и отрабатывается по нему

# что бы не дублировать сеторы и геторы и property(get_old,set_old)
# используем декораторы
# old = property(get_old,set_old) не пишем!!!

    # @property # ОБЯЗАТЕЛЬНО ПЕРЕД ГЕТОРОМ
    # def old(self): # имена методов должны совпадать
    #     return self.__old
    #
    # @get_old.setter
    # def old(self,old): # имена методов должны совпадать
    #     self.__old = old
    #
    # @old.deleter # удаляем приватное свойство
    # def old(self):
    #     del self.__old


# теперь для записи и получение информации к __old
# Используем p.old = 100 или a = p.old
# del p.old удалили локальное свойство в экземплере класса



# Дескрипторы (data descriptor и non-data descriptor)
# Делаем класс для того что бы на каждую переменную не писать сетор и гетор с одним и тем же функционалом

#
# non-data descriptor может только считывать
class ReadIntx:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:  #Дискриптор данных
    # ПРИ НЕОБХОДИМОСТИ ПРОВЕРКИ ПЕРЕНОСИМ В ЭТОТ ЖЕ КЛАСС

    # self ссылка на экземпляр класса Integer который находиться  в классе вызываемого обьекта
    # owner ссылка на класс вызываемого обьекта
    # name -  имя к которому присваивается экземпляр класса Integer()
    def __set_name__(self, owner, name):
        #в экземпляре создаем локальное свойство
        #с именем равной строке
        self.name = "_" + name

    # self ссылка на экземпляр класса Integer который находиться  в классе вызываемого обьекта
    # instance ссылка на экземпляр класс создаваемого обьекта
    # owner ссылка на класс вызываемого обьекта

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    # self ссылка на экземпляр класса Integer который находиться  в классе вызываемого обьекта
    # instance ссылка на экземпляр класс создаваемого обьекта
    # value значение которое присваеваеться атрибутам вызываемого экземпляра
    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)

class Point3D:
    # сформировали дискрипторы
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntx() # Дескриптор не данных


    def __init__(self, x, y, z):
        # обращаемся к обьектам класса Integer() (Дискрипторам)
        self.x = x
        self.y = y
        self.z = z
# Магические методы __getitem__, __setitem__ и __delitem__
# переопределяют []
# __getitem__(self, item) - получение значения по ключу item
# если ключа не существует вылитит ошибка нужно проверять на наличие ключа

# __setitem__(self, key, value) - запись значения value по ключу key
# нужно проверять на то что ключ int (если коллекция не словарь)
# и расширять коллекцию на размер ключа


# __delitem__(self,key) - удаление элемента по ключу key


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    #можем обращаться у обьекта класса []
    x = "обьект класса"[2] #на выходе x = self.marks[2]
    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("неверный индекс")

    # key = индекс value = значение    "обьект класса"[3] = "новое значение"
    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым не отрицательным числом")

        # расширяем коллекцию до размера ключа
        if key >= len(self.marks): # проверили нужно ли расширять коллекцию
            off = key + 1 - len(self.marks) # вычислили на сколько нужно расширить коллекцию
            self.marks.extend([None]*off) # расширили коллекцию

        self.marks[key] = value


    def __delitem__(self, key): #  del "обьект класса"[индекс]

        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым не отрицательным числом")

        del self.marks[key]

# РАБОТА СО СРЕЗАМИ
# slice  это класс среза
# class RadiusVector:
    def __init__(self,*args):
        self.coords = list(args)

    def __getitem__(self, item):
        # if type(item) == slice если в item передали срез то ор является обьектом класса slice
        return tuple(self.coords[item]) if type(item) == slice else self.coords[item]

    def __setitem__(self, key, value):
        # если key == срез то по этому срезу передастся value
        self.coords[key] = value

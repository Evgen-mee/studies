# Класс, от которого наследуется класс, называется родительским или базовым классом.
# Класс, который наследуется от родительского (базового) класса, называется дочерним классом или наследником.
# Дочерние классы также называют подклассами, а родительские классы — суперклассами

# синтаксис наследования
# class ParentClass:                         # родительский класс
#     pass
#
# class ChildClass(ParentClass):             # дочерний класс
#     pass


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         return f'{self.name} спит zZ'
#
# class Cat(Animal):                       # т.к. использует метод __init__() класса Animal
#     pass                                 # имеет атрибуты name и age
#
# animal = Animal('Роджер', 2)
# cat = Cat('Кемаль', 1)
# Родитель
# print(animal.name, animal.age)   # Роджер 2
# print(animal.sleep())            # Роджер спит zZ
# Дочерний
# print(cat.name, cat.age)         # Кемаль 1
# print(cat.sleep())               # Кемаль спит zZ

class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = 0 if self.value - n < 0 else self.value - n


class NonDecCounter(Counter):
    def dec(self, n=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.__limit = limit

    def inc(self, n=1):
        if (self.value + n) <= self.__limit:
            self.value += n
        else:
            self.value = self.__limit



counter = LimitedCounter()

print(counter.value)  # 0
counter.inc()
counter.inc(4)
print(counter.value) # 5
counter.dec()        # 4
counter.dec(2)       # 2
print(counter.value) # 2
counter.inc(20)      # 22
print(counter.value)

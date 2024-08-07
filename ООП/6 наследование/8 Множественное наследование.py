# Порядок указания классов в объявлении наследования имеет значение для поиска атрибутов и методов!!!

# Когда класс наследует от нескольких классов, порядок наследования определяет
# приоритетность классов при поиске атрибутов и методов.
# При обращении к атрибуту или методу, Python идет по цепочке наследования, начиная с самого левого класса
# в объявлении наследования.

# class Son(Mother, Father) не то же самое, что class Son(Father, Mother)!!!!

# получаем возможность в дочернем классе пользоваться атрибутами и методами всех указанных
# родительских классов с последующим их переопределением или расширением

# Попытка создать класс, MRO которого невозможно определить, приводит
# к возбуждению исключения TypeError: Cannot create a consistent method resolution

# проблема ромбовидного наследования заключается в неоднозначности,
# которая возникает при определении метода или атрибута, который должен быть унаследован дочерним классом.

# - mro()
# также можно получить с помощью атрибута класса __mro__
# результатом является список родителей класса, включая сам класс,
# расположенных ровно в том порядке, в котором Python будет производить поиск методов
# class A:
#     def method(self):
#         print('Метод класса A')
#
#
# class B(A):
#     def method(self):
#         print('Метод класса B')
#
#
# class C(A):
#     def method(self):
#         print('Метод класса C')
#
#
# class D(B, C):
#     pass
#
#
# print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Поиск родиьеля метода или атрибута
# def get_method_owner(cls, method):
#     for i in cls.mro():
#         if method in i.__dict__:
#             return i

#  - Правило наследования.
# Если некоторый класс D является наследником классов A, B, C, то при построении MRO
# эти классы должны располагаться в том порядке, в котором они были указаны в определении класса D,
# причем между ними могут располагаться другие классы, однако их исходный порядок должен остаться неизменным

#  - Правило старшинства.
# При построении MRO все классы иерархии должны располагаться в порядке старшинства,
# то есть ни один родительский класс не должен следовать перед своим дочерним классом.


class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().rfind(parent)


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(MROHelper.len(D))
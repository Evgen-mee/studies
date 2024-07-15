# если определен, автоматически вызывается после метода __init__().
# Он может быть удобен в случаях, когда мы хотим добавить экземпляру класса атрибут,
# значение которого зависит от значений других атрибутов.

# from dataclasses import dataclass
# @dataclass
# class Person:
#     name: str
#     surname: str
#     age: int
#     fullname: str = None                               #
#
#     def __post_init__(self):
#         self.fullname = self.name + ' ' + self.surname  # полное имя на основе имени и фамилии
#
#
# person = Person('Гвидо', 'ван Россум', 67)
#
# print(person.fullname) #  Гвидо ван Россум


# чтобы значение атрибута, вычисляемого на основе других,
# нельзя было указывать при создании экземпляра класса, мы можем воспользоваться функцией field()
#
# from dataclasses import dataclass, field
# @dataclass
# class Person:
#     name: str
#     surname: str
#     age: int
#     fullname: str = field(init=False)                     # при инициализации данный параметр не ждет присваения
#
#     def __post_init__(self):
#         self.fullname = self.name + ' ' + self.surname     # полное имя на основе имени и фамилии
#
#
# person = Person('Гвидо', 'ван Россум', 67)
#
# print(person.fullname)
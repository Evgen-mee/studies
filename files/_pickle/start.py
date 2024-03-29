# pickle использовать бинарную сериализацию, то есть сериализацию в байты
#
# может сериализовывать:
# все встроенные типы данных (bool, int, float, complex, str, None)
# cписки, кортежи, словари и множества, содержащие любую комбинацию встроенных типов данных
# cписки, кортежи, словари и множества, содержащие любую комбинацию списков, кортежей, словарей и множеств
# функции, классы и экземпляры классов
# может сериализовывать обычные функции (объявленные с помощью  def),
# но не может сериализовывать лямбда-функции (объявленные с помощью lambda)
#
# не может сериализовывать генераторы
#
# pickle и json делают практически одно и то же
# по сути это одна и та же технология, только по-разному реализованная.
#
# pickle зависит от Python и не совместим с другими языками программирования
#
#
#
#
#  - dump()
# принимает сериализуемый Python объект,
#  сериализует его в бинарный,
#  Python-зависимый формат, используя протокол pickle,
#  и сохраняет его в открытый для записи бинарный файл.
#
# import pickle
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# with open('file.pkl', 'wb') as file: # создает файл file.pkl содержащий бинарное представление объекта obj
#     pickle.dump(obj, file)           # сохраняет его в открытый для записи бинарный файл.
#
#
# - load()
# принимает файловый объект,
#  читает из него сериализованные данные,
#  десериализует их в Python-объект
#  и возвращает полученный Python-объект
#
# import pickle
# with open('file.pkl', 'rb') as file:     # отрыли файл
#     obj = pickle.load(file)              # перевели байты в обьект и записали его в переменную
#     print(obj)                           # {'Python': 1991, 'Java': 1995, 'C#': 2002}
#     print(type(obj))                     # <class 'dict'>
#
#
# - dumps()  # возвращает объект типа bytes
# вместо того чтобы сохранять сериализованные данные в открытый бинарный файл,
# она просто возвращает эти сериализованные данные.
# import pickle
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)
# print(binary_obj)          # b'\x80\x03}q\x00(X\x06\x00\x00\x00Pythonq\x01M\xc7\x07X\x04'
# print(type(binary_obj))    # <class 'bytes'>
#
#
# - loads()
# вместо того чтобы принимать файловый объект,
# она принимает объект типа bytes,
# содержащий сериализованные данные
#
# import pickle
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)                   # перевели obj в байтовый формат
# new_obj = pickle.loads(binary_obj)               # перевели binary_obj в обычный формат
# print(new_obj)                                   # {'Python': 1991, 'Java': 1995, 'C#': 2002}
#
# объекты obj и new_obj равны НО НЕ ИНДЕТИЧНЫ!!!!!
# print(obj == new_obj)     # True
# print(obj is new_obj)     # False


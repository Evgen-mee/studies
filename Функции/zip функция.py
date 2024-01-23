# Функция zip
# a = [1,2,3,4]
# b = [5,6,7,8,9,10]
# z = zip(a,b) аргументов может быть больше 4
# z = ((1,5),(2,6),(3,7),(4,8))
# производит обьеденение в кортеж до конца самой короткой колекции

# z = zip(a, b, c)
# lz = list(z)
# t1,t2,t3 = zip(*z)

# Функция zip() удобна для создания словарей, когда ключи и значения находятся в разных списках.
# keys = ['name', 'age', 'gender']
# values = ['Timur', 28, 'male']
# info = dict(zip(keys, values))
# print(info) == {'name': 'Timur', 'age': 28, 'gender': 'male'}
#
#
# Функция zip() удобна для одновременного (параллельного) итерирования сразу по нескольким коллекциям.
# name = ['Timur', 'Ruslan', 'Rustam']
# age = [28, 21, 19]
# for x, y in zip(name, age):
#     print(x, y)


# Мы можем использовать одновременно функции zip() и enumerate()
# list1 = ['a1', 'a2', 'a3']
# list2 = ['b1', 'b2', 'b3']
#
# for index, (item1, item2) in enumerate(zip(list1, list2)):
#     print(index, item1, item2)

#
# x =[input() for _ in range(int(input()))]
# print(x ,sep="\n")
# *(sorted(x,key=lambda x: sum(ord(i.upper())-ord("A") for i in x),reverse=True)
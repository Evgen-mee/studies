#ФУНКЦИИ
#def NAME ():
# Делаем два отступа после тела функции
# Alt + Ctrl + L пайчар редоктирвует код под pip8

# a = foo()
# return (a, b)может возвращать несколько значений через колекции
# x = foo(a,foo(a,b)) в функцию можно передавать аргументом другую функцию

# переопределение функций
'''
if True
def foo (a,b):
print("True")
else:
def foo (a,b):
print("False")
'''
# конфликта имен не будет
# если вызвать без блока то сработает ближайшея функция к вызову print("False")

# get foo(a,b,c)
# Можно так foo(c = 7, a = 9, b = 12)  или   foo(7, с = 9, b = 12)
# так нельзя   foo(a = 3, 9, 12) выдаст ошибку

# Если используем в функции аргумент с с значением по умолчанию
# с ИЗМЕНЯЕМЫМ ТИПОМ ДАННЫХ то обязательно чистим его
# так как в нем будет сохранено значение предыдущего вызова
# ПРИМЕР
# def foo(i, lst=None):  есле передали второй параметр то данные сохраняться в предидущем списке
#     if lst is None:    есле не передали второй параметр то создается новый список
#         lst = []
# l = foo(1)      на выходе l = [1,]
# l = foo(2,l)    на выходе l = [1,2]  при вызове после первой функции

# print(ФУНКЦИЯ.__defaults__) - выведет значение аргументов по умолчанию

# ПЕРЕДАЕМ ФУНКЦИИ ПРОИЗВОЛЬНОЕ ЧИСЛО ЭЛЕМЕНТОВ
# foo(*"Параметр1")  * оператор упаковки элементов
# *"Параметр1" создаст кортеж из введенных значений
# foo(* "строка1","строка2","строка3") в функции будет параметр1 = ("строка1","строка2","строка3")
# foo(*"Параметр1","Параметр2" = 1010)  * оператор упаковки элементов

# ЧТО БЫ ПЕРЕДАТЬ НЕОГРАНИЧЕННОЕ ЧИСЛО ИМЕННОВАННЫХ АРГУМЕНТОВ
# foo(*"Параметр1",**kwargs)
# foo(*"Параметр1","Параметр2" = 1010,"Параметр3" =5050)
# на выходе в функции **kwargs будет словарем
# kwargs = {Параметр2:1010, Параметр3:5050 }

# **kwargs
# Позиционные аргументы можно получать в виде *args
# именованные аргументы получаются в виде словаря
# что позволяет сохранить имена аргументов в ключах.
#
# ПЕРЕДАЧА СЛОВАРЯ В ФУНКЦИЮ
# info = {'name':'Timur', 'age':'28', 'job':'teacher'}
# my_func(**info)


# Операторы *args и **kwargs
# x,y = (1,2) на выходе x = 1 y = 2
# x,*y = (1,2,3,4) на выходе x = 1 y = [2,3,4,]
# работает со всеми итерируемимы обьекты

# a = [1,2,3] (a,) на выходе a = ([1,2,3]) список упакованный в кортеж
# a = [1,2,3] (*a,) на выходе a = (1,2,3) Благодаря * получили распакованный кортеж

# можно распаковывать в range(*a) если а имеет до трех значений start, stop, step

# a = {1:a, 2:b, 3:c}  x = {*a} на выходе получим множество из ключей x = {1,2,3}
# a = {1:a, 2:b, 3:c}  x = {*a.values()} на выходе получим множество из значений x = {a,b,c}
# a = {1:a, 2:b, 3:c}  x = {*a.items()} на выходе получим кортеж из пар x = {(1:a), (2:b), (3:c)}

# a = {1:a, 2:b, 3:c}
# b = {4:d, 5:e, 6:g}
# x = {**a + **b} на выходе получим два обьедененных словаря x = {1:a, 2:b, 3:c, 4:d, 5:e, 6:g }

# Keyword-only аргументы
# нельзя применять в функциях с неограниченным количеством позиционных аргументов *args
# пометить именованные аргументы функции так
# чтобы вызвать функцию можно было
# передав эти аргументы по именам
# их нельзя передать в функцию в виде позиционных.
#
# def make_circle(x, y, radius, *, line_width=1, fill=True): Здесь * выступает разделителем
# отделяет обычные аргументы (их можно указывать по имени и позиционно)
# от строго именованных.
# def make_circle(*, x, y, radius, line_width=1, fill=True):
# для вызова функции нам нужно передать значения всех аргументов явно через их имя


# Записать функцию в словарь
# def start():
#     # тело функции start
#     pass
# def stop():
#     # тело функции stop
#     pass
# def pause():
#     # тело функции pause
#     pass
#
# commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция
# command = input()  # считываем название команды
# commands[command]()  # вызываем нужную функцию через словарь по ключу




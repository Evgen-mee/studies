# принимает в качестве аргумента итерируемый объект, содержащий другие итерируемые объекты и возвращает итератор,
# который генерирует элементы всех вложенных итерируемых объектов.
#
# Аргументы функции:
# iterable — итерируемый объект, содержащий другие итерируемые объекты
#
# from itertools import chain
#
# chain_iter1 = chain.from_iterable(['ABC', 'DEF'])      # передаем список
# print(*chain_iter1)
#
# chain_iter2 = chain.from_iterable(enumerate('ABC'))
# print(*chain_iter2)
#
# for i in chain.from_iterable(['Timur', '29', 'Male', 'Teacher']):
#     print(i, end=' ')
# выводит:
#
# A B C D E F
# 0 A 1 B 2 C
# T i m u r 2 9 M a l e T e a c h e r

def calculate(x, y, operation = 'a'):
    match

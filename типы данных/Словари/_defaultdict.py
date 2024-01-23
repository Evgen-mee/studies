# если мы попытаемся получить доступ по несуществующему ключу,
# то defaultdict автоматически создаст ключ и сгенерирует для него значение по умолчанию
#
# что бы не использовать обычных словарей
#  - метод setdefault()
#  - метод get()
#  - проверка наличия ключа с помощью оператора принадлежности (key in dict)
#
# Когда удобно использовать defaultdict, вместо dict:
# Если ваш код в значительной степени основан на словарях
# и вы все время имеете дело с отсутствующими ключами,
# вам следует подумать об использовании defaultdict, а не обычного dict
#
# Если элементы вашего словаря необходимо инициализировать некоторым значением по умолчанию,
# вам следует подумать об использовании defaultdict, вместо dict
#
# Если ваш код использует словари для агрегирования, накопления, подсчета
# или группировки значений, вам следует подумать об использовании defaultdict, вместо dic

# Мы можем сравнивать обычные словари (тип dict) и defaultdict словари
#
# при создании defaultdict словаря можно указывать не только тип данных для значений по умолчанию,
# но и любую функцию, не принимающую аргументов и возвращающую некоторое дефолтное значение
# from collections import defaultdict
# def get_default():
#     return 69
# info = defaultdict(get_default, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
# print(info['name'])
# print(info['salary'])
# выводит:
# Timur
# 69

#
# Для того чтобы не возникало ошибки при обращении по несуществующему ключу
# с помощью квадратных скобок,
# достаточно использовать альтернативный вариант словаря – defaultdict.
#
# from collections import defaultdict
# info = defaultdict(int)       # создаем словарь со значением по умолчанию 0
# info['name'] = 'Timur'        # ошибка не возникла
# info['age'] = 29              # ошибка не возникла
# info['job'] = 'Teacher'       # ошибка не возникла
# print(info['salary'])
# print(info)
# выводит:
# 0
# defaultdict(<class 'int'>, {'name': 'Timur', 'age': 29, 'job': 'Teacher', 'salary': 0})
#
# - defaultdict()
# принимает в качестве аргумента тип элемента по умолчанию
# для ключей, к которым происходит обращение, словарь defaultdict
# поставит в соответствие дефолтный элемент данного типа
#  - для int – число 0
#  - для float – число 0.0
#  - для bool – значение False
#  - для str – пустая строка ''
#  - для list – пустой список []
#  - для tuple – пустой кортеж ()
#  - для set – пустое множество set()
#  - для dict – пустой словарь {}

# Помимо первого аргумента – типа элемента по умолчанию
# – мы можем передать второй аргумент:
# словарь, на основании которого будет создан defaultdict.
#
# from collections import defaultdict
# info = defaultdict(int, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
# print(info['name'])
# print(info['salary'])
# print(info)
# выводит:
# Timur
# 0
# defaultdict(<class 'int'>, {'name': 'Timur', 'age': 29, 'job': 'Teacher', 'salary': 0})

# при создании словаря defaultdict мы можем указать только именованные аргументы,
# но не можем указать только итерируемый объект с парами ключ-значение (или словарь).
# from collections import defaultdict
# info = defaultdict(name='Timur', age=29, job='Teacher')
# print(info)
# выводит:
# defaultdict(None, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
#
# from collections import defaultdict
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# result = defaultdict(int)
# for num in numbers:
#     result[num] += 1
#
# часто используют в связке с пустым списком в качестве значения по умолчанию,
# чтобы начинать добавление элементов без лишнего кода.
# from collections import defaultdict
# my_dict = defaultdict(list)
# for i in range(7):
#     my_dict[i].append(i)
# for key in my_dict:
#     print(key, my_dict[key])



from collections import defaultdict



# если мы попытаемся получить доступ по несуществующему ключу,
# то defaultdict автоматически создаст ключ и сгенерирует для него значение по умолчанию

# что бы не использовать обычных словарей
#  - метод setdefault()
#  - метод get()
#  - проверка наличия ключа с помощью оператора принадлежности (key in dict)

# можем сравнивать обычные словари (тип dict) и defaultdict словари

# принимает в качестве аргумента тип элемента по умолчанию.
# Таким образом, для ключей, к которым происходит обращение,
# словарь defaultdict поставит в соответствие дефолтный элемент данного типа:
# для int – число 0
# для float – число 0.0
# для bool – значение False
# для str – пустая строка ''
# для list – пустой список []
# для tuple – пустой кортеж ()
# для set – пустое множество set()
# для dict – пустой словарь {}


# можно указывать не только тип данных для значений по умолчанию,
# но и любую функцию, не принимающую аргументов и возвращающую некоторое дефолтное значение
# from collections import defaultdict
# def get_default():
#     return 69
#
# info = defaultdict(get_default, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
# print(info['name'])      # Timur
# print(info['salary'])    # 69
#
# from collections import defaultdict
# info = defaultdict(lambda: '1000000$', {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
# print(info['name'])      # Timur
# print(info['salary'])    # 1000000$


# Функцию, которая возвращает значение по умолчанию
# для отсутствующих ключей, можно явно менять через атрибут
# from collections import defaultdict
# data = defaultdict(int)
# print(data['salary1'])          # 0
# data.default_factory = list
# print(data['salary2'])          # []
# data.default_factory = float
# print(data['salary3'])          # 0.0

# from collections import defaultdict
# info = defaultdict(int)   # создаем словарь со значением по умолчанию 0
# info['name'] = 'Timur'
# info['age'] = 29
# info['job'] = 'Teacher'
# print(info['salary'])     # 0
# print(info)               # defaultdict(<class 'int'>, {'name': 'Timur', 'age': 29, 'job': 'Teacher', 'salary': 0})


# можем передать второй аргумент: словарь, на основании которого будет создан defaultdict
# from collections import defaultdict
# info = defaultdict(int, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
# print(info['name'])      # Timur
# print(info['salary'])    # 0
# print(info)              # defaultdict(<class 'int'>, {'name': 'Timur', 'age': 29, 'job': 'Teacher', 'salary': 0})


# счетчик чисел
# from collections import defaultdict
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# result = defaultdict(int)
# for num in numbers:
#     result[num] += 1


# часто используют в связке с пустым списком в качестве значения по умолчанию,
# чтобы начинать добавление элементов без лишнего кода
# from collections import defaultdict
# my_dict = defaultdict(list)
#
# for i in range(7):
#     my_dict[i].append(i)
#
# for key in my_dict:
#     print(key, my_dict[key])
# выводит:
# 0 [0]
# 1 [1]
# 2 [2]
# 3 [3]
# 4 [4]
# 5 [5]
# 6 [6]



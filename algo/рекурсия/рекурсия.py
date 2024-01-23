# Рекурсивная функция – это функция, которая вызывает саму себя.
#
# В ситуации когда не предусмотрен способ остановки
# рекурсивных вызовов происходит переполнение и возбуждается исключение RecursionError.
#
# Количество раз, которые функция вызывает саму себя, называется глубиной рекурсии.
#
#
# Хвостовой вид рекурсии примечателен тем,
# что может быть легко заменён на итерацию путём корректной перестройки кода функции.
#
# Оптимизация хвостовой рекурсии путём преобразования её в итерацию реализована
# во многих языках программирования. В Python такой оптимизации нет.
#
# Пример функции с хвостовой рекурсией:
# def message(times):
#     if times > 0:
#         print('Это рекурсивная функция')
#         message(times - 1)
#
# Пример функции с рекурсией, которая не является хвостовой:
# def message(times):
#     if times > 0:
#         print('Это рекурсивная функция.')
#         message(times - 1)
#         print(times)
#
#
#
# Чтобы сделать задачу, Надо сделать задачу.
# Не надейся на удачу, Разбивай на подзадачи.
# Разделяй и властвуй, Будет все прекрасно.
# Пусть их будет много, Это вовсе не опасно.
# Крайний случай базовый,
# Он самый простой -- В нем нельзя вызывать самого себя,
# Само собой.
# Но когда о нем забудешь, Стек уходит в глубину.
# Бесконечная рекурсия Тянет ко дну.
# Хирьянов


# обход списка и сумирование int
# my_list = [1, [4, 4], 2, [1, [2, 10]]]
# def recursive_sum(nested_lists):
#     total = 0
#     if not nested_lists:
#         return 0
#     for i in nested_lists:
#         if type(i) == int:
#             total += i
#         if type(i) == list:
#             total += recursive_sum(i)
#     return total
# print(recursive_sum(my_list))


# Линеаризация — это процесс преобразования списка,
# который может содержать несколько уровней вложенных списков,
# в список, содержащий все те же элементы без какой-либо вложенности.
# def linear(nested_lists):
#     new_list = []
#     def rec(nested_list):
#         for i in nested_list:
#             if type(i) == list:
#                 rec(i)
#             else:
#                 new_list.append(i)
#     rec(nested_lists)
#     return new_list
#
# my_list = [3, [4], [5, [6, [7, 8]]]]



# обход вложенного словаря поиск ключа
# def get_value(nested_dicts, key):
#     if key in nested_dicts:
#         return nested_dicts[key]
#
#     for v in nested_dicts.values():
#         if type(v) == dict:
#             value = get_value(v, key)
#             if value is not None:
#                 return value
#
# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993},
#         'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область',
#         'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}
# print(get_value(data, 'cityName'))



# def get_all_values(nested_dicts, key):
#     res = set()
#     def rec(coll):
#         if type(coll) == dict:
#             if key in coll:
#                 res.add(coll[key])
#
#             for v in coll.values():
#                 rec(v)
#     rec(nested_dicts)
#     return res
#
# my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
# result = get_all_values(my_dict, 'top_grade')
#
# print(*sorted(result))



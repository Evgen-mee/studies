# Самое главное в конвейерах генераторов это то, что обработка данных происходит по одному элементу за раз.
# Между этапами обработки в цепочке нет буферизации

# Один элемент проходит цепочку, толькол потом идет следующий.
# нет промежуточного хранения

# n = 10
# integers = (i for i in range(1, n + 1))
# evens = (i for i in integers if not i % 2)
# squared = (i * i for i in evens)
# negated = (-i for i in squared)
# print(*negated)


# def read_immediately(file_name):  # читает все непустые строки файла и заносит их в список
#     with open(file_name, 'r', encoding='utf-8') as file:
#         result = []
#         for line in file:
#             line = line.rstrip('\n')
#             if line != '':
#                 result.append(line)
#         return result
#
# def read_lazy(file_name):  # читает все непустые строки файла и возвращает их с помощью оператора yield
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file:
#             line = line.rstrip('\n')
#             if line != '':
#                 yield line
#
# Результат сравнения работы в том что yield работает в разы быстрее
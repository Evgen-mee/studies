# Блок finally размещается после последнего ехсерt блока, либо после блока else,
# если он присутствует, и содержит программный код, который выполняется в любом случае,
# независимо от того, возникла ошибка (исключение) при выполнении кода trу блока или нет.

# Инструкции внутри блока finally будут выполнены, даже если блок try содержит break, continue, return

# try:
#     # контролируемый код
# except тип_ошибки_1:
#     # код обработки ошибки (исключения)
# except тип_ошибки_2:
#     # код обработки ошибки (исключения)
# ...
# except тип_ошибки_n:
#     # код обработки ошибки (исключения)
# finally:
#     # код, который выполняется всегда


# В функциях блок выполняется до return вне зависимости от его размещения
# def func():
#     try:
#         return 10
#     finally:
#         print('Выполняется блок finally!')
#
# print(func())
# выводит:
# Выполняется блок finally!
# 10

# Если return указан в блоке то вернется значение именно из блока
# def func():
#     try:
#         return 10
#     finally:
#         return 20
#
# print(func())
# выводит:
# 20

# оператор return сохраняет значение возвращаемой переменной!!!!
# def f():
#     try:
#         x = [10]
#         return x             # перед возвратом отработает блок finally только потом отработает return
#     finally:
#         x.append(20)         # добавит в список 20
#
# print(f())    # [10, 20]


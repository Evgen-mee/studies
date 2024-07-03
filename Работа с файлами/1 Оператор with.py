# with open('output.txt', mode='w', encoding='utf-8') as file:
#     file.write('Python generation!')


# Объект, которым управляет оператор with, не обязательно должен создаваться в нем.
# file = open('output.txt', mode='w', encoding='utf-8')
# with file:
#     file.write('Python generation!')


# может управлять сразу несколькими объектами.
# with open('file.txt', encoding='utf-8') as file, open('output.txt', mode='w', encoding='utf-8') as output:
#     for index, line in enumerate(file, 1):
#         output.write(f'{index}. {line}')
#
# можно переписать в виде:
# with (
#     open('file.txt', encoding='utf-8') as file,
#     open('output.txt', mode='w', encoding='utf-8') as output
# ):
#     for index, line in enumerate(file, 1):
#         output.write(f'{index}. {line}')


# работает не со всеми объектами. Для того, чтобы иметь возможность использовать
# некоторый объект в операторе with, этот объект должен удовлетворять протоколу контекстного менеджера!!!!!


# open() возвращает специальный файловый объект (тип TextIOWrapper)


# Атрибут closed экземпляров типа TextIOWrapper позволяет проверить состояние закрытости файла.
# file = open('output.txt', mode='w', encoding='utf-8')
#
# with file:
#     print(file.closed)  # False
#
# print(file.closed)      # True


# С помощью методов readable() и writable() мы можем определить возможность чтения и записи из файла
# with open('output.txt', mode='w', encoding='utf-8') as file:
#     print(file.readable(), file.writable())                  # False True
#
# with open('output.txt', mode='r', encoding='utf-8') as file:
#     print(file.readable(), file.writable())                  # True False


# with вместе с конструкцией try-except-finally при необходимости
# при обработке исключений, связанных с открытием несуществующих файлов
# try:
#     with open('file.txt', encoding='utf-8') as file:
#         print(file.read())                            # если файла file.txt не существует
# except Exception as error:                            #  будет возбуждено исключение
#     print(f'Произошла ошибка {error}')







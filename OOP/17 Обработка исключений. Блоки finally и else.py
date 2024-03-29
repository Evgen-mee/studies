# Обработка исключений. Блоки finally и else

# исключения можно записывать в переменные
# try:
#     x, y = map(int, input().split())
# except ValueError as z: # создали переменную в которой лежит исключение
#     print(z) # вывели исключение
# else: # если все отработало штатно то выдаст сообщение
#     print("Ошибок нет")
# finally: # данный блок выполняется всегда после блока try
#     print("Блок try отработал")


# Распространение исключений (propagation exceptions)
# Обработку исключений можно сделать на любом уровне
# Пример:
# если есть функция в которой происходит ошибка
# мы можем отловить ошибку как в функции
# так и в теле программы выделев в try: саму функцию
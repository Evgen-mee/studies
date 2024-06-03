# Преобразование строки в дату и время
# Есть два пути, чтобы преобразовать введенные данные из строки:
# преобразовать данные самостоятельно
# преобразовывать данные с помощью метода strptime() типа datetime
#
# Самостоятельное преобразование данных
# from datetime import date, time
# day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')
# hour, minute, second = input('Введите время в формате ЧЧ:ММ:СС').split(':')
# my_date = date(int(year), int(month), int(day))        # создаем объект типа date
# my_time = time(int(hour), int(minute), int(second))    # создаем объект типа time
# print(my_date) == 2021-11-13
# print(my_time) == 21:34:59
#
# с исключением
# from datetime import date, time
# while True:
#     try:
#         day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')
#         my_date = date(int(year), int(month), int(day))
#         print('Введена корректная дата:', my_date)
#         break
#     except:      # перехватываем любую ошибку
#         print('Введенная дата не является корректной, попробуйте еще раз')


# Преобразование строки в дату с помощью метода fromisoformat()
# чтобы преобразовать строку из ISO формата в объект даты можно использовать метод fromisoformat()
# НЕ РАБОТАЕТ С datatime ТОЛЬКО DATA и TIME
# from datetime import date, time
# my_date = date.fromisoformat('2020-01-31')
# my_time = time.fromisoformat('10:20:30')
# print(my_date) == 2020-01-31
# print(my_time) == 10:20:30
# print(type(my_date)) == <class 'datetime.date'>
# print(type(my_time)) == <class 'datetime.time'>
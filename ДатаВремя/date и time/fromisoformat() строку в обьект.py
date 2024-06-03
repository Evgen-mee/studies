# работает только с датой и временем, записанными в ISO формате

# лучше использовать strptime() типа datetime

# from datetime import date, time
# my_date = date.fromisoformat('2020-01-31')
# my_time = time.fromisoformat('10:20:30')
# print(my_date)          # 2020-01-31
# print(my_time)          # 10:20:30
# print(type(my_date))    # <class 'datetime.date'>
# print(type(my_time))    # <class 'datetime.time'>
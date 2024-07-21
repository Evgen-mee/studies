# представляет собой временной интервал (разница между двумя объектами datetime или date)
# для различных манипуляций над типами datetime или date.

# все аргументы являются необязательными и по умолчанию равны 0
# недели (weeks)
# дни (days)
# часы (hours)
# минуты (minutes)
# секунды (seconds)
# миллисекунды (milliseconds)
# микросекунды (microseconds)

# можно сравнивать (==, !=, <, >, <=, >=)
# можно (+-/ между обьектами) (*/ обьекта на число)

# Аргументы могут быть целыми числами или числами с плавающей запятой,
# а также могут быть как положительными, так и отрицательными

# from datetime import timedelta
# delta = timedelta(days=7, hours=20, minutes=7, seconds=17)
# print(delta)          # 7 days, 20:07:17
# print(type(delta))    # <class 'datetime.timedelta'>


# ПРИНИМАЕТ ВСЕ ЕДИНИЦЫ ВРЕМЕНИ НО ВОЗРАЩАЕТ ТОЛЬКО days, seconds, microseconds,

# внутренне хранит ТОЛЬКО СОЧЕТАНИЕ days, seconds, microseconds,
# а остальные переданные в конструктор аргументы конвертируются в эти единицы
# - milliseconds преобразуется в 1000 microseconds
# - minutes преобразуется в 60 seconds
# - hours преобразуется в 3600 seconds
# - weeks преобразуется в 7 days

# from datetime import timedelta
# delta1 = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2) # 64 days, 8:05:56.000010
# delta2 = timedelta(weeks=1, hours=23, minutes=61)  # 8 days, 0:01:00
# delta3 = timedelta(hours=25)                       # 1 day, 1:00:00
# delta4 = timedelta(minutes=300)                    # 5:00:00




seconds = 3721
print(f'{seconds // 3600}:{(seconds // 60) % 60}:{seconds // 360}')

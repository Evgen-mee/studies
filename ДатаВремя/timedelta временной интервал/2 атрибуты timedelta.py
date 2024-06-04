# нет атрибутов hours и minutes!!!!
# ПРИНИМАЕТ ВСЕ ЕДИНИЦЫ ВРЕМЕНИ НО ВОЗРАЩАЕТ ТОЛЬКО days, seconds, microseconds,

# Атрибуты
# from datetime import timedelta
# delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
# print('Количество дней =', delta.days)                     # Количество дней = 64
# print('Количество секунд =', delta.seconds)                # Количество секунд = 29156
# print('Количество микросекунд =', delta.microseconds)      # Количество микросекунд = 10
# print('Общее количество секунд =', delta.total_seconds())  # Общее количество секунд = 5558756.00001

# Достать часы и минуты можно так:
# from datetime import timedelta
# def hours_minutes(td):
#     return td.seconds // 3600, (td.seconds // 60) % 60
#
# delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)
# hours, minutes = hours_minutes(delta)
# print(delta)    # 21 days, 8:12:05
# print(hours)    # 8
# print(minutes)  # 12
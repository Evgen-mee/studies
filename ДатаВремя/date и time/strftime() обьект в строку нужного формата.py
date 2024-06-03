# Для форматированного вывода даты и времени используется метод strftime() (для обоих типов date и time).

# По умолчанию вывод даты и времени осуществляется в ISO формате:
# дата имеет вид: YYYY-MM-DD
# время имеет вид: HH:MM:SS или HH:MM:SS.ffffff

# from datetime import date, time
# my_date = date(2021, 8, 10)
# my_time = time(7, 18, 34)
# print(my_date)                             # вывод в ISO формате 2021-08-10
# print(my_time)                             # вывод в ISO формате 07:18:34
# print(my_date.strftime('%d/%m/%y'))        # форматированный вывод даты 10/08/21
# print(my_date.strftime('%A %d, %B %Y'))    # форматированный вывод даты Tuesday 10, August 2021
# print(my_time.strftime('%H.%M.%S'))        # форматированный вывод времени 07.18.34


# from datetime import date, time
# given_time = time(14, 4, 29)
# print(given_time.strftime('Hours: %H, minutes: %M, seconds: %S.'))  # Hours: 14, minutes: 04, seconds: 29.
# print(given_time.strftime('%H:%M:%S'))                              # 14:04:29
# print(given_time.strftime('%I:%M:%S %p'))                           # 02:04:29 PM



import calendar

Атрибут calendar.day_name
возвращает итерируемый объект, содержащий названия дней недели на английском языке.

for name in calendar.day_name:
    print(name)
выводит:
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


Для локализации на русский язык мы используем код:
import calendar, locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
for name in calendar.day_name:
    print(name)
выводит:
понедельник
вторник
среда
четверг
пятница
суббота
воскресенье
а русском языке названия дней недели выводятся с маленькой буквы.
Для того чтобы сделать первую букву заглавной, можно использовать строковый метод title()

Для преобразования итерируемого объекта в список мы используем следующий код:
import calendar
names = list(calendar.day_name)
print(names)
который выводит:
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


Атрибут day_abbr
alendar.day_abbr возвращает итерируемый объект, содержащий сокращенные названия дней недели.

import calendar, locale
for name in calendar.day_abbr:
    print(name)
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
for name in calendar.day_abbr:
    print(name)
выводит:
Mon
Tue
Wed
Thu
Fri
Sat
Sun
Пн
Вт
Ср
Чт
Пт
Сб
Вс


Атрибут month_name
calendar.month_name возвращает итерируемый объект, содержащий названия месяцев года.
month_name соответствует обычному соглашению, что январь – это месяц номер 1, поэтому список имеет длину в 13
элементов, первый из которых – пустая строка.
import calendar, locale
english_names = list(calendar.month_name)
print(english_names)
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
russian_names = list(calendar.month_name)
print(russian_names)
выводит:
['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


Атрибут month_abbr
возвращает итерируемый объект, содержащий сокращенные названия месяцев года.
import calendar, locale
english_names = list(calendar.month_abbr)
print(english_names)
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
russian_names = list(calendar.month_abbr)
print(russian_names)
выводит:
['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
['', 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']


Функция setfirstweekday()
позволяет изменить поведение по умолчанию и устанавливает заданный день недели в качестве начала недели.
Например, чтобы установить первый будний день воскресенье, мы используем код:
import calendar
calendar.setfirstweekday(calendar.SUNDAY)     # эквивалентно calendar.setfirstweekday(6)


Функция isleap()
проверить високосность года
import calendar
print(calendar.isleap(2020))
print(calendar.isleap(2021))
выводит:
True
False


Функция leapdays()
возвращает количество високосных лет в диапазоне от y1 до y2 (исключая), где y1 и y2 – годы
print(calendar.leapdays(2020, 2025))
выводит:
2


Функция weekday()
weekday(year, month, day) возвращает день недели в виде целого числа
ля заданной даты.
import calendar
print(calendar.weekday(2021, 9, 1))     # среда
print(calendar.weekday(2021, 9, 2))     # четверг
выводит:
2
3


Функция monthrange()
monthrange(year, month) возвращает день недели первого дня месяца и количество дней
в месяце в виде кортежа для указанного года year и месяца month
import calendar
print(calendar.monthrange(2022, 1))     # январь 2022 года
print(calendar.monthrange(2021, 9))     # сентябрь 2021 года
выводит:
(5, 31)
(2, 30)


Функция monthcalendar()
monthcalendar(year, month) возвращает матрицу, представляющую календарь на месяц. Каждая строка матрицы представляет неделю.
дни, которые не входят в указанный месяц, представлены нулями. При этом каждая неделя начинается с понедельника,
если не установлено другое функцией setfirstweekday()
import calendar
print(*calendar.monthcalendar(2021, 9), sep='\n')
выводит:
[0, 0, 1, 2, 3, 4, 5]
[6, 7, 8, 9, 10, 11, 12]
[13, 14, 15, 16, 17, 18, 19]
[20, 21, 22, 23, 24, 25, 26]
[27, 28, 29, 30, 0, 0, 0]


Функция month()
month(year, month, w=0, l=0) возвращает календарь на месяц в многострочной строке.
Аргументами функции являются: year (год), month (месяц),
w (ширина столбца даты) и l (количество строк, отводимые на неделю).
import calendar
print(calendar.month(2021, 9))
print(calendar.month(2021, 10))
print(calendar.month(2021, 9, w=3))
print(calendar.month(2021, 9, l=2))
print(calendar.month(2021, 9, w=5, l=2))
выводит:

   September 2021
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30

    October 2021
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

       September 2021
Mon Tue Wed Thu Fri Sat Sun
          1   2   3   4   5
  6   7   8   9  10  11  12
 13  14  15  16  17  18  19
 20  21  22  23  24  25  26
 27  28  29  30

   September 2021

Mo Tu We Th Fr Sa Su

       1  2  3  4  5

 6  7  8  9 10 11 12

13 14 15 16 17 18 19

20 21 22 23 24 25 26

27 28 29 30


              September 2021

 Mon   Tue   Wed   Thu   Fri   Sat   Sun

               1     2     3     4     5

   6     7     8     9    10    11    12

  13    14    15    16    17    18    19

  20    21    22    23    24    25    26

  27    28    29    30



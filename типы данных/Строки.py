# print (1,2,34,4, sep="|") Сделали разделитель вместо пробела |

# print (1,2,34,4, end="")  сменили перенос строки
# print(f"Эта переменная равна {x}") При F строке в {} подставится переменная f

# a, b, g = map(int, input("Enter").split()) или  input().split()
# print(a,b,g)

# Можно записать текст вот так text = '''sasfafafa '''

#srt(6) преобразовать в строку

#ВХОД СТРОКИ "str" in "string" возвращает bool

# ord() - определение кода символа
# chr() позволяет определить по коду символа сам символ. Аргументом данной функции является численный код.

# ПОЛУЧИТЬ ЧАСТЬ СТРОКИ str1 = str2[start:stop:step]
# НЕЛЬЗЯ МЕНЯТЬ значение в строке при доступе по индексу

# метод s.upper() переводит в верхний регистр

#"sasd".center() - выравнивание по центру

# метод s.lower() переводит в нижний регистр

# Метод capitalize()  делает первую букву Строки заглавной

# метод s.count(подстрока,start,end) поиск подстроки в строке ВЕРНЕТ колл повторрений

# метод s.find(подстрока,start,end) возвращает индекс вхождения подстроки в строку возвращает -1, если символ или подстрока sub не найдены.

# str.index(sub[, start[, end]]) возвращает индекс первого совпадения Метод бросает исключение ValueError, если символ или подстрока sub не найдены.

# метод s.rfind(подстрока,start,end) возвращает индекс вхождения подстроки в строку ПОИСК С ПРАВА НА ЛЕВО

# метод s.replace(старая подстрока,новая подстрока,максимальное число замен) меняет значение подстроки на новую подстроку

# метод s.isalpha() возвращает try есле вся строка состоит из букв И НЕТ ПРОБЕЛОВ

# метод s.isdigit() возвращает try есле вся строка состоит из цифр И НЕТ ПРОБЕЛОВ и НЕТ ЧИСЕЛ С ТОЧКОЙ

# метод s.rjust(колличество символов сколько должно быть в строке,сивол который добавляем)
# на выходе получим строку на N символов больше с левой стороны, опряделяем их значение
# метод s.ljust() таук же как и s.rjust только символы с ghfdf


# метод s.split(" ") разбивает строку на список по указанному символу
# метод "разделитель между строк ",      " ".join(список строк) обьеденяет список строк в одну строку

# метод s.strip() удаляет пустые символы в строке
# метод s.lstrip() удаляет пустые символы в строке
# метод s.rstrip() удаляет пустые символы в строке
# Методы strip(), lstrip(), rstrip() могут принимать на вход опциональный аргумент<chars>.
# Необязательный аргумент <chars>– это строка, которая определяет набор символов для удаления.

# strip() принимает строку с символами и удаляет все их вхождения с обеих сторон строки.
# Например, после такого вызова в переменной
# string окажется строка 'python':
# string = '?!@python)*^'
# string = string.strip('@*!)^?')

# str = r"\n \t" r выводит как записанно СЫРАЯ СТРОКА

#str.format(name, age) позволяет подставить в строку переменные
# "Меня зовут {0} а мая фамилия {1} то есть {1} {0}".format(name, age)
# Делаем с ключами
# "Меня зовут {name} а мая фамилия {famili} то есть {name} {famili}".format(name = name,famili = famili)

# использование f строк позволяет не использовать ключи а писать прямо в строке переменные
#f"Меня зовут {name} а мая фамилия {famili} то есть {name} {famili}"
# в {можем вызывать методы}

#eval(s = "11+22 - 3+4") выполняет действия в строке на выходе получим результат действий

# метод s.islower() реагирует только на маленькие буквы и возвращает try

#Метод swapcase()  возвращает копию строки s,
# в которой все символы, имеющие верхний регистр, преобразуются в символы нижнего регистра и наоборот.

#Метод title() возвращает копию строки s, в которой первый символ каждого слова переводится в верхний регистр.

# Метод startswith(<suffix>, <start>, <end>)  определяет начинается ли исходная строка s подстрокой <suffix>.
# Если исходная строка начинается с подстроки <suffix>,метод возвращает значение True

# Метод endswith(<suffix>, <start>, <end>) определяет оканчивается ли исходная строка s подстрокой <suffix>.
# Можно передавать несколько аргументов endswith(('.com','.ru')
# Метод возвращает значение True

# Метод isalnum() определяет, состоит ли исходная строка из буквенно-цифровых символов.
# Метод возвращает значение True

# Метод isspace() определяет, состоит ли исходная строка только из пробельных символов.
# Метод возвращает значение True

# format
# age = 27
# txt = 'My name is Timur, I am {}'.format(age)
# print(txt)
# Мы передаем необходимые параметры методу format, а Python форматирует указанную строку
# и помещает их в строку на место заполнителей {}. Мы можем создавать сколько угодно заполнителей в строке:
#
# age = 27
# name = 'Timur'
# profession = 'math teacher'
# txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, profession)
# print(txt)
# Для наглядности и гибкости форматирования мы можем использовать порядковый номер в заполнителе: {0}, {1}, {2},
# .... Такой номер определяет позицию параметра, переданного методу format (нумерация начинается с нуля):
#
# age = 27
# name = 'Timur'
# profession = 'math teacher'
# txt = 'My name is {0}, I am {1}, I work as a {2}'.format(name, age, profession)
# print(txt)
# Параметр name встает в {0} заполнитель, параметр age встает в {1} заполнитель и т.д.
# Мы можем использовать одно и тоже число в нескольких заполнителях
#
# name = 'Timur'
# txt = 'My name is {0}-{0}-{0}'.format(name)
# print(txt)
# Результатом выполнения такого кода будет:
#
# My name is Timur-Timur-Timur



# Метод partition() принимает на вход один аргумент sep,
# разделяет строку при первом появлении sep и возвращает кортеж, состоящий из трех элементов:
# часть перед разделителем, сам разделитель и часть после разделителя.
# Если разделитель не найден, то кортеж содержит саму строку, за которой следуют две пустые строки.
# s1 = 'abc-de'.partition('-')
# ('abc', '-', 'de')


s = "AAAcD D"
print(any(i.isdigit() for i in s))
print(s.isalnum())
#str.format(name, age) позволяет подставить в строку переменные
# "Меня зовут {0} а мая фамилия {1} то есть {1} {0}".format(name, age)
# Делаем с ключами
# "Меня зовут {name} а мая фамилия {famili} то есть {name} {famili}".format(name = name,famili = famili)

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


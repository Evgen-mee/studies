# :=
# Можем создавать переменную в print, while, for
# print(x := input(), len(x), type(x))  # создали переменную и сразу обратились к ней
# print(x)                              # переменная живет до конца программы


# while
# если НЕ установить скобки то (value := input("Name:"))
# то в value присвоеться результат сравнения так как код выполняется с лева на право
# 1 действие input("Name:") != '' получаем True или False
# 2 действие присваеваем значение в переменную value :=
#
# while (value := input("Name:")) != '':  # создали переменную value
#     print(value)                        # выводим содержимое value


# for
# позволяет сократить количество вызовов функции с помощью создания переменной в теле for
#
# c моржом функцию тест вызвали 1 раз
# присвоили ее результат в перерменую Y
# если y != 4 то в список записали y
# f_data = [y for x in data if (y := test(x)) != 4]
#
# без моржа два раза вызываем функцию
# на проверке условия
# при записи в лист
# f_data = [test(x) for x in data if test(x) != 4]


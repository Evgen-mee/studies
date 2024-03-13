# Модуль random стандартной библиотеки
# import random

# метод random.random() вернет случайное ВЕЩЕСТВЕННОЕ число от 0 до 1    0,918364521
# по равномерному закону распределения гарантированно что значения появляются с равной вероятностью

# метод random.uniform(1,5) вернет случайное ВЕЩЕСТВЕННОЕ число от 0 до 5     3,96758
# по равномерному закону в диапозоне a-b

# метод random.randint(1,5) вернет случайное ЦЕЛОЕ число от 0 до 5(включительно)     3
# по равномерному закону в диапозоне a-b


# метод random.randrange(start,stop, step)
# random.randrange(start,stop, step) вернет случайное ЦЕЛОЕ число от 0 до 5(НЕ включительно)     3
# при передачи шага (-3,10,2) всегда будем получать не четные числа


# Гаусовские случайные величины
# gauss(mu,sigma) - случайное значение по гаусовскому закону (формальный диапозон не ограничен)
# mu - математическое ожидание
# sigma - среднеквадратическое отклонение
# a = random.gauss(0,3.5)

# метод a = random.choice("коллекция") вернет случайное значение из коллекции

# метод random.shuffle("коллекция будет изменена") поменяет в коллекции все значения местами

# метод a = random.sample("коллекция", 3) вернет новый список без дублей из 3 рандомных экз коллекции

# random.seed("значение")
# метод a = random.choice("коллекция")
# при каждом вызове в a будет лежать одно и то же
# тк задали зерно генератора  random.seed("значение")

# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)
#
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyz
# 0123456789
# 0123456789abcdefABCDEF
# 01234567
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c

x = ""




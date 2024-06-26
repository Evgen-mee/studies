# к характеристикам хорошей хеш-функции можно отнести следующее:
#  - Лавинообразный эффект.
# небольшое изменение входных данных должно существенно изменять хеш-значение
#
#  - Быстрое вычисление.
# Поскольку хеш-функции используются при построении хеш-таблиц,
# а они используются для быстрого поиска данных,
# то сама хеш-функция должна работать очень быстро
#
#  - Минимальное количество коллизий.
# Хеш-функция не должна возвращать много одинаковых значений для разных входных данных
#
#  - Равномерное распределение хешей.
# Хеш-функция должна равномерно распределять хеш-значения при большом количестве входных данных,
# тем самым минимизируя количество коллизий и эффективно используя весь доступный диапазон чисел

# Встроенная функция hash()  является примером хорошей хеш-функции

# - подвержена лавинообразному эффекту(при незначительном изменение входных данных ЗНАЧИТЕЛЬНО изменяется хеш)
# print(hash('beegeek')) # 8630382989964334220
# print(hash('Beegeek')) # 5789365726824330891                # заменяем лишь первый символ строки


# -  выполняется быстро даже на очень больших входных данных
# from time import perf_counter
#
# start = perf_counter()
# hash('b' * 100_000_000)  #  большие входные данные
# end = perf_counter()
# print(end - start)       # 0.041030700027476996  результат в секундах


#  - равномерно распределяет хеш-значения
# Посмотрим на распределение ею хеш-значений печатных символов ASCII.
# Для наглядности сузим диапазон генерируемых хеш-значений до [0; 20)
#
# from collections import defaultdict
# from string import printable
#
# hashes = defaultdict(int)
#
# for char in printable:
#     hashes[hash(char) % 20] += 1
#
# for hash_value, hash_count in sorted(hashes.items()):
#     print(hash_value, '■' * hash_count)
# выводит:
#
# 0 ■■
# 1 ■■■■■■
# 2 ■■■■■■■■
# 3 ■■■
# 4 ■■■
# 5 ■■■■■■■
# 6 ■■■■
# 7 ■■■■■■■■
# 8 ■■■■■■
# 9 ■■■■■■■
# 10 ■■
# 11 ■■■■■■■
# 12 ■■■■■
# 13 ■■■■
# 14 ■■■
# 15 ■■■■■■
# 16 ■■■■
# 17 ■■■■■
# 18 ■■■■
# 19 ■■■■■■





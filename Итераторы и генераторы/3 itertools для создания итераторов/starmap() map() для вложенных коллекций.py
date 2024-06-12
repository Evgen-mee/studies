# возвращает итератор, элементами которого являются элементы переданного итерируемого объекта iterable,
# к которым была применена функция func

# Аргументы функции:
# func — произвольная функция
# iterable — итерируемый объект, элементами которого являются итерируемые объекты

# Функция starmap() используется вместо map() в том случае,
# когда элементами итерируемого объекта являются другие итерируемые объекты,

# from itertools import starmap
# persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
# pairs = [(1, 3), (2, 5), (6, 4)]
# points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
# full_names = list(starmap(lambda name, surname: f'{name} {surname}', persons))
# print(full_names)                                    # ['Timur Guev', 'Arthur Kharisov']
# print(*starmap(lambda a, b: a + b, pairs))           # 4 7 10
# print(*starmap(lambda x, y, z: x * y * z, points))   # 1 2 12




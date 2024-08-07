# Функции all и any

# Функция all()
# возвращает значение True если ВСЕ элементы переданной
# ей последовательности (итерируемого объекта) истинны
# print(all([True, True, True]))     #  возвращает True, так как все значения списка равны True
# print(all([True, True, False]))    #  возвращает False, так как не все значения списка равны True

# b = all(a = [True,True,True,])  b = bool
# all() вернет True есле все значения True

# b = all(a = [1,True,"LALALA",[]])  b = False
# тк все значение в списке в функции прировнялись к bool было [1,True,"LALALA",[]]
# то b = False
# было [1,True,"LALALA",[]]  стало [True,True,True,False]
# пустой вложенный список прировнялся к False


# Функция any()
# возвращает значение True  если хотя бы ОДИН элемент переданный является истинным
# print(any([False, True, False]))       #  возвращает True, так как есть хотя бы один элемент, равный True
# print(any([False, False, False]))      #  возвращает False, так как нет элементов, равных True

# b = any(a = [False,False,True,])  b = bool
# b = True тк хоть раз встретилось в коллекции True
# any() возвращает False есле все экземпляры после преобразование в функции False

# Функции all() и any() могут быть полезны в комбинации с функцией map()
#
# проверяет, все ли элементы списка numbers больше 10
# numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
# result = all(map(lambda x: x > 10, numbers))
#
# проверяет, что хотя бы один элемент списка четное число
# numbers = [17, 91, 78, 55, 231, 45, 5, 89, 99, 11, 19]
# result = any(map(lambda x: x % 2 == 0, numbers))




a, b, c = tuple(map(int, input()))
print(('NO','YES')[a + b == c])

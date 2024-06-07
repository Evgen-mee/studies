# список == массив
# имеем доступ по индексу
# можем менять значение по индексу
# можем содержать любые типы
# city = ["москва", "питер", "воронеж"]

# - list преобразует итерируемый тип данных в список
# x = list("1234") на выходе получаем x = ['1', '2', '3', '4']

#  - Копирования списка:
# x1 = x[:]
# x = copy(list())

# - Срезы
# x[2:4] = [8,9] или x[2:4] = 8,9 ЗАМЕНИЛИ ЗНАЧЕНИЯ по указанному срезу
# x1 = x[::-1] ИНВЕРСИЯ СПИСКА

# - Срезы
# [старт:стоп:шаг]
# x[2:4] = [8,9] или x[2:4] = 8,9 ЗАМЕНИЛИ ЗНАЧЕНИЯ по указанному срезу


# МЕТОДЫ

# - append(100) добавления нового элемента в конец списка


# - extend([1,2,3,4]) добавить список в конец списка
# При добавлении строки разбивает 'python' на  символы 'p', 'y', 't', 'h', 'o', 'n' и их добавляет в качестве элементов списка


# - del list()[индекс]  или срез [ср:ез] удалять элементы списка


# - insert(3,100) добавляет значение по индексу и сдвигает очередность
# по индексу 3 запишем 100, значение которое ранее было по индексу 3 сместится на индекс 4 и т.д.


# - index(нужное значение) возвращает первый индекс введенного значения если находит
# index(100, -1) вторым значением указываем индекс начала поиска значения
# если значения нет в коллекции то вернет ошибку перед использованием проверяем через in


# метод remove(нужное значение) удалит первое совпадение в списке
# Все элементы после удаленного элемента смещаются на одну позицию к началу
# если значения нет в коллекции то вернет ошибку перед использованием проверяем через in

# pop() удаляет последний элемент или элемент по индексу pop(3)
# удаляемый элемент можем сохранить в переменную x = lst.pop()  в x лежит удаленный элемент


# count(нужное значение) возвращает количество совпадений в списке


# метод reverse() меняет порядок элементов на обратный в текущем списке


# метод sort(x,reverse = True) сортирует от меньшего к большему текущий список


# sorted(x) вернет новый список без изменения исходного от минимального к большему
# что бы отсортировать от большего то добавляем второй аргумент sorted(reverse=True)

























# метод clear() очищает список

# метод copy() копирует список x=x1.copy() или x=x1[:] или x=list(x1)

# метод count(100) возвращает количество совпадений в списке согласно введенному значению (число)



# метод reverse() зеркалит список

#  МОЖНО СОРТИРОВАТЬ СТРОКИ

# ВЛОЖЕННЫЕ СПИСКИ

# lng = [[x[:],x[:],x[:]] обЪявили вложенный список с копированием

# Обращаемся к вложенному списку lng[0][1]





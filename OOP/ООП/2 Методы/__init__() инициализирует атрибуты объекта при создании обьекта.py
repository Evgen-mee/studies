# называют методом инициализации или инициализатором

# принимает в качестве аргумента уже созданный классом объект и инициализирует его.

# инициализирует атрибуты объекта. Сразу после создания объекта исполняется метод __init__(),
# и параметру self автоматически присваивается объект, который был только что создан,
# что позволяет тут же наделить его необходимыми атрибутами.

# полностью повторяет сигнатуру любой функции, поэтому с помощью *args и **kwargs
# она может принимать произвольное количество позиционных и именованных аргументов соответственно.


# class Cat:
#     def __init__(self, breed, name=None):            # задали атрибут по умолчанию
#         self.breed = breed
#         self.name = name
#
#
# cat1 = Cat('Британский', 'Кемаль')       # задали атрибуты при создании экземпляра
# cat2 = Cat('Манчкин')
#
# print(cat1.breed, cat1.name)                         # Британский Кемаль
# print(cat2.breed, cat2.name)                         # Манчкин None


# Класс может иметь только один инициализатор.
# При попытке определить в классе два инициализатора, предыдущий будет заменен следующим.
#
# class Cat:
#     def __init__(self, breed, name):
#         self.breed = breed
#
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
#
# cat = Cat('Британский', 'Кемаль')
#
# print(cat.breed)     # Британский
# print(cat.name)      # Кемаль


class Scales:
    def __init__(self):
        self.scales_left = 0
        self.scales_right = 0

    def add_right(self, n):
        self.scales_right += n

    def add_left(self, n):
        self.scales_left += n

    def get_result(self):
        if self.scales_left > self.scales_right:
            return 'Левая чаша тяжелее'

        if self.scales_right > self.scales_left:
            return 'Правая чаша тяжелее'

        return 'Весы в равновесии'








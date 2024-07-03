# методом имитации нескольких инициализаторов является использование методов класса,
# которые создаются декоратором @classmethod.

# В отличие от обычных методов, методы класса не принимают текущий экземпляр self в качестве аргумента.
# Вместо этого они принимают сам класс, который обычно передается в качестве аргумента cls

# Использование методов класса — это чистый и основанный на Python метод создания классов,
# имитирующих несколько методов инициализации.


# class Cat:
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
#     @classmethod
#     def create_british_cat(cls, name):
#         return cls('Британский', name)
#
#     @classmethod
#     def create_kemal_cat(cls, breed):
#         return cls(breed, 'Кемаль')
#
#
# cat1 = Cat('Британский', 'Кемаль')
# cat2 = Cat.create_british_cat('Роджер')
# cat3 = Cat.create_kemal_cat('Шотландский')
#
# print(cat1.breed, cat1.name)    # Британский Кемаль
# print(cat2.breed, cat2.name)    # Британский Роджер
# print(cat3.breed, cat3.name)    # Шотландский Кемаль

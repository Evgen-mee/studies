# возвращает значение атрибута и при этом не изменяет его, называется геттером.
# Геттеры дают возможность программному коду, находящемуся за пределами класса,
# получать значения атрибутов безопасным способом, не подвергая эти атрибуты изменению программным кодом,
# находящимся вне метода.

# class Cat:
#     def __init__(self, name):
#         self._name = name                               # имя кошки
#
#     def get_name(self):                                 # геттер, используется для получения имени
#         return self._name
#
# cat = Cat('Кемаль')
#
# print(cat.get_name())  # Кемаль

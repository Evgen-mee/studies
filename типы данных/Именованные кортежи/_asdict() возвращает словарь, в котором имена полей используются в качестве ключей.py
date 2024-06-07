# метод возвращает словарь, в котором имена полей используются в качестве ключей.
# Ключи результирующего словаря находятся в том же порядке, что и поля в исходном именованном кортеже.

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# timur = Person._make(['Timur', 29, 170])
# print(timur._asdict())          # {'name': 'Timur', 'age': 29, 'height': 170}
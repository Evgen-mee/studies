# содержит словарь, который сопоставляет имена полей с
# соответствующими значениями по умолчанию, если таковые имеются.

# Если именованный кортеж не предоставляет значений по умолчанию,
# тогда атрибут _field_defaults содержит пустой словарь

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height', 'country'], defaults=['Russia'])
# timur = Person('Тимур', 29, 170)
# print(timur)                    # Person(name='Тимур', age=29, height=170, country='Russia')
# print(timur._field_defaults)    # {'country': 'Russia'}
# print(Person._field_defaults)   # {'country': 'Russia'}
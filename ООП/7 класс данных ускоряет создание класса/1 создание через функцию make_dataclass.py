
# принимает в качестве аргументов:
# имя класса
# итерируемый объект с именами атрибутов и возвращает соответствующий класс данных

# from dataclasses import make_dataclass
# Person = make_dataclass('Person', ['name', 'surname', 'age'])          # Создали класс
# person = Person('Гвидо', 'ван Россум', 67)                             # Создали экземпляр класса
# print(person)                                                 # Person(name='Гвидо', surname='ван Россум', age=67)

# При использовании make_dataclass тоже можно указывать типы значений
# атрибутов, значения по умолчанию и делать экземпляры класса неизменяемыми.
# from dataclasses import make_dataclass, field
#
# Person = make_dataclass(
#     'Person',
#     [
#         ('name', str),
#         ('surname', str),
#         ('age', int, field(default=80))
#     ],
#     frozen=True
# )
#
# person = Person('Mick', 'Jagger')
# print(person)
#
# Person(name='Mick', surname='Jagger', age=80)



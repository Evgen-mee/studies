# способ имитации нескольких инициализаторов заключается в проверке типов аргументов
# чтобы обеспечить различное поведение в зависимости от конкретного типа
#
# Использование проверки типов аргументов для имитации нескольких инициализаторов
# относится к анти-паттернам в Python
#
#
# from datetime import date
#
# class Cat:
#     def __init__(self, breed, name, birth_date):
#         self.breed = breed
#         self.name = name
#         if isinstance(birth_date, date):                      # проверка на тип даты
#             self.birth_date = birth_date                      # дата рождения кошки
#         elif isinstance(birth_date, str):                     # проверка на тип строки
#             self.birth_date = date.fromisoformat(birth_date)  # дата рождения кошки на основе строки
#         else:
#             raise ValueError(f'неверный формат даты: {birth_date}')  # ловит все остальные типы данных
#
#
# cat1 = Cat('Британский', 'Кемаль', date(2021, 3, 31))         # передаем объект date
# cat2 = Cat('Шотландский', 'Роджер', '2020-09-10')                     # передаем строку
# cat3 = Cat('Британский', 'Кемаль', 1617173745)                        # передаем не предусмотренный формат
#
# print(cat1.breed, cat1.name, cat1.birth_date)  # Британский Кемаль 2021-03-31
# print(cat2.breed, cat2.name, cat2.birth_date)  # Шотландский Роджер 2020-09-10
# print(cat3.breed, cat2.name, cat2.birth_date)  # ValueError: неверный формат даты: 1617173745
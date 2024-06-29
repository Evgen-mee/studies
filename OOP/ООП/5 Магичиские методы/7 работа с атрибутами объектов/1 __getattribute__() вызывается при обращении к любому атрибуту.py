# __getattribute__() вызывается первым и вызывается всегда, а метод __getattr__()
# вызывается только в том случае, если атрибута, к которому происходит обращение, не существует.
# Если атрибут существует, метод __getattribute__() возвращает его значение,
# в противном случае вызывается метод __getattr__()

# __getattribute__() может вести себя так, будто атрибут заведомо существует,
# и не выполнять каких-либо дополнительных проверок
#
# Если атрибута не существует, базовая реализация все равно возбудит исключение AttributeError,
# и управление будет передано методу __getattr__().

# можем управлять обращением к тому или иному атрибуту


# мы обращаемся к методу __getattribute__() класса object
# и передаем ему в качестве аргумента объект и имя атрибута, значение по которому хотим получить
#
# Метод __getattribute__() класса object возвращает значение атрибута по указанному имени
# или возбуждает исключение AttributeError, если атрибут с указанными именем не был найден.
#
# class Cat:
#     def __init__(self, name):
#         self.name = name  # имя кошки
#
#     def __getattribute__(self, attr):
#         print(f'Возвращаю значение атрибута {attr}')
#         return object.__getattribute__(self, attr)  # получение значения атрибута attr объекта self
#
#
# cat = Cat('Кемаль')
#
# print(cat.name) # Возвращаю значение атрибута name  #Кемаль


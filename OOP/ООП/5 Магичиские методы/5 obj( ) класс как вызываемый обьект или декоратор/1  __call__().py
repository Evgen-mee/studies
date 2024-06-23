# позволяет экземплярам класса вести себя так, как будто они функции
# можем вызывать их, передавать их в функции, которые ожидают в качестве аргумента функцию, и так далее

# классы которые возвращают через () значения
# называются функторы

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, speech):
#         print('Меня зовут', self.name, 'и я делаю', speech)
#
#
# cat = Cat('Кемаль')
#
# cat('Мяу')       # Меня зовут Кемаль и я делаю Мяу           # равнозначно cat.__call__('Мяу')
# cat('Мяяяяяy')   # Меня зовут Кемаль и я делаю Мяяяяяy       # равнозначно cat.__call__('Мяяяяяy')

# Чтобы проверить, является ли объект вызываемым
# Используем функцию callable()
# print(callable(int))   # True
# print(callable(len))   # True
# print(callable(1))     # False


class Filter:

    def __init__(self, predicate=None):
        self.predicate = predicate

    def __call__(self, iterable):
        return [*filter(self.predicate, iterable)]


leave_even = Filter(lambda x: x % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6]

print(leave_even(numbers))





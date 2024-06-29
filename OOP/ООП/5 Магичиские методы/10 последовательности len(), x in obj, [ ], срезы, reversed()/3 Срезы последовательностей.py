# чтобы реализовать возможность использовать срезы, требуется
# в магические методы, работающие с индексами
# __getitem__() определяет поведение при доступе к элементу, используя синтаксис self[key]
# __setitem__() определяет поведение при присваивании значения элементу, используя синтаксис self[key] = value
# __delitem__() определяет поведение при удалении элемента с помощью оператора del
# передается объект типа slice

# Срезы реализуются с помощью slice объектов. (работает как range)
# они автоматически создаются и указываются в качестве индексов, когда мы используем синтаксис срезов.

# атрибуты:
# slice1 = slice(10)                              # start=None, stop=10, step=None
# slice2 = slice(1, 10)                           # start=1, stop=10, step=None
# slice3 = slice(1, 10, 2)                        # start=1, stop=10, step=2

# nums = [1, 2, 3, 4, 5]
# print(nums[slice(1, None, None)])               # равнозначно nums[1:]
# print(nums[slice(3)])                           # равнозначно nums[:3]
# print(nums[slice(1, 3)])                        # равнозначно nums[1:3]
# print(nums[slice(1, 4, 2)])                     # равнозначно nums[1:4:2]


# class Order:
#     def __init__(self, cart, customer):
#         self.cart = list(cart)
#         self.customer = customer
#
#     def __len__(self):
#         return len(self.cart)
#
#     def __getitem__(self, key):                               # передаем значение в obj[]
#         if isinstance(key, slice):                            # проверяем на slice
#             return Order(self.cart[key], self.customer)       # возвращаем новый обьект согласно переданного среза
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть целым числом')
#         if key < 0 or key >= len(self.cart):
#             raise IndexError('Неверный индекс')
#         return self.cart[key]
#
#     def __contains__(self, item):
#         return item in self.cart
#
#     def __iter__(self):
#         yield from self.cart
#
#
# order1 = Order(['банан', 'яблоко', 'лимон', 'дыня', 'грейпфрут'], 'Кемаль')
# order2 = order1[1:]
# order3 = order1[2:4]
# order4 = order1[1:5:2]
#
# print(*order2, sep=', ')  # яблоко, лимон, дыня, грейпфрут
# print(*order3, sep=', ')  # лимон, дыня
# print(*order4, sep=', ')  # яблоко, дыня
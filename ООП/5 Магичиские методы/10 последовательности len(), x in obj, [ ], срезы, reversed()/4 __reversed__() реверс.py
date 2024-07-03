# Чтобы определить поведение при передаче в функцию reversed()

# class Order:
#     def __init__(self, cart, customer):
#         self.cart = list(cart)
#         self.customer = customer
#
#     def __len__(self):
#         return len(self.cart)
#
#     def __getitem__(self, key):
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
#     def __reversed__(self):                               # определили метод
#         return reversed(self.cart)
#
#
# order = Order(['банан', 'яблоко', 'лимон'], 'Кемаль')
#
# print(*order, sep=', ')           # банан, яблоко, лимон
# print(*reversed(order), sep=', ') # лимон, яблоко, банан






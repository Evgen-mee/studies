# для создания итерируемого объекта достаточно определить только метод __iter__(),
# возвращаемым значением которого является итератор.

# у итерируемых объектов удобно пользоваться всеми возможностями генераторов
# генераторными выражениями
# генераторными функциями
# ключевые слова yield и yield from

# class Order:
#     def __init__(self, cart, customer):
#         self.cart = list(cart)          # список покупок
#         self.customer = customer        # имя покупателя
#
#     def __iter__(self):
#         yield from self.cart            # или с помощью выражения return (elem for elem in self.cart)
#
#
# order = Order(['банан', 'яблоко', 'лимон'], 'Элой')
#
# for item in order:
#     print(item)
#
# выводит:
# банан
# яблоко
# лимон







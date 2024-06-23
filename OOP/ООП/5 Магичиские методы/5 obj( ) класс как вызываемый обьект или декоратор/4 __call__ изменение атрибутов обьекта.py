# при передачи в скобки () значений
# в первый раз вызов отработает __init__
# в последующие вызовы через скобки () будет отрабатывать __call__

# class Point:
#     def __init__(self, x, y):
#         print("вызвался init")
#         self.x = x
#         self.y = y
#
#     def __call__(self, x, y):
#         self.x, self.y = x, y
#
#
# point = Point(1, 2)
# print(point.x, point.y)   # 1, 2
#
# point(3, 4)
# print(point.x, point.y)  # 3, 4
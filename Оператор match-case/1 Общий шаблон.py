# в case можем пользоваться или |
# Можем комбинировать условия обработки (_, autor, title, price, *_) | (autor, title, price)
# НО КОЛЛИЧЕСТВО И ИМЕНА ПЕРЕМЕННЫХ ДОЛЖНЫ СОВПАДАТЬ кроме _ *_
# переменные созданные в case существуют и за пределами блока match

# cmd = 1
#
# match cmd:
#     case "top" | "left" | "right":      # проверка на или
#         print('вверх, влево, или вправо')
#
#     # 1 Проверили на тип если совпал:
#     # 2 создали переменную command которая ссылается на cmd
#     # 3 проверили условие после if
#     # 4 перешли в сам блок
#     case int() as command if command > 5:
#         print('ввели единицу')
#
#     # сработает если не вошли не в один блок case так ка нет проверок
#     case command: # создали переменную command в которую записано значение cmd
#         print(f"Завершили проверку в match cmd {command}")


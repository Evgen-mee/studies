# import pickle
# name_file, _sum = (input() for _ in range(2))
# res_sum = 0
# with open(name_file, 'rb') as file:
#     obj = pickle.load(file)
#     if type(obj) is dict:
#         res_sum += sum(filter(lambda x: type(x) in (int, float), obj))
#
#     else:
#         obj = filter(lambda x: type(x) in (int, float), obj)
#         res_sum += max(obj, default=0) * min(obj, default=0)
#
# print(("Контрольные суммы не совпадают", "Контрольные суммы совпадают")[int(_sum) == res_sum])


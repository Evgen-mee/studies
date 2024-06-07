# import pickle
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)
# new_obj = pickle.loads(binary_obj)
# print(new_obj)
#
# obj и new_obj равны, то есть имеют одинаковое содержимое,
# однако объекты не являются идентичными!!!!
#
# print(obj == new_obj)       # True
# print(obj is new_obj)       # проверка на идентичность False
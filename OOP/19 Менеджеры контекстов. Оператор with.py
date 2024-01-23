# Менеджеры контекстов. Оператор with
# wits <менеджер контекста>as<переменная>:
# список конструкций


# менеджер контекста это класс в котором реализованны методы
# __enter__()срабатывает в момент создания обьекта менеджера контекста
# __exit__()срабатывает в момент завершения работы менеджера контекста
# exc_tb(tb - Traceback), трассировка, или же сообщение проще об ошибке
# exc_type - это ясно что тип ошибки
# exc_val - value - значение(экземпляр исключения Exception).
# ИЛИ ВО ВРЕМЯ возникновения ошибки

#with open("какойто файл") as fp:# вызвался метод __enter__  его результат присвоился в fp
#    for t in fp:
#       print(t)
# после того как отработал данный блок или вызвалось исключение сработал __exit__()
class DefenedVector:
    def __init__(self,v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False


v1 =[1,2,3]
v2 =[2,3]
try:
    with DefenedVector(v1) as dv:
        for i,d in enumerate(dv):
            dv[1] +=v2 [i]
except:
    print("ошибка")
print(v1)

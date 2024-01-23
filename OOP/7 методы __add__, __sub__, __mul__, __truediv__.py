# Магические методы __add__, __sub__, __mul__, __truediv__
#
# Если метод __iadd__ не определён, то используется __add__ для +=.
#
# метод __add__() - для операции сложения +
# метод __rad__() - позволяет сложить когда число с лево от класса 100 + Class отработает так же как __add__()
# метод __iadd__() - операция += не создает новый класс просто добавляет в текущий
#
# методы __r метод__() и __i метод__() есть для всех операций
#
# метод __sub__() - для операции вычитания -
# метод __mul__() - для операции умножения *
# метод __truediv__() - для операции деления /
#
#   x + y    __add__(self, other)
#   x - y    __sub__(self, other)
#   x * y    __mul__(self, other)
#   x / y    __truediv__(self, other)
#   x // y   __floordiv__(self, other)
#   x % y    __mod__(self, other)
#
#   x += y   __iadd__(self, other)
#   x -= y   __isub__(self, other)
#   x *= y   __imul__(self, other)
#   x /= y   __itruediv__(self, other)
#   x //= y  __ifloordiv__(self, other)
#   x %= y   __imod__(self, other)


class Clock:
    __DAY = 86400   #число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)): # лпределили с какими типами данных можем работать
            raise ArithmeticError("правый операнд должен быть int или Clock")
        sc = other # вспомогательная переменная которая будет меняться в зависимости от типа данных

        if isinstance(other, Clock):
            sc = other.seconds # если передали класс то обратились к его атрибуту и записали в спомогательную переменную
        return Clock(self.seconds + sc) # Вернули новый экземпляр класса

    def __radd__(self, other): # когда число стоит с лева от класса
        return self + other # вызовет определенный метод в классе __add__

    def __iadd__(self, other):  #+=
        if not isinstance(other, (int, Clock)):  # лпределили с какими типами данных можем работать
            raise ArithmeticError("правый операнд должен быть int или Clock")
        sc = other  # вспомогательная переменная которая будет меняться в зависимости от типа данных
        if isinstance(other, Clock):
            sc = other.seconds # если передали класс то обратились к его атрибуту и записали в спомогательную переменную
        self.seconds += sc
        return self # вернули ссылку на текущий класс


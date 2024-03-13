# Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие

# метод __eq__() - для равенства ==
# метод __ne__() - для НЕ равенства != если не определен отработает инвертированный __eq__

# метод __lt__() - для оператора меньше <  если не определен сработает инвертируемый __gt__
# метод __le__() - для оператора меньше или равно <=
# метод __gt__() - для оператора больше > если не определен сработает инвертируемый __lt__
# метод __ge__() - для оператора больше или равно >=


class Clock:
    __DAY = 86400   #число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):  # лпределили с какими типами данных можем работать
            raise TypeError("правый операнд должен быть int или Clock")

        sc = other if isinstance(other, int) else other.seconds
        return sc


    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

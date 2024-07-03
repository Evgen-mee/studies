# -__abs__() — определяет поведение для встроенной функции abs()

# - __round__() — определяет поведение для встроенной функции round();
#помимо экземпляра класса метод принимает необязательный аргумент n,
#который, как правило, означает количество знаков после запятой после округления

# - __trunc__() — определяет поведение для функции trunc() из модуля math

# - __floor__() — определяет поведение для функции floor() из модуля math

# - __ceil__() — определяет поведение для функции ceil() из модуля math


import math

class Angle:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Angle({self.value})'

    def __abs__(self):
        return Angle(abs(self.value))       # вернули новый экземпляр

    def __round__(self, n=None):
        if n is None:
            return Angle(round(self.value))  # вернули новый экземпляр
        return Angle(round(self.value, n))

    def __trunc__(self):
        return Angle(math.trunc(self.value)) # вернули новый экземпляр

    def __floor__(self):
        return Angle(math.floor(self.value)) # вернули новый экземпляр

    def __ceil__(self):
        return Angle(math.ceil(self.value)) # вернули новый экземпляр


angle = Angle(-101.54)

print(abs(angle))          # Angle(101.54)
print(round(angle))        # Angle(-102)
print(round(angle, 1))     # Angle(-101.5)
print(math.trunc(angle))   # Angle(-101)
print(math.floor(angle))   # Angle(-102)
print(math.ceil(angle))    # Angle(-101)



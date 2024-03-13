# Функция isinstance для проверки типов данных
# производит проверку с учетом наследования классов
# isinstance(обьект, тип данных)
# Проверяет обьект на тип данных и возвращает bool

# a = 5
# b = isinstance(a,int) проверели что a int
# b = True

# bool и int из за наследования от int при передачи вернут True
# что бы отлечить int и bool
# делаем проверку
# b = true
# x = type(b) is bool  на выходе true
# x = type(b) is int  на выходе false

# можно делать множественные проверки
# b = isinstance(a,(int, float))
# вернет true есле a int или float
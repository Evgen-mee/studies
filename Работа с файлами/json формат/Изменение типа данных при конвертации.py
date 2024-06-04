# Изменение типа данных
# автоматически определяет тип значения при десериализации
#
# в JSON используются другие типы данных, и не для всех типов данных
# в Python есть соответствия
# Таблица конвертации типов данных Python в JSON:
# Python     |	JSON
# dict       | 	object
# list,tuple | 	array
# str 	     |  string
# int, float | 	number
# True 	     |  true
# False 	 |  false
# None 	     |  null
#
# Таблица конвертации JSON в типы данных Python:
# JSON 	      |    Python
# object 	  |    dict
# array 	  |    list
# string 	  |    str
# number(int) |    int
# number(real)|    float
# true 	      |    True
# false 	  |    False
# null 	      |    None
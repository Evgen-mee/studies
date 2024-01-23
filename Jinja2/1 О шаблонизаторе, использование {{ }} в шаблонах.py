# {% %} - спецификатор шаблона

# {{ }} - выражение для вставки любых конструкций Python в шаблон
# воспринимается как словарь
# ключ=имя параметра шаблона
# Template("Мне {{ a }} лет и зовут {{ n }}"
# значение = переданная в шаблон переменная
# tm.render(n=name1, a=age)
# так же в шаблоне можем передавать любую конструкцию
# Template("Мне {{ a*2 }} лет и зовут {{ n.upper() }}"

# {# #} - блок комментариев
# # ##  - строковый комментарий

from jinja2 import Template   # импортировали класс Template из библиотеки jinja2

name1 = "Федор"
age = 28

tm = Template("Мне {{ a*2 }} лет и зовут {{ n.upper() }}")  # Создали экземпляр Template на основе шаблона
msg = tm.render(n=name1, a=age)        # вызвали метод render который в шаблон вставил переменные
                                       # и присвоили в переменную msg

# Работа с классом
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

per = Person("Федор",28)

tm1 = Template("Мне {{ p.getAge() }} лет и зовут {{ p.getName() }}")        # Вызвали методы класса
msg1 = tm1.render(p=per)                                           # Передали в шаблон ссылку на экземпляр
                                                                  # И записали в переменную msg1

# работа со словарем
per = {"name": "Федор", "age": 33}
tm2 = Template("Мне {{ p['age'] }} лет и зовут {{ p['name']] }}")        # создали шаблон
msg2 = tm2.render(p=per)                                                 # Передали ссылку на словарь в шаблон

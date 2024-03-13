# sum - вычесление суммы определенной коллекции
# sum(iterable, attribute=None, start=0)-Sum(коллекция, указываем поле если нужно, прибавка к сумме)
# полный список фильтров sum, max, min,replace и т.д https://proproprogs.ru/modules/filtry-i-makrosy-macro-call

#from jinja2 import Template   # импортировали класс Template из библиотеки jinja2

# пример №1
# cars = [
#     {'model': 'Ауди', 'price': 23000},
#     {'model': 'Шкода', 'price': 17300},
#     {'model': 'Вольво', 'price': 44300},
#     {'model': 'Фольксваген', 'price': 21300}
# ]
#
# tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"  # указываем на атрибут коллекции для сумы
# tm = Template(tpl)                                                    # записали в tm экз.класса jinja2 передав шаблон
# msg = tm.render(cs=cars)                                       # вызвали метод экз и передали в переменную cs коллекцию

# пример №2
# Большую гибкость в применении фильтров дает специальный блок:
# {{% filter <название фильтра> %}
# <фрагмент для применения фильтра>
# {% endfilter %}

# persons = [
#     {"name": "Алексей", "old": 18, "weight": 78.5},
#     {"name": "Николай", "old": 28, "weight": 82.3},
#     {"name": "Иван", "old": 33, "weight": 94.0}
#     ]
#
# tpl = '''
# {%- for u in users -%}
# {% filter upper %}{{u.name}}{% endfilter %}
# {% endfor -%}
# '''
# tm = Template(tpl)
# msg = tm.render(users=persons)
# print(msg)
# экранированная строка
#from jinja2 import Template   # импортировали класс Template из библиотеки jinja2
# data = '''{% raw %}модуль jinja вместо
# определения {{ name }}
# подстовляет соответствующие значения {% endraw %}'''
# После применения {% raw %} и {% endraw %} присвоение в переменную не сработает
# Пример1
# tm3 = Template(data)                              # создали шаблон
# msg3 = tm3.render(name="Федор")                   # присволили в переменную name

# msg3 =
# модуль jinja вместо
# определения {{ name }}
# подстовляет соответствующие значения

# Пример2
# Способ №1
#from jinja2.filters import escape
# <a href="#">Ссылка</a> в HTML-документе ссылки определяються так: Ссылка

# e - escape(экранирование) Флаг
# меняет символы <> <a> ТЕГИ
# для работы нужно подключить  from jinja2.filters import escape или from markupsafe import escape

# link = '''В HTML-документе ссылки определяются так:
# <a href="#">Ссылка</a>'''
#
# tm = Template("{{ linc | e }}")
# msg = tm.render(link=link)
# после применения шаблона в HTML-документе ссылки определяються так: <a href="#">Ссылка</a>

# Способ №2 результат как в способе № 1
# msg = escape(link)
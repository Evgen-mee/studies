# Модуль Jinja поддерживает макроопределения для шаблонов, которые весьма полезны,
# чтобы избежать повторяемых определений в соответствии с принципом

# Например, нам необходимо создать несколько полей
# ввода input в шаблоне HTML-документа. Его можно задать так:
# from jinja2 import Template
#
# html = '''
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# '''
# tm = Template(html)
# msg = tm.render()
# print(msg)

# Здесь с помощью ключевого слова macro задано макроопределение с именем input и набором параметров.
# Это очень похоже на определение функций в Python.
# Учитывая, что в качестве параметров можно указывать специальные:
#
# varargs – список переданных значений (параметров);
# kwargs – список переданных именованных параметров.
#
# А далее, мы используем этот макрос для создания трех полей input.
# Как видите, это может быть очень удобно.
# По аналогии можно создавать другие макросы и, затем, многократно их использовать в шаблонах.
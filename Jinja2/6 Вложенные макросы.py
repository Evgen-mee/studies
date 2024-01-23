# Модуль Jinja имеет специальное определение:

# {% call[(параметры)] <вызов макроса> %}
# <вложенный шаблон>
# {% endcall %}

# На уровне HTML-документа это выглядит так:
# <ul>
# <li>Алексей
#     <ul>
#     <li>age:
#     <li>weight: 78.5
#     </ul>
# <li>Николай
#     <ul>
#     <li>age:
#     <li>weight: 82.3
#     </ul>
# <li>Иван
#     <ul>
#     <li>age:
#     <li>weight: 94.0
#     </ul>
# </ul>

# Создадим шаблон, который позволяет генерировать
# такой список на основе коллекции:

# persons = [
#     {"name": "Алексей", "old": 18, "weight": 78.5},
#     {"name": "Николай", "old": 28, "weight": 82.3},
#     {"name": "Иван", "old": 33, "weight": 94.0}
# ]
#
# # Далее, определим макрос, который генерирует начальный список из имен.
# # Его можно представить так:
# html = '''
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in users -%}
#     <li>{{u.name}}
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {{list_users(users)}}
# '''
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg) # получили просто список имен

# теперь для каждого человека добавим вложенный список с его возрастом и весом.
# И сделаем это через блок call.

# persons = [
#     {"name": "Алексей", "old": 18, "weight": 78.5},
#     {"name": "Николай", "old": 28, "weight": 82.3},
#     {"name": "Иван", "old": 33, "weight": 94.0}
# ]
# html = '''
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
#     <li>{{u.name}} {{caller(u)}}
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#     <li>age: {{user.old}}
#     <li>weight: {{user.weight}}
#     </ul>
# {% endcall -%}
#'''
# мы здесь прописали call с передаваемым ему параметром user
# – это будет текущий словарь, взятый из списка persons.
# Далее, указываем макрос, который следует вызвать для этого блока call.
# А все что записано внутри этого блока будет подставлено на место вызова метода caller
# внутри макроса list_users. В результате будет сформирован искомый список.

# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg) # получили просто список имен

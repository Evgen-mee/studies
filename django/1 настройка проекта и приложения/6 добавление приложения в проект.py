# Django не "знает" о приложении, пока мы явно не добавим его в файл проект/settings.py

# 1 открываем файл проекта settings.py
# 2 вносим имя проекта или путь в раздел INSTALLED_APPS


# В большинстве случаев можно использовать 1й способ, указывая только имя приложения.
# Точный путь к конфигурационному классу следует использовать когда их несколько в файле apps.py,
# это удобнее чем устанавливать в файле apps.py атрибут default = True для нужного конфигурационного класса.


# Способ № 1
# указывается только имя приложения

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'blog',                             # имя нашего приложения
# ]
#
# При указании имени приложения Django ищет конфигурационный класс в файле apps.py данного приложения.
# Если там их несколько, то используется тот, у которого значение атрибута default = True.
# Если он один, то будет использоваться он, вне зависимости от значения атрибута default.
# Если нет ни одного, тогда будет использоваться базовый класс AppConfig из django.apps.


# Способ № 2
# указывается путь к конфигурационному классу приложения,
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'blog.apps.BlogConfig',            # путь к конфигурационному классу нашего приложения
# ]
#
# В данном примере путь blog.apps.BlogConfig, где
#  - blog приложение
#  - apps - модуль(файл blog/apps.py)
#  - BlogConfig конфигурационный класс.
#
# способ позволяет задать имя используемого конфигурационного
# класса(их может быть несколько в файле apps.py) через файл настроек.
#
# Код конфигурационного класса BlogConfig можно посмотреть в файле blog/apps.py,
# файл с ним был создан автоматически вместе с приложением.
# посмотрим на его содержимое:
#
# from django.apps import AppConfig
#
# class BlogConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'blog'
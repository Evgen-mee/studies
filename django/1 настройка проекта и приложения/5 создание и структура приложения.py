# что бы создать приложение в проекте вводим команду в терминал
# python manage.py startapp имя приложения


# Базовая структура приложения
#  __init__.py
#  пустой  файл,  который  сообщает  Python,  что  каталог blog нужно трактовать как пакет Python;

#  admin.py
#  здесь вы регистрируете модели, чтобы управлять ими через веб-интерфейс админ панели нашего сайта;

#  apps.py:
#  содержит главную конфигурацию приложения blog;

#  migrations:
#  этот каталог будет содержать миграции базы данных приложения.
#  Миграции позволяют Django отслеживать изменения модели соответствующим образом
#  синхронизировать базу данных. Указанный каталог содержит пустой файл __init__.py;

#  models.py:
#  содержит относимые к приложению модели данных.
#  Если вы не будете использовать модели в своем приложении, его можно удалить;

#  tests.py:
#  здесь можно добавлять относимые к приложению тесты;

#  views.py:
#  здесь расположена логика приложения;
#  каждое представление получает HTTP-запрос, обрабатывает его и возвращает ответ.
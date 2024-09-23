# в запросе http://127.0.0.1:8000/blog/3/Tom/
# 3/Tom/ представляют параметры URL
#
# в запросе http://127.0.0.1:8000/blog?id=3&name=Tom
# 3 и Tom представляют параметры строки запроса
#
# Параметры строки запроса указываются после ?
# параметр представляет пару ключ-значение id=3
#
# Параметры в строке запроса отделяются друг от друга & id=3&name=Tom


# request.GET - это словарь переменных GET-запросов
# имеет метод .get()

# в файле views.py
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse('<h2>Главная</h2>')
#
# def user(request):
#     age = request.GET.get('age', 0)                               # получили значение по ключу
#     name = request.GET.get('name', 'Undefined')                   # получили значение по ключу
#     return HttpResponse(f'<h2>Имя: {name}, Возраст: {age}</h2>')  # вернули строку


# в файле urls.py приложения
#
# from django.urls import path
# from blog import views
#
# urlpatterns = [
#     path('', views.index),
#     path('user/', views.user)
# ]

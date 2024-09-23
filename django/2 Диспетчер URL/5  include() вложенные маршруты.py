# include(pattern_list)
# Параметр pattern_list представляет набор вызовов функций path() и/или re_path()
#
# Можем сделать набор маршрутов который для определенного шаблона


# 1 внесем путь в файл проекта urls.py
#
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls')),     # 1 все запросы кроме admin отправляем в приложение blog
# ]


# 2 определим маршруты в urls.py приложения
# from django.urls import path, include
# from blog import views
#
# product_patterns = [                   # 3 определен набор маршрутов, который касается товаров
#     path('', views.products),
#     path('comments/', views.comments),
#     path('questions/', views.questions),
# ]
#
# urlpatterns = [
#     path('', views.index),
#     path('products/<int:id>/', include(product_patterns)), # 2 при передачи products/int/ параметр
#                                                            # include выбирет из маршрутов соответствующий
#                                                            # дочерний маршрут получает параметр родительского
#                                                            # и передаст значение в представление
# ]


# 3 добавим представления
# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse('Главная страница')
#
# def products(request, id):                            # 4 отработает представление
#     return HttpResponse(f'Товар {id}')
#
# def comments(request, id):
#     return HttpResponse(f'Комментарии о товаре {id}')
#
# def questions(request, id):
#     return HttpResponse(f'Вопросы о товаре {id}')








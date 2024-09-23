# Когда запрос приходит к приложению, то система проверяет соответствие запроса маршрутам
# по мере их определения:
# вначале сравнивается первый маршрут, если он не подходит,
# то сравнивается второй и так далее.
#
# Поэтому более общие маршруты должны определяться в последнюю очередь,
# а более конкретные маршруты должны идти в начале.


# В данном случае адрес ^about/contact/ представляет более конкретный маршрут по сравнению c ^about/.
# Поэтому он определяется в первую очередь
#
# from django.urls import path, re_path
# from blog import views
#
# urlpatterns = [
#     re_path(r'^about/contact/', views.contact),
#     re_path(r'^about/', views.about),
#     path('', views.index),
# ]
#
#
# запрос по адресу ^about/contact/ обрабатывался бы функцией views.about
#
# urlpatterns = [
#     path('', views.index),
#     re_path(r'^about/', views.about),
#     re_path(r'^about/contact/', views.contact),
# ]



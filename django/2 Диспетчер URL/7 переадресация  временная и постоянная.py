# При временной переадресации мы указываем, что документ временно перемещен на новый адрес
#
# При постоянной переадресации мы уведомляем, что документ теперь постоянно будет доступен по новому адресу


# from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
#
# def index(request):
#     return HttpResponse('Index')
#
# def about(request):
#     return HttpResponse('About')
#
# def contact(request):
#     return HttpResponseRedirect('/about/') # временная переадресация будет перенаправлять по пути about
#
# def details(request):
#     return HttpResponsePermanentRedirect('/') # постоянная переадресация перенаправляет на корень веб-приложения



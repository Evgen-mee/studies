# Статусный код                     Класс
#
# 304 (Not Modified)           HttpResponseNotModified
#
# 400 (Bad Request)            HttpResponseBadRequest
#
# 403 (Forbidden)              HttpResponseForbidden
#
# 404 (Not Found)              HttpResponseNotFound
#
# 405 (Method Not Allowed)     HttpResponseNotAllowed
#
# 410 (Gone)                   HttpResponseGone
#
# 500 (Internal Server Error)  HttpResponseServerError

# В функцию конструктора этих классов можно передать сообщение об ошибке
#
# HttpResponseNotModified('Not Modified')
# HttpResponseBadRequest('Bad Request')
# HttpResponseForbidden('Forbidden')
# HttpResponseNotFound('Not Found')
# HttpResponseNotAllowed('Method is not allowed')
# HttpResponseGone('Content is no longer here')
# HttpResponseServerError('Server Error')

# Все эти классы может заменить HttpResponse()
# если передать соответствующие параметры HttpResponse('Not Found', status=404)
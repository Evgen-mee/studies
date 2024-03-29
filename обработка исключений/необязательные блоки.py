# блок else
# выполняется только в том случае,
# если при выполнении кода в trу блоке ошибок (исключений) не было.
# try:
#     # контролируемый код
# except тип_ошибки_1:
#     # код обработки ошибки (исключения)
# except тип_ошибки_2:
#     # код обработки ошибки (исключения)
# ...
# except тип_ошибки_n:
#     # код обработки ошибки (исключения)
# else:
#     # код для случая, если ошибки (исключения) не было
#
#
#
# Блок else в конструкции try-except подобен блоку else в конструкциях for/while.
# Он срабатывает если в контролируемом коде не произошло ошибок
# (если тело цикла завершилось штатным способом, без break).

#
# блок finally
# одержит программный код, который выполняется в любом случае
#
# try:
#     # контролируемый код
# except тип_ошибки_1:
#     # код обработки ошибки (исключения)
# except тип_ошибки_2:
#     # код обработки ошибки (исключения)
# ...
# except тип_ошибки_n:
#     # код обработки ошибки (исключения)
# finally:
#     # код, который выполняется всегда
#
#
# Блоки try-except можно вкладывать один в другой.
# Python никак нас не ограничивает в количестве таких вложений.
# try:
#     file = open('data.txt', encoding='utf-8')
#     try:
#         text = file.read()
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Файл с указанным именем не найден!')
# except:
#     print('Произошла ошибка!')
#
#
# Общий шаблон инструкции try-except
# try:
# # контролируемый код
# except тип_ошибки_1:
# # код обработки ошибки (исключения)
# except тип_ошибки_2:
# # код обработки ошибки (исключения)
# ...
# except тип_ошибки_n:
# # код обработки ошибки (исключения)
# else:
# # код для случая, если ошибки не было
# finally:
# # код, который выполняется всегда
#
#
# блок finally выполняется до return
# def func():
#     try:
#         return 10
#     finally:
#         print('Выполняется блок finally!')
#
# print(func())
# выводит:
# Выполняется блок finally!
# 10
#
#
# Приоритет return - finally в функциях.
# Выполняются все инструкции до return ;
# Когда 'доходит' до return - то return запоминает сам объект, что должен вернуть;
# Выполняется проверка на наличие блока finally : если его нет - возвращается значение из return ,
# если есть - выполняется код из finally (логично).
# def f():
#     try:
#         x = 10
#         return x
#     finally:
#         x = 20
#
# print(f()) == 20
#
# Важно понимать! Если объект меняется (на месте) в блоке finally,
# то return вернёт изменённый объект, в противном случае return вернёт то, что 'запомнил'.
# def f():
#     try:
#         x = [10]
#         return x
#     finally:
#         x.append(20)
# print(f()) == [10,20]






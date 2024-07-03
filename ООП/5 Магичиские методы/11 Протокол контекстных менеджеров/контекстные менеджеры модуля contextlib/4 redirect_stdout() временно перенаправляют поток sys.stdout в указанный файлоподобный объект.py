#  для построения контекстных менеджеров, которые временно перенаправляют поток
#  sys.stdout в указанный файлоподобный объект.


# from contextlib import redirect_stdout
#
# with open('output.txt', mode='w', encoding='utf-8') as file:
#     with redirect_stdout(file):
#         print('Python generation!')
#         help(len)
# создает файл output.txt с содержимым:
#
# Python generation!
# Help on built-in function len in module builtins:
#
# len(obj, /)
#     Return the number of items in a container.
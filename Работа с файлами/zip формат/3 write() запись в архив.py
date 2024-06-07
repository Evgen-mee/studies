
#mode='w' создание нового zip
# from zipfile import ZipFile
# with ZipFile('archive.zip', mode='w') as zip_file: # создаем архив
#     zip_file.write('program.py')                       # записали в архив файл program.py
#     zip_file.write('lse.jpeg')                         # записали в архив файл program.py
#     print(zip_file.namelist())                         # выводим список всех файлов


# mode='a' запись в существующий архив
# from zipfile import ZipFile
#
# with ZipFile('test.zip', mode='a') as zip_file:                   # открыли zip на чтение
#     zip_file.write('program.py', 'test/program.py')   # добавляем файл в папку test
#     zip_file.write('lse.jpeg')                                        # добавляем файл в корень архива
#     print(*zip_file.namelist(), sep='\n')                             # выводим список всех файлов
#
# выводит:
# test/
# test/Картинки/
# test/Картинки/1.jpg
# test/Картинки/avatar.png
# test/Картинки/certificate.png
# test/Картинки/py.png
# test/Картинки/World_Time_Zones_Map.png
# test/Картинки/Снимок экрана.png
# test/Неравенства.djvu
# test/Программы/
# test/Программы/image_util.py
# test/Программы/sort.py
# test/Разные файлы/
# test/Разные файлы/astros.json
# test/program.py
# lse.jpeg
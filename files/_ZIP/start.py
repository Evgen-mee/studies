# Архивация файлов —
# упаковка нескольких файлов в один файл или поток — архив.
# Не следует путать архивацию со сжатием,
# которое далеко не всегда применяется при создании архива.

# Для того чтобы проверить является ли некоторый файл zip архивом,
# используется функция zipfile.is_zipfile(),
# которая принимает на вход путь к файлу (или сам файловый объект)
# и возвращает значение True, если указанный файл является zip архивом,
# или False в противном случае.
#
# Архивный файл – это специальным образом организованный файл,
# содержащий в себе один или несколько файлов в сжатом или несжатом виде
# и служебную информацию об именах файлов, дате и времени их создания или модификации, размерах и т.д.
#
# from zipfile import ZipFile
# ZipFile похожи на файловые объекты,
# возвращаемые функцией open()
#
#
#  - printdir() Метод
# выводит таблицу с информацией о содержимом архива:
# полные названия файлов
# с указанием даты изменения
# и размера в байтах.

# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     zip_file.printdir()
# Вывидет:
# /usr/bin/python3 /home/jo/Документы/Studies/files/_ZIP/start.py
# File Name                                             Modified             Size
# test/                                          2021-11-27 12:47:10            0
# test/Картинки/                                 2021-11-27 12:49:02            0
# test/Картинки/1.jpg                            2021-09-02 12:30:20        90156
# test/Картинки/avatar.png                       2021-08-20 09:38:44        19053
# test/Картинки/certificate.png                  2021-10-23 09:46:36        43699
# test/Картинки/py.png                           2021-07-28 17:55:56        33522
# test/Картинки/World_Time_Zones_Map.png         2021-11-08 07:30:06      2324421
# test/Картинки/Снимок экрана.png                2021-10-01 20:47:02        10878
# test/Неравенства.djvu                          2021-08-19 08:39:06      5283010
# test/Программы/                                2021-11-27 12:48:20            0
# test/Программы/image_util.py                   2021-11-18 12:42:22         4955
# test/Программы/sort.py                         2021-11-14 19:31:02           61
# test/Разные файлы/                             2021-11-27 12:48:10            0
# test/Разные файлы/astros.json                  2021-11-08 09:29:58          505
#
#  - mode По умолчанию 'r'
# необязательный аргумент
# задает режим работы
#
# r — файл будет открыт для чтения
# w — если файл существует, то он будет уничтожен и вместо него будет создан новый файл
# a — существующий файл будет открыт в режиме добавления в конец


# - infolist() метод
# позволяет получить информацию о файлах
# в виде списка специальных объектов (тип ZipInfo)
# содержат дополнительную информацию о каждом файле
#
# - file_size
# - compress_size
# - filename
# - date_time     # date_time представляет из себя кортеж (год, месяц, день, час, минута, секунда)
#
# rom zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time)                # дата изменения файла
#
#
# - is_dir() метод
# проверить тип объекта: файл или папка.
# возвращает True, если объект является папкой,
# или False в противном случае
#
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[0].is_dir())
#     print(info[6].is_dir())
#
#
#  - namelist() метод
# возвращает список названий файлов и директорий,
# содержащихся в архиве
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     print(*info, sep='\n')
#
# выводит
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
#
#
# - getinfo() метод
# позволяет получить информацию о конкретном файле по его имени в архиве
#
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()                # получаем названия всех файлов архива
#     last_file = zip_file.getinfo(info[-4])    # получаем информацию об отдельном файле
#     print(last_file.file_size)
#     print(last_file.compress_size)
#     print(last_file.filename)
#     print(last_file.date_time)
# выводит:
# 4955
# 1641
# test/Программы/image_util.py
# (2021, 11, 18, 12, 42, 22)


# Работа с конкретными файлами из архива
#
# ЧТЕНИЕ
# ZipFile.open() открывает файл именно в бинарном виде
#
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read())
#
# Выводит:
# (b'{"number": 10, "people": [{"craft": "ISS", "name": "Mark Vande Hei"}, '
#  b'{"craft": "ISS", "name": "Pyotr Dubrov"}, {"craft": "ISS", "name": "Thomas Pesquet"}, '
#  b'{"craft": "ISS", "name": "Megan McArthur"}, {"craft": "ISS", "name": "Shane Kimbrough"}, '
#  b'{"craft": "ISS", "name": "Akihiko Hoshide"}, {"craft": "ISS", "name": "Anton Shkaplerov"}, '
#  b'{"craft": "Shenzhou 13", "name": "Zhai Zhigang"}, {"craft": "Shenzhou 13", "name": "Wang Yaping"}, '
#  b'{"craft": "Shenzhou 13", "name": "Ye Guangfu"}], "message": "success"}')
#
# b перед выводом бинарная строка
#
#
# - file.read()
# возвращает сырые байты (тип bytes)
# преобразовать их в строку использовать метод decode(),
# указав нужную кодировку
#
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read().decode('utf-8'))
#
# выводит:
# {"number": 10, "people": [{"craft": "ISS", "name": "Mark Vande Hei"},
#                           {"craft": "ISS", "name": "Pyotr Dubrov"},
#                           {"craft": "ISS", "name": "Thomas Pesquet"},
#                           {"craft": "ISS", "name": "Megan McArthur"},
#                           {"craft": "ISS", "name": "Shane Kimbrough"},
#                           {"craft": "ISS", "name": "Akihiko Hoshide"},
#                           {"craft": "ISS", "name": "Anton Shkaplerov"},
#                           {"craft": "Shenzhou 13", "name": "Zhai Zhigang"},
#                           {"craft": "Shenzhou 13", "name": "Wang Yaping"},
#                           {"craft": "Shenzhou 13", "name": "Ye Guangfu"}],
#                           "message": "success"}


# Запись в zip архив
#
# - write() метод
# принимает имя существующего файла
#
# from zipfile import ZipFile
# with ZipFile('archive.zip', mode='w') as zip_file:  # cоздает в папке с программой архив с именем archive.zip
#     zip_file.write('program.py')                        # записывает в него содержимое program.py
#     zip_file.write('lse.jpeg')                          # записывает в него содержимое lse.jpeg
#     print(zip_file.namelist())                          # выводит список всех файлов данного архива
#
#
# write() может принимать еще один строковый аргумент,
# задающий новое имя файла в архиве.
#
# from zipfile import ZipFile
# with ZipFile('archive.zip', mode='w') as zip_file:
#     zip_file.write('program.py', 'new_program.py')  # первый аргумент - это имя файла второй аргумент - это имя файла в архиве
#     zip_file.write('lse.jpeg', 'lse1.jpeg')         # первый аргумент - это имя файла второй аргумент - это имя файла в архиве
#     print(zip_file.namelist())                                       # выводит список всех файлов данного архива
#
#
# добавления файлов в уже существующий архив
# необходимо создать объект ZipFile в режиме mode='a'
# from zipfile import ZipFile
# with ZipFile('test.zip', mode='a') as zip_file:      # создали объект ZipFile в режиме mode='a'
#     zip_file.write('program.py', 'test/program.py')  # записали файл в папку test
#     zip_file.write('lse.jpeg')                                       # записали файл в корневую папку
#     print(*zip_file.namelist(), sep='\n')                            # выводит список всех файлов данного архива
#
#
# Извлечение содержимого zip-файла в каталог
#
#  - extract() метод извлечь отдельные файлы
# ринимает два аргумента: название файла и путь
# Если путь не указывать, то файл будет извлечен в папку,
# где находится файл с программой
#
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     zip_file.extract('test/Картинки/avatar.png')
#     zip_file.extract('test/Программы/image_util.py')
#     zip_file.extract('lse.jpeg')
#
#  - extractall() извлечь все содержимое архива
# принимает в качестве аргумента путь,
# по которому требуется извлечь все файлы.
# Если путь не указывать, то файл будет извлечен в папку,
# где находится файл с программой.
#
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     zip_file.extractall()
#
# извлекает все содержимое файла test.zip в папку,
# где находится файл с программой,
# при этом структура каталогов архива сохраняется.

#  - members необязательный аргумент
# умолчанию имеет значение None
# Если ему не передавать никакие другие значения, то он принимает список всех файлов из архива.
# Если же мы передадим в args названия файлов, которые нужно извлечь, то members примет кортеж файлов и извлечет их.
# Если же в args ничего не передавать, тогда members примет пустой кортеж и ничего извлекать вообще не будет.
# Это отличается от поведения по умолчанию, которое было описано выше.
# Для этого и нужна проверка на пустой кортеж.
# Если кортеж пуст, присваиваем переменной args значение None, и тогда извлекутся все файлы.
# from zipfile import ZipFile
# def extract_this(zip_name: str, *args):
#     if not args:
#         args = None
#     with ZipFile(zip_name) as zf:
#         zf.extractall(members=args)

# или
#
# def extract_this(zip_name: str, *args):
#     with ZipFile(zip_name) as zf:
#         zf.extractall(members=args or None)























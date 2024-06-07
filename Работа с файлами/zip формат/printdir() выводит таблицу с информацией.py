#Выводит полные названия файлов с указанием даты изменения и размера в байтах


#  - mode По умолчанию 'r'необязательный аргумент
# задает режим работы
# r — файл будет открыт для чтения
# w — если файл существует, то он будет уничтожен и вместо него будет создан новый файл
# a — существующий файл будет открыт в режиме добавления в конец

# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     zip_file.printdir()

# Вывидет:
# /usr/bin/python3 /home/jo/Документы/Studies/Работа с файлами/zip формат/1 pickle модуль.py
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
# - infolist() метод
# позволяет получить информацию о файлах
# в виде списка специальных объектов (тип ZipInfo)
# содержат дополнительную информацию о каждом файле
# - file_size        # размер начального файла в байтах
# - compress_size    # размер сжатого файла в байтах
# - filename         # имя файла
# - date_time        # дата изменения файла представляет из себя кортеж (год, месяц, день, час, минута, секунда)

# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)             # 2324421
#     print(info[6].compress_size)         # 2322032
#     print(info[6].filename)              # test/Картинки/World_Time_Zones_Map.png
#     print(info[6].date_time)             # (2021, 11, 8, 7, 30, 6)








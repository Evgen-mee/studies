# позволяет получить информацию о конкретном файле по его имени в архиве
#
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()                # получаем названия всех файлов архива
#     last_file = zip_file.getinfo(info[-4])    # получаем информацию об отдельном файле
#     print(last_file.file_size)                # 4955
#     print(last_file.compress_size)            # 1641
#     print(last_file.filename)                 # test/Программы/image_util.py
#     print(last_file.date_time)                # (2021, 11, 18, 12, 42, 22)
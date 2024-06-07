# Метод ZipFile.open() открывает файл именно в бинарном виде, не в текстовом.

# decode('utf-8') переводит байт код в str

# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:                            # открыли zip
#     with zip_file.open('test/Разные файлы/astros.json') as file: # открыли конкретный файл
#         print(file.read().decode('utf-8'))                       # указали кодировку в decode
#
# выводит:
# {"number": 10, "people":
#     [{"craft": "ISS", "name": "Mark Vande Hei"}, {"craft": "ISS", "name": "Pyotr Dubrov"},
#      {"craft": "ISS", "name": "Thomas Pesquet"}, {"craft": "ISS", "name": "Megan McArthur"},
#      {"craft": "ISS", "name": "Shane Kimbrough"}, {"craft": "ISS", "name": "Akihiko Hoshide"},
#      {"craft": "ISS", "name": "Anton Shkaplerov"}, {"craft": "Shenzhou 13", "name": "Zhai Zhigang"},
#      {"craft": "Shenzhou 13", "name": "Wang Yaping"}, {"craft": "Shenzhou 13", "name": "Ye Guangfu"}],
#  "message": "success"}
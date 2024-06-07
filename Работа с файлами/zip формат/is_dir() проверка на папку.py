# Он возвращает True, если объект является папкой, или False в противном случае.
#
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[0].is_dir())        # True
#     print(info[6].is_dir())        # False
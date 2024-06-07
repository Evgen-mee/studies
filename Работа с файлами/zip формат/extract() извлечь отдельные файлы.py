# принимает два аргумента:
#  - название файла
#  - путь по которому требуется извлечь файл
#
# Если путь не указывать, то файл будет извлечен в папку, где находится файл с программой
#
# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     zip_file.extract('test/Картинки/avatar.png')
#     zip_file.extract('test/Программы/image_util.py')
#     zip_file.extract('lse.jpeg')
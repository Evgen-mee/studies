# Инструкция raise и пользовательские исключения
#
class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать {str(data)}")


    def send_data(self, data):
        if not self.send_to_print(data): # проверяем могут ли данные быть отправленны на печать
            raise Exception("принтер не отвечает") # если не могут то генерирвуем свое исключение

    def send_to_print(self, data):
        return False

p = PrintData()

try: # Отлавливаем ошибку
    p.print("123")
except Exception:
    print("принтер не отвечает")


# так же можно создавать свой класс исключений
class ExceptionPrintError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"ошибка: {self.message}"

# и мы можем отлавливать конкретное исключение а не все Exception
try: # Отлавливаем ошибку
    p.print("123")
except ExceptionPrintError: # ловим конкретное исключение
    print("принтер не отвечает")
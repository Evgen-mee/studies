# Часто используемые шаблоны
#  - \n Новая строка
#  - . Любой символ, кроме символа новой строки. Если flags=re.DOTALL - любой символ.
#  - \s Любой символ пробела, табуляции или новой строки.
#  - \S Любой символ, кроме пробела, табуляции или новой строки.
#  - \d Любая цифра. Ищет все цифры: арабские, персидские, индийские, и так далее. Не эквивалентен [0-9]
#  - \D Любой символ, кроме цифр.
#  - \w Любая буква, цифра, или _. Шаблон не соответствует выражению [a-zA-Z0-9_]! Буквы используются не только латинские, туда входит множество языков.
#  - \W Любой символ, кроме букв, цифр, и _.
#  - \b Промежуток между символом, совпадающим с \w, и символом, не совпадающим с \w в любом порядке.
#  - \B Промежуток между двумя символами,совпадающими с \w или \W.
#  - \A Начало всего текста
#  - \Z Конец всего текста
#  - ^ Начало всего текста или начало строчки текста, если flags=re.MULTILINE
#  - $ Конец всего текста или конец строчки текста, если flags=re.MULTILINE
#
#
# Остальные шаблоны
#  - \r carriage return или CR, символ Юникода U+240D.
#  - \t Tab символ
#  - \0 null, символ Юникода U+2400.
#  - \v	Вертикальный пробел в Юникоде
#  - \xYY 8-битный символ с заданным шестнадцатеричным значением. Таблица юникода Например \x2A находит символ *.
#  - \ddd	8-битный символ с заданным восьмеричным значением. Таблица UTF-8 Например \052 находит символ *.
#  - [\b] Символ backspace или BS. В скобках, т.к. \b уже занято другим спецсимволом.
#  - \f Символ разрыва страницы.


# Вариации использования
#  - $
# r'[A$Z]'  # Ищет символы A,$,Z
# r'^text$' # Ищет text между началом и концом строки
# r'100\$'  # Ищет 100$
#
#  - ^
# r"[^abc]"      # Ищет любой символ, кроме a,b,c
# r"^Some text$" # Ищет Some text между началом и концом строки
# r"\^"          # Ищет символ ^
# r"[a^bc]"      # Символ ^ не стоит первым в скобках, поэтому выражение ищет символы a,b,c,^
#
#  - .
# r'[A.Z]'     # Ищет символы A,.,Z
# r'text.'     # Ищет text с любым символом, кроме перехода на новую строку
# r'1\.000\$'  # Ищет 1.000$
#
#  - -
# r'Как-то так' # Ищет Как-то так
# r'[+-]'       # Ищет символы +,-
# r'[^-+]'      # Ищет любой символ, кроме +, -
# r'[a-z]'      # Ищет все буквы латинского алфавита в нижнем регистре
# r'[a\-z]'     # Ищет символы a,-,z
#
#  - []
# r'[abc]'   # Ищет символы a,b,c
# r'\[abc\]' # Ищет [abc]
# r'[\[abc\]]' # Ищет символы [,a,b,c,]
#
# Не все шаблоны в квадратных скобках используются как текстовые символы:
# r'[.]'  # Находит точку
# r'[\d]' # То же самое, что и \d


# \b и \B
# являются "пустыми" и не занимают места в тексте,
# они являются промежутком между символами, вследствие чего их невозможно увидеть
#
#  - \b
# Очень часто используется как граница слова или числа.
# Он стоит между \w и \W и не зависит от того, в каком порядке они расположены:
# он будет как между \w\W, так и между \W\w.
#
# Представим, что у нас есть следующий текст и такое регулярное выражение:
# text = 'That wall was black'
# regex = r'\b\w\w\w\w\b' # ищем слово где в начале пробел 4 символа и пробел
# Регулярное выражение найдёт следующие последовательности:
# That, wall



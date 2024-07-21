# Если мы используем не известный тег то браузер просто его пропускает

# <!-- Это комментарий -->

# <!DOCTYPE html> используем стандарт HTML № 5

# <html> </html> начало и конец html документа

# <head> </head> начало и конец заголовка

# <title>Название вкладки в браузере</title>

# <meta charset="UTF-8">  кодировка

# <body> какойто текст </body> все что видит пользователь на экране

# <h1> <h2> ... до <h6> - теги заголовков
# <h1> используется при поиске поэтому должен содержать самую важную информацию
# у тегов заголовков имеется атрибут меняющий расположение (по умолчанию с лева)
# aling=
# left - выравнивание по левому краю
# right - выравнивание по правому краю
# center - выравнивание по центру
# justify - выравнивание по ширине страницы

# <p> </p> - тег абзаца (между строками добавляется отступ)
# имеется атрибут меняющий расположение (по умолчанию с лева)
# aling=
# left - выравнивание по левому краю
# right - выравнивание по правому краю
# center - выравнивание по центру
# justify - выравнивание по ширине страницы

#<br> перевод на новую строку (Строки попорядку)

# если в абзацце задать aling то все строки внутри абзаца
# будут выравненны согласно aling абзацца
# <p align="center">Я ужин отдаю врагу!
# <br>Но чай не выпить - не могу.
# <br>К нему печенька, мармеладка-
# <br>Теперь усну, пожалуй, сладко...</p>

# Для подключения картинки используется тег
# <img>

# <img src="images/rec_img.jpg"> - путь от куда берем изображение
# Данный путь чаще всего используется на практике

# <img src="http://mysite.ru/images/rec_img.jpg"> - ПОЛНЫЙ путь от куда берем изображение
# позволяет обращаться к ресурсам сайта вне зависимости положения
# плох тем что имеем привязку к домену

# Имеет следующие 1 Атрибуты:
# src="URL" - Адрес загружаемого рисунка
# aling="botton | left | middle | top" - способ выравнивания изображения в документе

# alt="текст" - Альтернативное описание изображения
# отображается при не удачной загрузке изображения

# title="текст" - описание изображения появляется при наведении мыши

# border="толщина рамки" - устанавливает толщину рамки вокруг изображения
# Что бы убрать рамку нужно поставить значение 0

# height="высота" - высота рисунка при отображении в пиксилях или %

# width="ширина" - ширина рисунка при отображении в пиксилях или %

# hspace="отступ по горизантали" - задает величину отступа по горизонтали

# vspace="отступ по вертикали" - задает величину отступа по вертикали


# <img> - строковый элемент HTML - документа
# <h1> и <p> - блоковые элементы

# Блоковые элементы:
# - Занимают всю доступную ширину
# - Высота зависит от содиржимого
# - каждый новый элемент занимает новую строку
# - могут вкладываться в другие блочные элементы
# - Не могут быть вложенны в строковые элементы

# Строковые элементы:
# - Ширина зависит от содержимого + поле и отступы
# - высота зависит от содержимого
# - Могут отображаться в строчку
# - Могут вкладываться и в блоковые и в строковые элементы

# <b> </b> - выделение фрагмента полужирным
# <u> </u> - подчеркивание фрагмента
# <i> </i> - наклонный шрифт

# <sup> </sup> - сдвигаем фрагмент текста вверх (степень) (x2 + y2 = R2)
# <sub> </sub> - сдвигаем фрагьент текста вниз (индекс) H2O

# <hr> рисует горизантальную черту
# align="center | left | right" - <hr aling=center> - способ выравнивания документа
# color="цвет" - <hr color="red"> - устанавливаем цвет линии
# Noshade - <hr noshade> - отменяет трехмерный эффект при рисовании линии
# size="число" - <hr size=1> - устанавливает толщину линии по умолчанию 2
# width="число" - <hr width="50%"> - любое допустимое значение в пикселах или процентах



# <ul> - создание списка с фигурами
# СПИСКИ МОЖНО ВКЛАДЫВАТЬ В СПИСКИ
# <li> - позиция списка
# <ul>
#     <li><u>Банан крупный</u> - 0,5 шт. (или 1 маленький)
# </ul>
# type =
# disk - закрашенные кружочки (по умолчанию)
# circle - не закрашенные кружочки
# square - закрашенные квадратики

# <ol> - создание нумерованного списка
# <ol>
#     <li><p>Подготавливаем ингредиенты для пудинга с бананом.
#         Банан возьмем перезревший.
#         <p>Также подготовьте маленькую жаростойкую форму для выпекания.
#         Включаем духовку заранее что бы она хорошо прогрелась.
# </ol>
#
# в <li value=10> можно задават значение
# следующие элементы списка будут прономерованны исходя из данного значения
#
# type=A - прописные латинские буквы
# type=a - строчные латинские буквы
# type=I - большие римские цифры
# type=i - малые римские цифры
# type=1 - арабские цифры (по умолчанию)
# start=5 - начало нумерации


# Добавить ссылку
# если ссылка ведет на внешние ресурсы то указываем полный путь
# если ссылка ведет на внутренние то указываем короткий путь
# <a>анкор ссылки </a>
# анкор ссылки это как будет отображаться ссылка в браузере
# <p>Пример<a href="mypage.html">ссылки<\a> в HTML документе
# в браузере отоброзиться Пример ссылка в HTML документе

#так же в качестве анкора можно использовать изображение
# <p>Пример<a href="mypage.html"><img src=/images/strelk.jpg>><\a> в HTML документе

# можно создать ссылку на определенное место HTML документа
# для перехода нужно создать маркер
# <a name="имя маркера"></a>
# или
# <a name="also"></a>
# чаще используют
# <h3 id="also">Читайте так же </h3>   (записали в id имя по которому будем далее обращаться)
# далее для перехода на определенный маркер
# <a href="#also">Что еще почитать?</a>

# target="_blank открыть сайт в новой вкладке
# target="_self открыть сайт в этой же вкладке (по умолчанию)
# <a href="https://vk.com/" target="_blank">

# <div> - позволяет разбить страницу на блоки
# <span> - тег текстового уровня не может содержать дугие блоки применяется к фрагментам текста



# Таблицы <table>
# разбивка на ячейки
# <tr> строка
# <tb> ячейка

# 1 Атрибуты <table>
# align="left | center | right" - выравнивание таблицы и отикание ее другими элементами
# background="URL" - фон таблицы
# bgcolor="цвет" - цветфона задается как red, blue и т.д. или в шестнадцетеричном формате #RRGGBB
# border=1 размер толщины рамки
# cellpadding="число" - растояние в пикселях между границей ячейки и ее содержимым
# cellspacing="число" - растояние в пикселях между рамками ячеек по горизонтали и вертикали
# width="значение%" - определяет желаемую ширину таблицы в % или пикселях по отношению к окун браузера

# 1 Атрибуты <tr> и <tb>
# align="left | center | right" - выравнивание содержимого в строке или ячейки
# background="URL" - фон строки или ячейки
# bgcolor="цвет" - цветфона задается как red, blue и т.д. или в шестнадцетеричном формате #RRGGBB
# width="значение%" - определяет желаемую ширину строки или ячейки в % или пикселях по отношению к окун браузера
# valign="top | middle | bottom" - выравнивает по вертикали (верх, середина, низ)

# 1 Атрибуты <tb>
# colspan - обьеденение ячеек по горизонтали
# rowspan - обьеденение ячеек по вертикали


# Фреймы позволяют разбить окно браузера на несколько прямоугольных областей
# расположенных рядом друг с другом
# в каждой области свой HTML документ
# при необходимости можно организовать взаимодействие между фреймоми

# при создании HTML документа вместо <body>
# прописываем <frameset> УСТАРЕЛО!!!!
# 1 Атрибуты
# cols="ширина ячейки 1, ширина ячейки 2"
# <frameset cols="20%, 80%"> - задали размеры двух полей в окне браузера
# <frameset cols="20%, *"> - звездочка означает все остальное пространство


# GET и POST запросы
# файл contact

#  поля ввода, кнопки, списки

# <input type="нужная форма"> (см.register)
# text - пустое поле ввода
# button - кнопка ввода
# сheckbox - Флажок (квадрат с галочкой)
# radio - переключатели выбрать круглешек из разных вариантов
# password - поле ввода пароля (знаки не видно только снежинки)
# hidden- скрытое поле
# reset - сброс данных формы (удаляет содержимое формы)
# submit - отправить данные серверу

# так же к input добавляеться
# value="значение" (без текста по умолчанию)
# size="10" - число длина поля
# name="fio" - данные при отправки на сервер что бы он понимал какая информация пришла


#<select> выпадающие списки или списки
# name="fio" - данные при отправки на сервер что бы он понимал какая информация пришла
# size="10" - число отображаемых строк списка, если >1 то список не выпадающий
# multiple - позволяет выбирать несколько элементов списка

# <textarea>
# cols - ширина поля в символах
# rows - высота поля в символах
# name="fio" - данные при отправки на сервер что бы он понимал какая информация пришла
# maxlength - максимальное число вводимых символов


#каскадные таблицы стилей, начало CSS
# что бы использовать css в html в заголовке
# указываем путь к css файлу в котором прописанна вся визуальная
# настройка страницы
# <link type="text/css" href="css/style.css" rel="stylesheet">

# можно импортитровать один css в другой
# @import url("/css/main.css");

# html, body {    # теги к которому будет применен стиль
#     margin: 0;  # отступы между элементами таблицы (div) в пикселях
#     padding: 0; # растояние (внутри блока) между содержимым и краем таблицы (по центру)
#     fonts-family: Arial, Tahoma; # шрифт
#     color: #444;                #цвет шрифта
# }

# h1 {
#     fonts-size: 20px;       # размер шрифта для заголовка
#     margin: 0 0 20px 0;    # отступ со все сторон
#     padding-bottom: 10px;  # создает зазор между заголовком и нижней границей блока
#     border-bottom: 1px solid #ccc; # Толщина, тип линии, цвет
# }

# #reg_form {  # так как div блоков много обратились по id
#     width: 350px; # ширина тега div
#     margin: 20px auto 0 auto;  # отступ со все сторон
#     padding: 10px; # растояние (внутри блока) между содержимым и краем таблицы (по центру)
#     background: #fff; # цвет фона
#     box-shadow: 5px 5px 10px #aaa; # тень от блока
# }

# .reg_list {  # для определения класса ставиться точка (класс в отличии от id может использоваться многократно)
#     list-style: none; # маркеры списка
#     padding: 0; # растояние (внутри блока) между содержимым и краем таблицы (по центру)
#     margin: 0;  # отступ со все сторон
# }

# .reg_list li{  # в нутри тега где подключенн данный класс нужно взять все теги li
#     margin: 10px 0 10px 0; # и к ним применить данное свойство
# }

# .reg_title {
#     display: inline-block;  # следует отображать как блоковый но разрешает отображать другие элементы
#     min-width: 100px;       # Минимальная ширина блока
# }

# input .reg_input {
#     width: 230px;  # ширина тега div
#     border: none; # рамки
#     border-bottom: 1px solid #aaa; # Толщина, тип линии, цвет
#     fonts-size: 16px;  # размер шрифта
# }

# input.reg_input:focus {  # псевдо класс применяется только ьогда когда элемент находиться в фокусе
#     border-bottom: 1px solid #FFDB4D;
# }


# Единицы измерения CSS

# Относительные - меняются под экран или окно браузера
# em - высота шоифта элемента
# ex - высота буквы X
# px - пиксель
# % - процент

# Абсолютные - на всех экранах одинаковые
# in - дюйм (2.54 см)
# cm - сантиметр
# mm - милиметр
# pt - пункт (1/72 in)
# pc - пика (12 pt)




print(*reversed([input() for _ in range(3)]), sep='\n')






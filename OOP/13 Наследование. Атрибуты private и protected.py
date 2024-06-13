# Наследование. Атрибуты private и protected

# public
# attribute(без одного или двух подчеркиваний) публичное свойство public

# protected
# _attribute(с одним подчеркиванием) режим доступа protected
# служит для обращения внутри класса и во всех дочерних классах
# не запрещает обращаться из вне
# то есть из любого места можем обратиться экземпляр класса._attribute

# private
# __attribute(c двумя подчеркиваниниями) режим доступа private
# служит для обращения внутри класса
# если в родителе 1 Атрибуты private
# мы можем инициализировать их через super()__init__
# НО МЫ НЕ МОЖЕМ обратиться к ним через ребенка
# ПОЭТОМУ ПРОПИСЫВАЕМ СЕТОРЫ И ГЕТОРЫ


# если приватные 1 Атрибуты создавать через дескриптор и проперти - наследуются как и обычные.
# единственный вариант иметь в дочернем классе аналогичный приватный атрибут как в базовом
# - во всех трех случаях создания приватных атрибутов - переопределять саму инициализацию этих атрибутов,
# т.е. либо прописывать их от руки заново, либо копировать проперти из базового класса в дочерний,
# либо повторять привязку к дескриптору в дочернем классе.
# кстати, если у нас один базовый класс даже с одним приватным атрибутом и множество дочерних,
# у которых мы хотим наличие аналогичного приватного атрибута -
# в таком ключе дескриптор будет выгоднее проперти, т.к.
# для каждого нового дочернего класса мы перепишем только одну строчку, а не целый объект-свойство
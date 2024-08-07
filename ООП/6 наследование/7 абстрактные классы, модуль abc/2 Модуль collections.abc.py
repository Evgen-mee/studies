# Модуль collections.abc предоставляет абстрактные базовые классы,
# которые можно использовать для проверки того, реализует объект тот или иной интерфейс или нет.

# Mixin методы представляют собой методы, которые автоматически реализуются на основе абстрактных методов.

# Стоит наследоваться тогда когда нужно поменять основной функионал встроенного типа
# Если изменения не большие то стоит наследоваться от базового класса

# Таким образом, некоторый объект реализует интерфейс:
# Iterable, если он содержит метод __iter__()
# Iterator, если он содержит методы __next__() и __iter__()
# Collection, если он содержит методы __contains__(), __iter__() и __len__()
# Sequence, если он содержит методы __getitem__(), __len__(), __contains__(), __iter__(), __reversed__(), index() и count()
# Mapping, если он содержит методы __getitem__(), __iter__(), __len__(), __contains__(), keys(), items(), values(), get(), __eq__() и __ne__()
# и т.д.

# С помощью типов из данного модуля и функций isinstance() и issubclass()
# можно проверить, например, является ли объект итерируемым, или реализует ли класс протокол последовательности

 # - Iterable - можно ли итерироваться?
 #
 # - Iterator - является ли итератором?
 #
 # - Reversible - можно ли применить reversed?
 #
 # - Collection - является ли коллекцией?
 #
 # - Sequence - является ли последовательностью?
 #
 # - MutableSequence - является ли изменяющейся последовательностью?
 #
 # - Mapping - является ли словарем?
 #
 # - MutableMapping - является ли изменяющимся словарем?


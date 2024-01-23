# В Python 3.10 вместо записи Union[X, Y] можно писать X | Y
# - Union
# когда нужно объединить несколько типов
# чтобы указать, что функция может принимать и целые и вещественные числа

#  - аргументы указываемые в квадратных скобках должны быть типами,
# причем необходимо указать хотя бы один тип
#  - запись Union[Union[int, str], float] эквивалентна записи Union[int, str, float]
#  - запись Union[int] эквивалентна записи int
#  - запись Union[int, str, int] эквивалентна записи Union[int, str]
#  - запись Union[int, str] эквивалентна записи Union[str, int]

#
# что бы сократить:
# from typing import Union
# def add_or_concatenate(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str]:
#     return a + b
#
# Делаем так:
# from typing import Union
# NumberOrStr = Union[int, float, str] #добавили переменную с типами
# def add_or_concatenate(a: NumberOrStr, b: NumberOrStr) -> NumberOrStr:
#     return a + b


#  - Optional
# Возвращает определенные типы или None
# from typing import Optional
# name: Optional[str]    # str или None
#
# name: Union[str, None] и name: Optional[str] это одно и то же,
# но второй вариант читается проще

#
#  - Any
# абсолютно что угодно
# from typing import Any
# def func(arg: Any) -> Any:
#     return arg
#
#  - NoReturn
# указывает, что функция никогда не возвращает значение
# from typing import NoReturn
# def stop() -> NoReturn:
#     raise RuntimeError('no way')
#
# - Callable
# указываем что возвращаем функцию
# from typing import Callable
# def do_something() -> Callable:
#     pass
#
# аннотировать *args и **kwargs
# def foo(*args: str, **kwds: int):
#lambda

from typing import Callable


def fun(c: Callable):
    print(type(c))
    x = c()
    print(type(x))


class myclass():
    pass

fun(myclass)




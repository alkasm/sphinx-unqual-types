import typing
from bar import Bar
from numpy.polynomial import polynomial


def make_bar() -> Bar:
    return Bar()


def multiply_polynomial(
    p: polynomial.Polynomial, value: int
) -> typing.Tuple[polynomial.Polynomial, polynomial.Polynomial]:
    return p, polynomial.Polynomial(*(value * p.coef))

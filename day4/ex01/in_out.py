def square(x: int | float) -> int | float:
    "Function that returns the square of an argument"

    return x ** 2


def pow(x: int | float) -> int | float:
    "function that returns the power of an argument by himself"

    return x ** x


def outer(x: int | float, function) -> object:
    """
    Function that takes as argument a number and a function, it returns an
    object that when called returns the result of the arguments calculation
    """
    def inner() -> float:
        "Execute the provided function, update value, and return the result"

        nonlocal x
        res = function(x)
        x = res
        return res
    return inner

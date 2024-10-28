def callLimit(limit: int):
    """
    Takes an integer and returns a decorator that restricts
    number of times a decorated function can be called
    """
    count = 0

    def callLimiter(function):
        "Takes the function to be decorated and returns the wrapped function"

        def limit_function(*args: any, **kwds: any):
            "Tests if count is > to limit and raise an exception if needed"

            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function
    return callLimiter

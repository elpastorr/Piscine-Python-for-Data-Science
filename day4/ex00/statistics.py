def get_mean(args) -> float:
    "Function that returns the mean of a list"

    return sum(args) / len(args)


def get_median(args) -> float:
    "Function that returns the median of a list"

    args_len = len(args)
    if args_len % 2 == 0:
        arg1 = args[int((args_len - 2) / 2)]
        arg2 = args[int(args_len / 2)]
        return (arg1 + arg2) / 2
    return args[int((args_len - 1) / 2)]


def get_quartile(args) -> list:
    "Function that returns the quartiles of a list"

    q1_index = len(args) // 4
    q3_index = (len(args) * 3) // 4
    return [float(args[q1_index]), float(args[q3_index])]


def get_std(args) -> float:
    "Function that returns the standard deviation of a list"

    mean = get_mean(args)
    tmp = 0
    for i in args:
        tmp += (i - mean) ** 2
    return (tmp / len(args)) ** 0.5


def get_var(args) -> float:
    "Function that returns the variance of a list"

    mean = get_mean(args)
    tmp = 0
    for i in args:
        tmp += (i - mean) ** 2
    return tmp / len(args)


def ft_statistics(*args: any, **kwargs: any) -> None:
    "Function that calculates various statistical measures"

    if len(args) == 0:
        for value in kwargs.items():
            print("ERROR")
        return

    case = {"mean": get_mean, "median": get_median, "quartile": get_quartile,
            "std": get_std, "var": get_var}

    for value in kwargs.items():
        if value[1] in case:
            print(value[1], ":", case[value[1]](sorted(args)))

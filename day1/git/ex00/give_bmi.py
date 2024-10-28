def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    try:
        if len(height) == 0 or len(weight) == 0:
            raise Exception("Error: empty list")
        if len(height) != len(weight):
            raise Exception("Error: list are not the same size")
        for i in range(len(height)):
            if not isinstance(height[i], int):
                if not isinstance(height[i], float):
                    raise Exception("Error: list are not all float or int")
            if not isinstance(weight[i], int):
                if not isinstance(weight[i], float):
                    raise Exception("Error: list are not all float or int")
    except Exception as error:
        print(error)
        exit(0)
    bmi = []
    try:
        for i in range(len(height)):
            if (height[i] == 0):
                raise Exception("Error: height is 0")
            bmi.append(weight[i] / (height[i] * height[i]))
    except Exception as error:
        print(error)
        exit(0)
    return bmi


give_bmi.__doc__ = "A function that returns a list of BMI values"


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if len(bmi) == 0:
            raise Exception("Error: empty list")
        for i in range(len(bmi)):
            if not isinstance(bmi[i], int) and not isinstance(bmi[i], float):
                raise Exception("Error: list is not all float or int")
    except Exception as error:
        print(error)
        exit(0)
    output = []
    for i in range(len(bmi)):
        output.append(bmi[i] > limit)
    return output


apply_limit.__doc__ = "A function returns a list of booleans \
True if bmi value is above the limit"

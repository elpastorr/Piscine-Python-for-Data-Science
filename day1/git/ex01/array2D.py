def slice_me(family: list, start: int, end: int) -> list:
    try:
        if len(family) == 0:
            raise Exception("Error: empty array")
        if not isinstance(family, list):
            raise Exception("Error: family is not a array")
        if not isinstance(family[0], list):
            raise Exception("Error: family is not a 2D array")
        prev_elem = -42
        for i in range(len(family)):
            if prev_elem != -42 and len(family[i]) != prev_elem:
                raise Exception("Error: array elements are not the same size")
            prev_elem = len(family[i])
    except Exception as error:
        print(error)
        return [0]

    print(f"My shape is : ({len(family)}, {len(family[0])})")

    new_family = []
    if end <= start:
        new_family.append(family[start])
    else:
        for i in range(start, end):
            new_family.append(family[i])

    print(f"My new shape is : ({len(new_family)}, {len(new_family[0])})")

    return new_family

    slice_me.__doc__ = "A function that takes a 2D array, prints its shape,\
and returns a truncated version of the array based on start and end"

def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
    elif type(object) is float:
        print("Cheese:", object, type(object))
    elif type(object) is int:
        print("Zero:", object, type(object))
    elif object == '':
        print("Empty:", type(object))
    elif type(object) is bool:
        print("Fake:", object, type(object))
    else:
        print("Type not Found")
        return 1
    return 0

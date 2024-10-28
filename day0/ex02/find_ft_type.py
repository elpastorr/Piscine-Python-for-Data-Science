def all_thing_is_obj(object: any) -> int:
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    type_names = type_names.get(type(object), "Type not found")

    if type(object) is str:
        print(object, "is in the kitchen :", type(object))
    elif type_names == "Type not found":
        print(type_names)
    else:
        print(type_names, ":", type(object))
    return 42

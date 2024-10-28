class calculator:
    "calculator class for performing operations between a vector and a object"

    def __init__(self, vector):
        "Init calculator class"

        self.vector = vector

    def __add__(self, object) -> None:
        "Methode to '+' each element of vector to object"

        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __mul__(self, object) -> None:
        "Methode to '*' each element of vector to object"

        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __sub__(self, object) -> None:
        "Methode to '-' each element of vector to object"

        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __truediv__(self, object) -> None:
        "Methode to '/' each element of vector to object"
        try:
            if object == 0:
                raise ZeroDivisionError("Error: division by zero")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
            return [x for x in self.vector]
        except ZeroDivisionError as error:
            print(error)

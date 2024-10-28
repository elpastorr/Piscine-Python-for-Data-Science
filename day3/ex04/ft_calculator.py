class calculator:
    "calculator class for performing operations between two vectors"

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        "methode to '*' 2 vectors"

        dot_prod = 0
        for i in V1:
            dot_prod += i * V2[V1.index(i)]
        print("Dot product is :", dot_prod)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        "methode to '+' 2 vectors"

        new_vec = []
        for i in V1:
            new_vec.append(i + V2[V1.index(i)])
        print("Add Vector is :", new_vec)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        "methode to '-' 2 vectors"

        new_vec = []
        for i in V1:
            new_vec.append(i - V2[V1.index(i)])
        print("Sous Vector is:", new_vec)

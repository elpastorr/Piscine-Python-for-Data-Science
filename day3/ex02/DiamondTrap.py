from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    "Class representing a monster"

    def __init__(self, first_name, is_alive=True):
        "Method to init King class"

        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        "Method to change eyes parameter"

        self.eyes = eyes

    def set_hairs(self, hairs):
        "Method to change hairs parameter"

        self.hairs = hairs

    def get_eyes(self):
        "Method to get eyes"

        return self.eyes

    def get_hairs(self):
        "Method to get hairs"

        return self.hairs

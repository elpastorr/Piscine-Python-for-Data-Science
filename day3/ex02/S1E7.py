from S1E9 import Character


class Baratheon(Character):
    "Class representing a Baratheon character"

    def __init__(self, first_name, is_alive=True):
        "Method to init Baratheon class"

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        "Method to change state of is_alive"

        self.is_alive = False


class Lannister(Character):
    "Class representing a Lannister character"

    def __init__(self, first_name, is_alive=True):
        "Method to init Lannister class"

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        "Method to change state of is_alive"

        self.is_alive = False

    @classmethod
    def create_lannister(self, first_name, is_alive):
        "Method to create a Lannister"

        new_lannister = self(first_name)
        new_lannister.is_alive = is_alive
        return new_lannister

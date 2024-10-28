from abc import ABC, abstractmethod


class Character(ABC):
    "Abstract class representing a character"

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        "Method to init Character class"

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        "Method to change state of is_alive (defined in Stark class)"

        pass

    def __str__(self):
        "Method to return a string representation of the character"

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        "Method to return a string representation of the character"

        return self.__str__()


class Stark(Character):
    "Class representing a Stark character"

    def __init__(self, first_name, is_alive=True):
        "Method to init Stark class"

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        "Method to change state of is_alive"

        self.is_alive = False

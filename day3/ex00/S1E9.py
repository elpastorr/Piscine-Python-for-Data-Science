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


class Stark(Character):
    "Class representing a Stark character"

    def __init__(self, first_name, is_alive=True):
        "Method to init Stark class"

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        "Method to change state of is_alive"

        self.is_alive = False

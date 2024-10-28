from S1E7 import Baratheon, Lannister


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    J = Lannister.create_lannister("Jaine", True)
    print(f"Name : {J.first_name, type(J).__name__}, Alive : {J.is_alive}")


if __name__ == "__main__":
    main()

main.__doc__ = "A program that tests new Baratheon and Lannister classes"

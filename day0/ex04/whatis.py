import sys


def main():
    if len(sys.argv) == 1:
        exit(0)

    try:
        if len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided")
    except AssertionError as error:
        print("AssertionError:", error)
        exit(0)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit(0)

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()

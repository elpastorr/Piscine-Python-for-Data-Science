import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
    except AssertionError as error:
        print("AssertionError:", error)
        exit(0)
    try:
        string = str(sys.argv[1])
        num = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        exit(0)
    filtered = list(ft_filter(lambda word: len(word) > num, string.split()))
    print(filtered)


main.__doc__ = "A program that filters words from the length provided"

if __name__ == "__main__":
    main()

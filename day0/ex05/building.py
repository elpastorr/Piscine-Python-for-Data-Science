import sys
import string


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("More than one argument is provided")
    except AssertionError as error:
        print("AssertionError:", error)
        exit(0)
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    else:
        text = sys.argv[1]
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punct += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1
    print("The text contains", len(text), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punct, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")


main.__doc__ = "A program that takes a string argument and displays its length\
 upper-case, lower-case, punctuation, digits and spaces."


if __name__ == "__main__":
    main()

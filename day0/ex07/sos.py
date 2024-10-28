import sys


def main():
    morse_dict = {
        " ": "/", "A": ".-", "B": "-...", "C": "-.-", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-",
        "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----",
        "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----."
    }

    try:
        if len(sys.argv) != 2 or len(sys.argv[1]) == 0 \
                or not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")
    except AssertionError as error:
        print("AssertionError:", error)
        exit(0)

    text = sys.argv[1]
    morse_text = []

    try:
        for char in text.upper():
            if char in morse_dict:
                morse_text.append(morse_dict[char])
            else:
                raise AssertionError("the arguments are bad")
    except AssertionError as error:
        print("AssertionError:", error)
        exit(0)
    print(" ".join(morse_text))


main.__doc__ = "A program that takes a string and encodes it into Morse Code"

if __name__ == "__main__":
    main()

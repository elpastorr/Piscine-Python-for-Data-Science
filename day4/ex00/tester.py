from statistics import ft_statistics


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tu="median", ta="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejf="heheh", ejd="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()

main.__doc__ = "A program that tests ft_statistics"

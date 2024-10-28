from load_csv import load


def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()


main.__doc__ = "A program that run load and print his result"

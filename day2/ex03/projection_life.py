from load_csv import load
import matplotlib.pyplot as plt


def clean_income(income):
    if income.endswith('k'):
        return float(income[:-1]) * 1e3
    return float(income)


clean_income.__doc__ = "A function that transforms income data to get\
 it all at same range"


def main():
    norm = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    income_data = load(norm)
    life_data = load("life_expectancy_years.csv")
    inc_1900 = income_data['1900']
    life_1900 = life_data['1900']

    plt.scatter(inc_1900, life_1900)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])

    plt.show()


if __name__ == "__main__":
    main()


main.__doc__ = "A program that displays the projection of life expectancy in \
relation to the gross national product of the year 1900 for each country"

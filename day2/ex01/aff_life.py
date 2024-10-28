from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("life_expectancy_years.csv")
    france_data = data[data['country'] == 'France']
    years = france_data.columns[1:]
    life_expect = france_data.values[0][1:]

    plt.plot(years, life_expect)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(years[::40])
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()


main.__doc__ = "A program that loads life_expectancy_years.csv, and displays a\
 country information"

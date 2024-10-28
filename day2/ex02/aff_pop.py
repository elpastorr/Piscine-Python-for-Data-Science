from load_csv import load
import matplotlib.pyplot as plt


def clean_population(pop):
    if pop.endswith('k'):
        return float(pop[:-1]) * 1e3
    if pop.endswith('M'):
        return float(pop[:-1]) * 1e6
    if pop.endswith('B'):
        return float(pop[:-1]) * 1e9
    return float(pop)


clean_population.__doc__ = "A function that transforms population data to get\
 it all at same range"


def main():
    data = load("population_total.csv")

    fra_data = data[data['country'] == 'France']
    bel_data = data[data['country'] == 'Belgium']
    ita_data = data[data['country'] == 'Italy']

    years = fra_data.columns[1:]

    fra_population = fra_data.values[0][1:]
    bel_population = bel_data.values[0][1:]
    ita_population = ita_data.values[0][1:]

    fra_pop = [clean_population(pop) for pop in fra_population]
    bel_pop = [clean_population(pop) for pop in bel_population]
    ita_pop = [clean_population(pop) for pop in ita_population]

    years = years[:-50]
    fra_pop = fra_pop[:-50]
    bel_pop = bel_pop[:-50]
    ita_pop = ita_pop[:-50]

    plt.plot(years, fra_pop, label="France")
    plt.plot(years, bel_pop, label="Belgium")
    plt.plot(years, ita_pop, label="Italy")

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.xticks(years[::40])
    plt.yticks([2 * 1e7, 4 * 1e7, 6 * 1e7], ["20M", "40M", "60M"])

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()


main.__doc__ = "A program that loads population_total.csv, and displays a\
 country information vs another one"

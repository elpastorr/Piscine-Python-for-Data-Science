from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    print("My ft_tqdm:")
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    print("Original tqdm:")
    for elem in tqdm(range(333)):
        sleep(0.005)


main.__doc__ = "A program that test ft_tqdm"


if __name__ == "__main__":
    main()

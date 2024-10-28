from ft_filter import ft_filter


def is_vowel(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


def is_multiple_of_3(num):
    return num % 3 == 0


def main():
    print("TEST 1")
    sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
    filtered0 = filter(is_vowel, sequence)
    filtered1 = ft_filter(is_vowel, sequence)
    print('The filtered letters are:')
    for c in filtered0:
        print(c)
    print("-----------")
    for c in filtered1:
        print(c)

    print("TEST 2")
    seq = [0, 1, 2, 3, 5, 8, 13]
    result0 = filter(lambda x: x % 2 != 0, seq)
    result1 = ft_filter(lambda x: x % 2 != 0, seq)
    print(list(result0))
    print(list(result1))
    result0 = filter(lambda x: x % 2 == 0, seq)
    result1 = ft_filter(lambda x: x % 2 == 0, seq)
    print(list(result0))
    print(list(result1))

    print("TEST 3")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result0 = list(filter(lambda x: is_multiple_of_3(x), numbers))
    result1 = list(ft_filter(lambda x: is_multiple_of_3(x), numbers))
    print(result0)
    print(result1)


if __name__ == "__main__":
    main()

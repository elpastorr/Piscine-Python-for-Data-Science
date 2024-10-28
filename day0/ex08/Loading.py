import shutil


def ft_tqdm(lst: range) -> None:
    percent = 0
    total = len(lst)
    term_length = shutil.get_terminal_size().columns + len(str(total) * 2) - 46

    spaces = " " * term_length
    for i in lst:
        yield i
        percent = '{:3.0f}'.format(i / total * 100)
        loading = spaces.replace(' ', '█', round(i / total * term_length))
        print(f"{percent}%|{loading}| \
{i + 1:>{len(str(total))}}/{total}", end='\r')


ft_tqdm.__doc__ = "A function that reproduce the function tqdm"

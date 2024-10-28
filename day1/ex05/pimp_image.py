import numpy as np
from PIL import Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    image = 255 - array
    Image.fromarray(image).show()


ft_invert.__doc__ = "A function that inverts colors of an image"


def ft_red(array: np.ndarray) -> np.ndarray:
    red_only = array[:, :, 0]
    image = np.zeros_like(array)
    image[:, :, 0] = red_only
    Image.fromarray(image).show()


ft_red.__doc__ = "A function that transform an image into his red version"


def ft_green(array: np.ndarray) -> np.ndarray:
    green_only = array[:, :, 1]
    image = np.zeros_like(array)
    image[:, :, 1] = green_only
    Image.fromarray(image).show()


ft_green.__doc__ = "A function that transform an image into his green version"


def ft_blue(array: np.ndarray) -> np.ndarray:
    blue_only = array[:, :, 2]
    image = np.zeros_like(array)
    image[:, :, 2] = blue_only
    Image.fromarray(image).show()


ft_blue.__doc__ = "A function that transform an image into his blue version"


def ft_grey(array: np.ndarray) -> np.ndarray:
    grey_arr = np.zeros((len(array), len(array[0])), dtype=np.uint8)

    for i in range(len(array)):
        for j in range(len(array[i])):
            grey = array[i][j].mean()
            grey_arr[i][j] = grey
    Image.fromarray(grey_arr).show()


ft_grey.__doc__ = "A function that transform an image into his grey version"

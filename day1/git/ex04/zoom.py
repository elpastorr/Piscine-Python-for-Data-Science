import numpy as np


def print_zoom(img: np.ndarray):
    print(f"[[[{img[0][0][0]}]")
    print(f"[{img[0][0][1]}]")
    print(f"[{img[0][0][2]}]")
    print("...")
    print(f"[{img[len(img) - 1][len(img[len(img) - 1]) - 1][0]}]")
    print(f"[{img[len(img) - 1][len(img[len(img) - 1]) - 1][1]}]")
    print(f"[{img[len(img) - 1][len(img[len(img) - 1]) - 1][2]}]]]")


print_zoom.__doc__ = "A function that print information about a zoomed image"


def ft_zoom(image: np.ndarray, x: int, y: int, size: int):
    try:
        if not isinstance(image, np.ndarray):
            raise Exception("Error: image is not an array")
        if not isinstance(size, int):
            raise Exception("Error: size is not an int")
        if not isinstance(x, int) or not isinstance(y, int):
            raise Exception("Error: x or y is not an int")
        if x < 0 or x >= image.shape[0] or x + size > image.shape[0]:
            raise Exception("Error: invalid x value")
        if y < 0 or y >= image.shape[1] or y + size > image.shape[1]:
            raise Exception("Error: invalid y value")
    except Exception as error:
        print(error)
        exit()

    zoomed_img = image[x:x + size, y:y + size]
    return zoomed_img


ft_zoom.__doc__ = "A function that zoom a given image"

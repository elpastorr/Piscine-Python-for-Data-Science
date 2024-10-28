import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from load_image import ft_load


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


def main():
    path = "animal.jpeg"
    image = ft_load(path)
    print("The shape of image is:", image.shape)
    print(image)
    zoomed_img = ft_zoom(image, 100, 450, 400)

    zoomed_img = Image.fromarray(zoomed_img)
    zoomed_grey_img = zoomed_img.convert("L")
    zoomed_grey_img.show()
    zoomed_img.save("new_image.jpg")
    zoomed_img_arr = ft_load("new_image.jpg")
    print("\nNew shape after slicing:", zoomed_img_arr.shape)
    print_zoom(zoomed_img_arr)

    plt.imshow(zoomed_img_arr)
    plt.title("Zoomed Image")
    plt.axis('on')
    plt.show()


main.__doc__ = "A program that load the image 'animal.jpeg', print some \
information about it and display it after zooming"


if __name__ == "__main__":
    main()

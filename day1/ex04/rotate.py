import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from zoom import ft_zoom, print_zoom


def ft_transpose(img: np.ndarray):
    rotated_img = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rotated_img[i, j] = img[j, i]
    return rotated_img


ft_transpose.__doc__ = "A function that rotate an img by transposing the data"


def main():
    path = "animal.jpeg"
    image = ft_load(path)
    zoomed_img = ft_zoom(image, 100, 450, 400)
    print("The shape of image is:", zoomed_img.shape)
    print_zoom(zoomed_img)

    rotated_img = ft_transpose(zoomed_img)
    print("\nNew shape after Transpose:", rotated_img.shape)
    print(rotated_img)

    plt.imshow(rotated_img)
    plt.title("Zoomed Image")
    plt.axis('on')
    plt.show()


main.__doc__ = "A program that load the image 'animal.jpeg', print some \
information about it and display it after zooming"


if __name__ == "__main__":
    main()

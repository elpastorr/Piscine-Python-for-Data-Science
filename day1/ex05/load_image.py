import os
import numpy as np
from PIL import Image


def ft_load(path: str):
    try:
        if not isinstance(path, str):
            raise Exception("Error: path is not a string")
        if not path:
            raise Exception("Error: path is empty")
        if not path.endswith(".jpg") and not path.endswith(".jpeg"):
            raise Exception("Error: only jpg and jpeg format supported")
        if not os.path.exists(path):
            raise Exception("Error: file not found", path)

        image = Image.open(path)

        if image is None:
            raise Exception("Error: failed to laod image")

        image_arr = np.array(image)
        print("The shape of image is:", image_arr.shape)
        print(image_arr)

    except Exception as error:
        print(error)
        print("slt")
        exit()
    return image_arr


ft_load.__doc__ = "A function that loads an image, prints its format, and its \
pixels content in RGB format"

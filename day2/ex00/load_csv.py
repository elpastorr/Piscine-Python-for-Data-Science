import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        if not isinstance(path, str):
            raise Exception("Error: path is not a string")
        if not os.path.exists(path):
            raise Exception("Error: Invalid path")
        if not path.lower().endswith(".csv"):
            raise Exception("Error: data file is not a .csv")
    except Exception as error:
        print(error)
        return None
    data = pd.read_csv(path)
    print("Loading dataset of dimensions", data.shape)
    return data


load.__doc__ = "A function that writes the dimensions of the data set and \
returns it"

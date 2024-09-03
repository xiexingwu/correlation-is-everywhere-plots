import numpy as np


# QoL to attach data to attributes
class Data:
    pass


def readHistoricalCsv(filename):
    converters = {1: lambda price: float(price[1:])}
    y = np.genfromtxt(
        filename, delimiter=",", skip_header=1, usecols=(1, 2), converters=converters
    )

    d = Data()
    d.x = np.arange(y.shape[0])
    d.y1 = y[::-1, 0]  # raw data is reverse-chronological
    d.y2 = y[::-1, 1]
    return d


def centre(array):
    return array - array.mean()


def normalise(array):
    return centre(array) / np.std(array)


def corr(y1, y2):
    n = len(y1)
    y1 = centre(y1)
    y2 = centre(y2)
    return y1 * y2 / (n * np.std(y1) * np.std(y2))

import numpy as np
from PIL import Image

import utils

arr = utils.readImage("data/wally.png")
arr_fft = np.fft.fft2(arr, axes=(0, 1))

def firstNModes(arr_fft, n):
    f = arr_fft.copy()
    f[n:-n, :, :] = 0
    f[:, n:-n, :] = 0
    return np.fft.ifft2(f, axes=(0, 1)).real.astype(np.uint8)

modes = [10, 50, 200, 500]
for mode in modes:
    arr = firstNModes(arr_fft, mode)
    img = Image.fromarray(arr)
    img.save(f"plots/4_{mode}.png")

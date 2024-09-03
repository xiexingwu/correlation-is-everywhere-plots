import sys
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

import utils

wally = utils.grayscale(utils.readImage("data/wally.png"))
ref = utils.grayscale(utils.readImage("data/wally_ref.png"))

H, W = wally.shape
h, w = ref.shape

I, J = (W - w + 1, H - h + 1)

# To run the computation, which takes a couple mins:
#   python 3_wally.py --compute
if "--compute" in sys.argv:
    cc = np.zeros((J, I))
    for i in range(I):
        for j in range(J):
            cc[j, i] = sum(
                utils.corr(ref.flatten(), wally[j : j + h, i : i + w].flatten())
            )
            print(f"{j:04d}, {i:04d}", end="\r")

    cc = np.nan_to_num(cc, 0)
    np.save("data/cc.npy", cc, allow_pickle=False)  # binary dump

# Load and plot cross-correlation map
cc = np.load("data/cc.npy")
cc = (cc + 1) / 2  # scale from [-1,1] to [0, 1]
cc = 10**cc / 10  # simulate log scale
cc = np.round(cc * 255)  # scale to 8-bit color
img = Image.fromarray(cc).convert("RGB")
img.save("plots/3.png")


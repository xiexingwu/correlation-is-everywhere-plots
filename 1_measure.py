import matplotlib.pyplot as plt
import numpy as np

import utils

goog = utils.readHistoricalCsv("data/goog.csv")

# Data prep
n = 20
x = goog.x[-n:]
np.random.seed(6942069)

y = utils.centre(goog.y1[-n:])
y2 = y/2
y3 = -y
y4 = np.random.rand(n) * 10

# FIG 1 - signals
fig, ax = plt.subplots()

ax.set_xticks(np.arange(0, n, 2))
ax.set_ylim([-12.5, 12.5])

# FIG 2 - point-wise multiplication
fig2, ax2 = plt.subplots()
ax2.set_xticks(np.arange(0, n, 2))
ax2.set_ylim([-0.2, 0.2])

# 1 - Ref
ax.plot(x, y, 'k-')
fig.savefig('plots/1_1a.png', transparent=False, dpi=80, bbox_inches="tight")

ax2.plot(x, utils.corr(y, y), 'k-')
fig2.savefig('plots/1_1b.png', transparent=False, dpi=80, bbox_inches="tight")


# 2 - Scale down
ax.plot(x, y2, 'ro-')
fig.savefig('plots/1_2a.png', transparent=False, dpi=80, bbox_inches="tight")

ax2.plot(x, utils.corr(y, y2), 'ro-')
fig2.savefig('plots/1_2b.png', transparent=False, dpi=80, bbox_inches="tight")


# 3 - Invert
ax.plot(x, y3, 'bs-')
fig.savefig('plots/1_3a.png', transparent=False, dpi=80, bbox_inches="tight")

ax2.plot(x, utils.corr(y, y3), 'bs-')
fig2.savefig('plots/1_3b.png', transparent=False, dpi=80, bbox_inches="tight")

# 4 - Noise
ax.plot(x, y4, 'g^-')
fig.savefig('plots/1_4a.png', transparent=False, dpi=80, bbox_inches="tight")

ax2.plot(x, utils.corr(y, y4), 'g^-')
fig2.savefig('plots/1_4b.png', transparent=False, dpi=80, bbox_inches="tight")

with open("plots/1_4b.txt", "w") as f:
    corr = sum(utils.corr(y, y4))
    print(corr)
    f.write(f"{corr:.2f}\n")

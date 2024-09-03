import matplotlib.pyplot as plt
import numpy as np

import utils

goog = utils.readHistoricalCsv("data/goog.csv")
amzn = utils.readHistoricalCsv("data/amzn.csv")

# Data prep
N = len(goog.x)  # data len
Y = np.roll(amzn.y1, 15)  # Synthetic delay in data
i_st = N // 4
i_en = 3 * N // 4
n = i_en - i_st  # sample len

x = np.arange(n)
y0 = goog.y1[i_st:i_en]  # Reference line

max_dt = N // 4

# FIG 1 - signals
fig, ax = plt.subplots()

ax.set_xticks(np.arange(0, n, 10))
# ax.set_ylim([-12.5, 12.5])

# FIG 2 - Cross-correlation
fig2, ax2 = plt.subplots()

ax2.set_xlim([-10, 10])
ax2.set_xticks(np.concatenate((np.arange(0, -max_dt, -5), np.arange(0, max_dt, 5))))
ax2.set_ylim([-1, 1])

fig2.savefig("plots/2_0.png", transparent=False, dpi=80, bbox_inches="tight")


# 0 - Goog reference
ax.plot(x, y0, "k-")

# 1 - No shift
y = Y[i_st:i_en]
l1 = ax.plot(x, y, "ro-")
ax2.plot([0], [sum(utils.corr(y0, y))], "ro")

fig.savefig("plots/2_1a.png", transparent=False, dpi=80, bbox_inches="tight")
fig2.savefig("plots/2_1b.png", transparent=False, dpi=80, bbox_inches="tight")

# 2 - offset 2
dt = 5
y = Y[i_st + dt : i_en + dt]
l2 = ax.plot(x, y, "bs-")
ax2.plot([dt], [sum(utils.corr(y0, y))], "bs-")

for l in l1:
    l.set(alpha=0.2)
fig.savefig("plots/2_2a.png", transparent=False, dpi=80, bbox_inches="tight")
fig2.savefig("plots/2_2b.png", transparent=False, dpi=80, bbox_inches="tight")


# 3 - all offsets
t = np.arange(-max_dt, max_dt + 1)
cc = np.zeros(len(t))
for i, dt in enumerate(t):
    y = Y[i_st + dt : i_en + dt]
    cc[i] = sum(utils.corr(y0, y))
ax2.plot(t, cc, "k-")

for l in l2:
    l.set(alpha=0.2)
fig2.savefig("plots/2_3b.png", transparent=False, dpi=80, bbox_inches="tight")

# 4 - optimal offset
dt = 15
y = Y[i_st + dt : i_en + dt]
ax.plot(x, y, "g^-")
ax2.plot([dt], [sum(utils.corr(y0, y))], "g^-")


fig.savefig("plots/2_4a.png", transparent=False, dpi=80, bbox_inches="tight")
fig2.savefig("plots/2_4b.png", transparent=False, dpi=80, bbox_inches="tight")

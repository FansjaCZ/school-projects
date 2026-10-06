import matplotlib.pyplot as plt
import math
import numpy as np

from model import calculate

# Matplotlib graph
fig, ax = plt.subplots()

ax.set_title(label="Afgelegde afstand tegen de tijd")
ax.set_xlabel("tijd (s)")
ax.set_ylabel("afstand (m)")

# lijnen maken
angle10 = calculate(10, 1)
angle20 = calculate(20, 1)
angle30 = calculate(30, 1)
ax.plot(angle10["Time"],angle10["Distance"], linewidth=2, label="10 graden")
ax.plot(angle20["Time"],angle20["Distance"], linewidth=2, label="20 graden")
ax.plot(angle30["Time"],angle30["Distance"], linewidth=2, label="30 graden")
ax.legend()

# stipjesss
scatterDistance = [0.2,0.4,0.6,0.8,1.0]
ax.scatter([0.56,0.79,0.98,1.14,1.28],scatterDistance, c="tab:blue")
ax.scatter([0.38,0.56,0.70,0.80,0.90],scatterDistance, c="tab:orange")
ax.scatter([0.34,0.49,0.60,0.67,0.76],scatterDistance, c="tab:green")

# manual text toevoegen
# ax.text(1.12,0.85,"10 graden")
# ax.text(0.82,0.85,"20 graden")
# ax.text(0.52,0.85,"30 graden")

# een grid en increment van grafiekje veranderen
maximumTime = max(angle10["TotalTime"], angle20["TotalTime"], angle30["TotalTime"])

ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

totalt = maximumTime+0.1
total = 1 + 0.1
inct = math.floor(maximumTime)/10
inc = math.floor(1)/10
ax.set_xticks(np.arange(inct, totalt, inct))
ax.set_yticks(np.arange(inc,total,inc))

ax.grid(visible=True)

plt.show()
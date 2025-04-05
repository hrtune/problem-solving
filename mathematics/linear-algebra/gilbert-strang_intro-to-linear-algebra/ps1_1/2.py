"""
2 Draw v = (4, 1), w = (-2, 2), v + w, and v - w in a single xy plane.

v: blue
w: red
v + w: purple
-w: orange
v - w: brown
"""

import matplotlib.pyplot as plt

plt.figure()

# Draw v = (4, 1)
plt.quiver(0, 0, 4, 1, angles="xy", scale_units="xy", scale=1, color="blue")

# Draw w = (-2, 2)
plt.quiver(0, 0, -2, 2, angles="xy", scale_units="xy", scale=1, color="red")

# Draw v + w from v
plt.quiver(4, 1, -2, 2, angles="xy", scale_units="xy", scale=1, color="red")

# Draw v + w from 0
plt.quiver(0, 0, 2, 3, angles="xy", scale_units="xy", scale=1, color="purple")

# Draw -w from v
plt.quiver(4, 1, 2, -2, angles="xy", scale_units="xy", scale=1, color="orange")

# Draw v - w from 0
plt.quiver(0, 0, 6, -1, angles="xy", scale_units="xy", scale=1, color="brown")


plt.xlim(-3, 7)
plt.ylim(-3, 7)
plt.grid()

plt.xticks(range(-3, 8, 1))
plt.yticks(range(-3, 8, 1))

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.gca().set_aspect("equal")
plt.title("Vector using arrow")
plt.show()

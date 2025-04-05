"""
3 If v + w = (5, 1) and v - w = (1, 5), compute and draw the vectors v and w.

By adding up two vectors:
v + w + (v - w) = (6, 6)
2v = (6, 6)
v  = (3, 3)

Then substitute v into the former equation:
(3, 3) + w = (5, 1)
w = (5, 1) - (3, 3)
w = (2, -2)

v: blue
w: red
"""

import matplotlib.pyplot as plt

plt.figure()

# Draw v = (3, 3)
plt.quiver(0, 0, 3, 3, angles="xy", scale_units="xy", scale=1, color="blue")

# Draw w = (2, -2)
plt.quiver(0, 0, 2, -2, angles="xy", scale_units="xy", scale=1, color="red")

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

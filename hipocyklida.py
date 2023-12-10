import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R = 3
r = 1
d = 0.5
str_val = 0.5

fig, ax = plt.subplots()
ax.set_xlim(-R - r - d, R + r + d)
ax.set_ylim(-R - r - d, R + r + d)

circle_base, = ax.plot([], [], 'bo')
circle_rotating, = ax.plot([], [], 'go')
hypocycloid, = ax.plot([], [], 'r')
trace, = ax.plot([], [], 'g-')
radius, = ax.plot([], [], 'k-')
circle_base_outline, = ax.plot([], [], 'b--')
circle_rotating_outline, = ax.plot([], [], 'g--')

def init():
    circle_base.set_data([], [])
    circle_rotating.set_data([], [])
    hypocycloid.set_data([], [])
    trace.set_data([], [])
    radius.set_data([], [])
    circle_base_outline.set_data([], [])
    circle_rotating_outline.set_data([], [])
    return circle_base, circle_rotating, hypocycloid, trace, radius, circle_base_outline, circle_rotating_outline

def update2(frame):
    t = np.linspace(0, 2 * np.pi, 1000)

    x_base = 0
    y_base = 0

    x_rotating = R * np.cos(frame * str_val) - r * np.cos(frame * str_val)
    y_rotating = R * np.sin(frame * str_val) - r * np.sin(frame * str_val)

    x_hypocycloid = (R - r) * np.cos(frame * str_val) + r * np.cos((R / r - 1) * frame * str_val)
    y_hypocycloid = (R - r) * np.sin(frame * str_val) - r * np.sin((R / r - 1) * frame * str_val)

    x_radius = [x_rotating, x_hypocycloid]
    y_radius = [y_rotating, y_hypocycloid]

    circle_base.set_data([x_base], [y_base])
    circle_rotating.set_data([x_rotating], [y_rotating])
    hypocycloid.set_data([x_hypocycloid], [y_hypocycloid])
    trace.set_data(np.append(trace.get_xdata(), x_hypocycloid),
                   np.append(trace.get_ydata(), y_hypocycloid))
    radius.set_data(x_radius, y_radius)
    circle_base_outline.set_data(R * np.cos(t), R * np.sin(t))
    circle_rotating_outline.set_data(R * np.cos(frame * str_val) - r * np.cos(t),
                                     R * np.sin(frame * str_val) - r * np.sin(t))

    return circle_base, circle_rotating, hypocycloid, trace, radius, circle_base_outline, circle_rotating_outline

animation = FuncAnimation(fig, update2, frames=np.arange(0, 100, 0.1), init_func=init, blit=True)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parametry epicykloidy
R = 2  # Promień koła bazowego
r = 0.5  # Promień koła obracającego się wokół koła bazowego
stosunek_promieni = 2 * (R - r)
d = R - stosunek_promieni * r  # Odległość punktu na obracającym się kole od środka koła bazowego
str_val = 0.5  # Parametr sterujący animacją

# Utworzenie figury i osi
fig, ax = plt.subplots()
ax.set_xlim(-R - 2 * r - d, R + 2 * r + d)
ax.set_ylim(-R - 2 * r - d, R + 2 * r + d)

# Utworzenie obiektów do animacji
circle_base, = ax.plot([], [], 'bo')  # Koło bazowe
circle_rotating, = ax.plot([], [], 'go')  # Koło obracające się
epicycloid, = ax.plot([], [], 'r')  # Epicykloida
trace, = ax.plot([], [], 'g-')  # Ślad epicykloidy
radius, = ax.plot([], [], 'k-')  # Promień mniejszego koła
circle_base_outline, = ax.plot([], [], 'b--')  # Obwód koła bazowego
circle_rotating_outline, = ax.plot([], [], 'g--')  # Obwód koła obracającego się

# Funkcja inicjalizująca animację
def init():
    circle_base.set_data([], [])
    circle_rotating.set_data([], [])
    epicycloid.set_data([], [])
    trace.set_data([], [])
    radius.set_data([], [])
    circle_base_outline.set_data([], [])
    circle_rotating_outline.set_data([], [])
    return circle_base, epicycloid, trace, radius, circle_base_outline, circle_rotating

# Funkcja klatki animacji
def update(frame):
    t = np.linspace(0, 2 * np.pi, 1000)

    # Położenie koła bazowego
    x_base = 0
    y_base = 0

    # Położenie koła obracającego się wokół koła bazowego
    x_rotating = (R + r) * np.cos(frame * str_val)
    y_rotating = (R + r) * np.sin(frame * str_val)

    # Położenie punktu na obracającym się kole (epicykloida)
    x_epicycloid = x_rotating + d * np.cos((R + r) / r * frame * str_val)
    y_epicycloid = y_rotating + d * np.sin((R + r) / r * frame * str_val)

    # Położenie końca promienia mniejszego koła
    x_radius = [x_rotating, x_epicycloid]
    y_radius = [y_rotating, y_epicycloid]

    # Aktualizacja danych obiektów animacji
    circle_base.set_data([x_base], [y_base])
    circle_rotating.set_data([x_rotating], [y_rotating])
    epicycloid.set_data([x_epicycloid], [y_epicycloid])
    trace.set_data(np.append(trace.get_xdata(), x_epicycloid),
                   np.append(trace.get_ydata(), y_epicycloid))
    radius.set_data(x_radius, y_radius)
    circle_base_outline.set_data(R * np.cos(t), R * np.sin(t))
    circle_rotating_outline.set_data(R * np.cos(t) + r * np.cos(t),
                                     R * np.sin(t) + r * np.sin(t))
    return circle_base, epicycloid, trace, radius, circle_base_outline, circle_rotating

# Utworzenie animacji
animation = FuncAnimation(fig, update, frames=np.arange(0, 100, 0.1), init_func=init, blit=True)

# Wyświetlenie animacji
plt.show()

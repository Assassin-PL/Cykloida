# Cykloida
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# stale, promień, dokłądność,
promien_okregu_cykloidy = 0.05
promien_okregu_epicykloidy = promien_okregu_cykloidy / 2
l = 0.001
str = 1

# deklaracja trasy
fun_x = np.arange(0.00001, 10, l)  # d eklaracja argumentu
# fun_x = np.arange(-4, 4, l) #d eklaracja argumentu
# fun_y = fun_x* 0 + 1  # trasa fukcji sin
fun_y = 2 * (np.sin(fun_x) + np.sqrt(1 / fun_x)) / (np.power(fun_x, 2) + 53 + np.exp(fun_x))

# liczenie pochondych
dx = np.roll(fun_x, 1) - fun_x
dy = np.roll(fun_y, 1) - fun_y
dl = np.sqrt(dx ** 2 + dy ** 2)

# liczenie stycznych
styczna_a = dy / dx
styczna_b = fun_y - np.multiply(styczna_a, fun_x)

# deklaracja tablicy figury
x_data = []
y_data = []

# deklaracja tablicy, trasy
x_cykloida = []
y_cykloida = []
x_epicykloida = []
y_epicykloida = []
x_hipocykloida = []
y_hipocykloida = []

# setup plota
fig, ax = plt.subplots()
ax.set_xlim(min(fun_x), max(fun_x))
ax.set_ylim(-0.01, 5)
line, = ax.plot(fun_x, fun_y)
line2, = ax.plot(0, 0)
line3, = ax.plot(0, 0)
# deklaracja cykloidy
cykloida_center, = ax.plot(0, 0, marker='o')
cykloida, = ax.plot(0, 0)
cykloida_promien, = ax.plot(0, 0)
# deklaracja
epicykloida, = ax.plot(0, 0)
epicykloida_center, = ax.plot(0, 0, marker='x')
epicykloida_promien, = ax.plot(0, 0)
hipocykloida = ax.plot(0, 0)
# cykloida_promien, = ax.plot(0, 0)

# deklaracja pkt start
A = styczna_a[0]
B = -1
start_cykloida_v0 = np.array([A, B])
start_cykloida_v0 = start_cykloida_v0 / np.sqrt(np.sum(start_cykloida_v0 ** 2))
start_cykloida_v0 = np.multiply(start_cykloida_v0, (promien_okregu_cykloidy))

A = styczna_a[0] + 2 * promien_okregu_cykloidy
B = -1
start_epicykloida = np.array([A, B])
start_epicykloida = start_epicykloida / np.sqrt(np.sum(start_epicykloida ** 2))
start_epicykloida = np.multiply(start_epicykloida, - promien_okregu_cykloidy * str)


def frame(i):
    x = fun_x[i]
    y = styczna_a[i] * fun_x[i] + styczna_b[i]
    # vektor do centrum
    A = styczna_a[i]
    B = -1
    wektor_do_centrum_cykloidy = np.array([A, B])
    wektor_do_centrum_cykloidy = wektor_do_centrum_cykloidy / np.sqrt(np.sum(wektor_do_centrum_cykloidy ** 2))
    wektor_do_centrum_cykloidy = np.multiply(wektor_do_centrum_cykloidy, -promien_okregu_cykloidy * str)

    # kąt obrotu punktu względem środka okręgu
    cykloida_alfa = dl[i] / promien_okregu_cykloidy * str * -1
    nowy_punkt_cykloidy_vx = start_cykloida_v0[0] * np.cos(cykloida_alfa) - start_cykloida_v0[1] * np.sin(cykloida_alfa)
    nowy_punkt_cykloidy_vy = start_cykloida_v0[0] * np.sin(cykloida_alfa) + start_cykloida_v0[1] * np.cos(cykloida_alfa)
    start_cykloida_v0[0] = nowy_punkt_cykloidy_vx
    start_cykloida_v0[1] = nowy_punkt_cykloidy_vy

    x_cykloida.append(x + wektor_do_centrum_cykloidy[0] + nowy_punkt_cykloidy_vx)
    y_cykloida.append(y + wektor_do_centrum_cykloidy[1] + nowy_punkt_cykloidy_vy)
    t = np.arange(0, 2 * 3.1416, 0.03)

    # aktualizacja położenia okręgu
    x_okregu_cykloidy = promien_okregu_cykloidy * np.cos(t) + x + wektor_do_centrum_cykloidy[0]
    y_okregu_cykloidy = promien_okregu_cykloidy * np.sin(t) + y + wektor_do_centrum_cykloidy[1]

    # aktualizacja wizualiazcji kształtów
    line2.set_xdata(x_okregu_cykloidy)
    line2.set_ydata(y_okregu_cykloidy)
    cykloida_center.set_data(x + wektor_do_centrum_cykloidy[0], y + wektor_do_centrum_cykloidy[1])
    cykloida.set_data(x_cykloida, y_cykloida)
    cykloida_promien.set_data(
        [x + wektor_do_centrum_cykloidy[0], x + wektor_do_centrum_cykloidy[0] + nowy_punkt_cykloidy_vx],
        [y + wektor_do_centrum_cykloidy[1], y + wektor_do_centrum_cykloidy[1] + nowy_punkt_cykloidy_vy])

    return line, line2, cykloida_center, cykloida


animation = FuncAnimation(fig, func=frame, frames=np.arange(len(styczna_a)), interval=1, repeat=False)

plt.show()

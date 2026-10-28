import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figuras", exist_ok=True)

f = lambda x: 1 / (1 + 25 * x**2)
xx = np.linspace(-1, 1, 1000)
plt.plot(xx, f(xx), 'k', linewidth=2, label='f(x)')
for n in [4, 8, 12]:
    xn = np.linspace(-1, 1, n + 1)  # n+1 puntos equiespaciados
    c = np.polyfit(xn, f(xn), n)  # polinomio de grado n
    error = np.max(np.abs(np.polyval(c, xx) - f(xx)))
    print(f"n = {n:2d} error maximo = {error:.4f}")
    plt.plot(xx, np.polyval(c, xx), label=f'grado {n}')
plt.ylim(-1, 2); plt.legend(); plt.grid()
plt.savefig("figuras/parte4_runge.png")
plt.show()

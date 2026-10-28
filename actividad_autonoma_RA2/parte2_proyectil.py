import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figuras", exist_ok=True)

t = np.array([0.0, 1.0, 2.0])
h = np.array([2.0, 12.1, 12.4])
A = np.vander(t, increasing=True)  # observa que matriz es A
print(A)
a = np.linalg.solve(A, h)
print(a)  # coeficientes a0, a1, a2

tt = np.linspace(0, 3, 200)
plt.plot(t, h, 'ro', tt, a[0] + a[1]*tt + a[2]*tt**2)
plt.grid()
plt.savefig("figuras/parte2_proyectil.png")
plt.show()

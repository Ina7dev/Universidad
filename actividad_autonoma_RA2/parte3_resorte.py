import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figuras", exist_ok=True)

F = np.arange(7)
x = np.array([0.1, 1.9, 4.2, 5.8, 8.1, 9.9, 12.2])

# 3.1 grafico solo de los datos
plt.plot(F, x, 'ko')
plt.xlabel('F [N]'); plt.ylabel('x [cm]'); plt.grid()
plt.savefig("figuras/parte3_datos.png")
plt.show()

# 3.3
c6 = np.polyfit(F, x, 6)  # grado 6: pasa por los 7 puntos
c1 = np.polyfit(F, x, 1)  # grado 1: recta de "mejor ajuste"
print("Recta:", c1)

FF = np.linspace(0, 6.5, 300)
plt.plot(F, x, 'ko', label='datos')
plt.plot(FF, np.polyval(c6, FF), label='grado 6')
plt.plot(FF, np.polyval(c1, FF), label='grado 1')
plt.legend(); plt.grid()
plt.savefig("figuras/parte3_resorte.png")
plt.show()

for Fi in [5.5, 6.5]:
    print(Fi, np.polyval(c6, Fi), np.polyval(c1, Fi))

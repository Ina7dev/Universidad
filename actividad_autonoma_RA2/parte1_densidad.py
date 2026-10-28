import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figuras", exist_ok=True)

T = np.array([0, 10, 20, 30, 40, 50])
rho = np.array([999.84, 999.70, 998.21, 995.65, 992.22, 988.04])
print(np.interp(25, T, rho))  # interpolacion lineal

plt.plot(T, rho, 'o-')
plt.xlabel('T [°C]'); plt.ylabel('densidad [kg/m3]'); plt.grid()
plt.savefig("figuras/parte1_densidad.png")
plt.show()

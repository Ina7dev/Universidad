import numpy as np
import matplotlib.pyplot as plt

class FuncionTrigonometrica:
    def __init__(self, tipo, amplitud=1, periodo=2 * np.pi):
        self.tipo = tipo.lower()
        self.amplitud = amplitud
        self.periodo = periodo
        if self.tipo not in ['seno', 'coseno', 'tangente']:
            raise ValueError("Debe ser uno de los 3: seno, coseno, tangente")

    def evaluar(self, x):
        if self.tipo == 'seno':
            return self.amplitud * np.sin(x * 2 * np.pi / self.periodo)
        elif self.tipo == 'coseno':
            return self.amplitud * np.cos(x * 2 * np.pi / self.periodo)
        elif self.tipo == 'tangente':
            return self.amplitud * np.tan(x * 2 * np.pi / self.periodo)

    def graficar(self, rango=(-2 * np.pi, 2 * np.pi), pts=1000):
        x = np.linspace(rango[0], rango[1], pts)
        y = np.array([self.evaluar(xi) for xi in x])
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f'{self.tipo.capitalize()} (amplitud={self.amplitud}, periodo={self.periodo})')
        plt.xlabel('x (radianes)')
        plt.ylabel('f(x)')
        plt.title(f'Gráfico de la función {self.tipo.capitalize()}')
        plt.legend()
        plt.grid(True)
        plt.ylim(-self.amplitud - 1, self.amplitud + 1)
        plt.show()

    def __str__(self):
        return (f'Función: {self.tipo.capitalize()}\n'
                f'Amplitud: {self.amplitud}\n'
                f'Período: {self.periodo}')

    def valor_critico(self):
        if self.tipo in ['seno', 'coseno']:
            return f'Máximo: {self.amplitud}, Mínimo: {-self.amplitud}'
        elif self.tipo == 'tangente':
            return 'No tiene valores críticos definidos'

# Crear una función seno con amplitud 2 y período 4*pi
func_seno = FuncionTrigonometrica('seno', 2, 4 * np.pi)
func_seno.graficar()
print(func_seno)
print('Valor crítico:', func_seno.valor_critico())

import numpy as np
import matplotlib.pyplot as plt

class Cuerpo:
    def __init__(self, velocidad, posicion_inicial):
        self.velocidad = velocidad
        self.posicion_inicial = posicion_inicial
    
    def posicion(self, tiempo):
        return self.posicion_inicial + self.velocidad * tiempo

class SimuladorMovimiento:
    def __init__(self, cuerpo):
        self.cuerpo = cuerpo
    
    def simular(self, tiempo_maximo, num_puntos):
        tiempos = np.linspace(0, tiempo_maximo, num_puntos)
        posiciones = [self.cuerpo.posicion(t) for t in tiempos]
        
        plt.figure(figsize=(10, 6))
        plt.plot(tiempos, posiciones, label='Posición vs. Tiempo', color='b')
        plt.title('MRU')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Posición (m)')
        plt.grid(True)
        plt.legend()
        plt.show()

# VELOCIDAD: 5 m/s | X inicial: 0 m
cuerpo = Cuerpo(5,0)
    
#crear el grafico
simulador = SimuladorMovimiento(cuerpo)
    
# Simular el movimiento durante 10 segundos (100 puntos para grafico)
simulador.simular(10,100)
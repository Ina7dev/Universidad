"""Desarrollar un programa en Pygame que permita
mover dos círculos independientes por la pantalla y
evitar que colisionen entre sí.
El programa debe detectar colisiones circulares y
evitar que los círculos se superpongan, cambiando
su color como indicativo de colisión"""

import pygame
import math

# Inicializa Pygame
pygame.init()

# Configuración de pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Círculos en Movimiento")

# Colores
color_corculo_1 = (0, 128, 255)
color_circulo_2 = (255, 100, 0)
color_colision = (255, 0, 0)
blanco = (255, 255, 255)

# Posiciones y radios iniciales
pos_circulo_1 = [200, 300]
radio_1 = 40
vel_circulo_1 = [3, 3]

pos_circulo_2 = [600, 300]
radio_2 = 40
vel_circulo_2 = [3, -3]

# Función para detectar colisiones circulares
def hay_colision(pos1, pos2, radio1, radio2):
    distancia = math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
    return distancia < (radio1 + radio2)

# Ciclo principal del juego
ejecutando = True
while ejecutando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizar posiciones de los círculos
    for i in range(2):
        pos_circulo_1[i] += vel_circulo_1[i]
        pos_circulo_2[i] += vel_circulo_2[i]

    # Rebotar en los bordes de la pantalla (para el círculo 1)
    if pos_circulo_1[0] - radio_1 <= 0 or pos_circulo_1[0] + radio_1 >= ancho:
        vel_circulo_1[0] *= -1
    if pos_circulo_1[1] - radio_1 <= 0 or pos_circulo_1[1] + radio_1 >= alto:
        vel_circulo_1[1] *= -1

    # Rebotar en los bordes de la pantalla (para el círculo 2)
    if pos_circulo_2[0] - radio_2 <= 0 or pos_circulo_2[0] + radio_2 >= ancho:
        vel_circulo_2[0] *= -1
    if pos_circulo_2[1] - radio_2 <= 0 or pos_circulo_2[1] + radio_2 >= alto:
        vel_circulo_2[1] *= -1

    # Detectar colisión entre los círculos
    if hay_colision(pos_circulo_1, pos_circulo_2, radio_1, radio_2):
        color_1 = color_colision
        color_2 = color_colision
    else:
        color_1 = color_corculo_1
        color_2 = color_circulo_2

    # Dibujar todo en la pantalla
    pantalla.fill(blanco)
    pygame.draw.circle(pantalla, color_1, (int(pos_circulo_1[0]), int(pos_circulo_1[1])), radio_1)
    pygame.draw.circle(pantalla, color_2, (int(pos_circulo_2[0]), int(pos_circulo_2[1])), radio_2)

    # Actualizar la pantalla
    pygame.display.flip()

    # Control de la velocidad del bucle
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()

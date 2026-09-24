import pygame

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Control de Figuras Geométricas")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Posiciones iniciales
pos_triangulo = [200, 300]
pos_circulo = [400, 300]
pos_cuadrado = [600, 300]

# Dimensiones
RADIO_CIRCULO = 30
LADO_CUADRADO = 60

# Velocidad de movimiento
VELOCIDAD = 5

# Ciclo principal
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Detectar teclas presionadas
    teclas = pygame.key.get_pressed()

    # Movimiento del triángulo con flechas
    if teclas[pygame.K_UP]:
        pos_triangulo[1] -= VELOCIDAD
    if teclas[pygame.K_DOWN]:
        pos_triangulo[1] += VELOCIDAD
    if teclas[pygame.K_LEFT]:
        pos_triangulo[0] -= VELOCIDAD
    if teclas[pygame.K_RIGHT]:
        pos_triangulo[0] += VELOCIDAD

    # Movimiento del círculo con WASD
    if teclas[pygame.K_w]:
        pos_circulo[1] -= VELOCIDAD
    if teclas[pygame.K_s]:
        pos_circulo[1] += VELOCIDAD
    if teclas[pygame.K_a]:
        pos_circulo[0] -= VELOCIDAD
    if teclas[pygame.K_d]:
        pos_circulo[0] += VELOCIDAD

    # Movimiento del cuadrado con IJKL
    if teclas[pygame.K_i]:
        pos_cuadrado[1] -= VELOCIDAD
    if teclas[pygame.K_k]:
        pos_cuadrado[1] += VELOCIDAD
    if teclas[pygame.K_j]:
        pos_cuadrado[0] -= VELOCIDAD
    if teclas[pygame.K_l]:
        pos_cuadrado[0] += VELOCIDAD

    # Dibujar en la pantalla
    VENTANA.fill(NEGRO)
    pygame.draw.polygon(VENTANA, ROJO, [
        (pos_triangulo[0], pos_triangulo[1] - 20),
        (pos_triangulo[0] - 20, pos_triangulo[1] + 20),
        (pos_triangulo[0] + 20, pos_triangulo[1] + 20)
    ])
    pygame.draw.circle(VENTANA, VERDE, pos_circulo, RADIO_CIRCULO)
    pygame.draw.rect(VENTANA, AZUL, (pos_cuadrado[0], pos_cuadrado[1], LADO_CUADRADO, LADO_CUADRADO))

    # Actualizar pantalla
    pygame.display.flip()

    # Control de FPS
    reloj.tick(30)

pygame.quit()

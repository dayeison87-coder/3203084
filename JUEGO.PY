import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Juego en Python")

# Colores
BLANCO = (255, 255, 255)
AZUL = (50, 100, 255)
ROJO = (255, 50, 50)

# Jugador
jugador_size = 40
jugador = pygame.Rect(100, 300, jugador_size, jugador_size)
velocidad_jugador = 5

# Enemigo
enemigo_size = 40
enemigo = pygame.Rect(random.randint(0, ANCHO - enemigo_size), 0, enemigo_size, enemigo_size)
velocidad_enemigo = 5

# Reloj
clock = pygame.time.Clock()

# Fuente para el texto
fuente = pygame.font.SysFont("Arial", 30)

# Puntuación
puntos = 0

# Bucle principal
while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += velocidad_jugador
    if teclas[pygame.K_UP] and jugador.top > 0:
        jugador.y -= velocidad_jugador
    if teclas[pygame.K_DOWN] and jugador.bottom < ALTO:
        jugador.y += velocidad_jugador

    # Movimiento del enemigo
    enemigo.y += velocidad_enemigo
    if enemigo.top > ALTO:
        enemigo.x = random.randint(0, ANCHO - enemigo_size)
        enemigo.y = 0
        puntos += 1  # Gana un punto si lo esquiva

    # Colisión
    if jugador.colliderect(enemigo):
        print("¡GAME OVER! Puntos:", puntos)
        pygame.quit()
        sys.exit()

    # Dibujar en pantalla
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, AZUL, jugador)
    pygame.draw.rect(ventana, ROJO, enemigo)

    # Mostrar puntuación
    texto = fuente.render(f"Puntos: {puntos}", True, (0, 0, 0))
    ventana.blit(texto, (10, 10))

    pygame.display.flip()
    clock.tick(30)  # 30 FPS

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('Múltiplos obstáculos')
screen_width, screen_height = screen.get_size()
running = True
dt = 0
#CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Player
player = pygame.Rect(100, 100, 50, 50)
speed = 300

#Obstáculos
obstaculos = []
for _ in range(5):
    x = random.randint(0, screen_width - 50)
    y = random.randint(0, screen_height - 50)
    obstaculo = pygame.Rect(x, y, 50, 50)
    obstaculos.append(obstaculo)

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0: player.x -= speed * dt
    if keys[pygame.K_RIGHT] and player.x < screen_width - player.width: player.x += speed * dt
    if keys[pygame.K_UP] and player.y > 0: player.y -= speed * dt
    if keys[pygame.K_DOWN] and player.y < screen_height - player.height: player.y += speed * dt

    #Limpa tela
    screen.fill(BLACK)

    #verificar colisão
    for obstaculo in obstaculos:
        if player.colliderect(obstaculo):
            print('Colisão detectada')

    #Desenhar player
    pygame.draw.rect(screen, RED, player)

    #Desenhar obstáculos
    for obstaculo in obstaculos:
        pygame.draw.rect(screen, GREEN, obstaculo)
    
    pygame.display.flip()

    dt = clock.tick(30) / 1000


pygame.quit()
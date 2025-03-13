import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
#CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#Definir retângulos
player = pygame.Rect(100, 100, 50, 50)
wall = pygame.Rect(300, 100, 50, 50)

speed = 100
running = True
playerx, playery = 100, 100
dt = 0

while running:
    for evente in pygame.event.get():
        if evente.type == pygame.QUIT:
            running = False 
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0: player.x -= speed * dt
    if keys[pygame.K_RIGHT] and player.x < 800 - player.width: player.x += speed * dt
    if keys[pygame.K_UP] and player.y > 0: player.y -= speed * dt
    if keys[pygame.K_DOWN] and player.y < 600 - player.height: player.y += speed * dt

    #Detectar colisão
    if player.colliderect(wall):
        player.x, player.y = playerx, playery
        print('Colisão detectada')

    screen.fill('#454545')   

    #desenhar player e wall
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, GREEN, wall)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
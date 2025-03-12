import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Movimentação de objeto')

dt = 0

x, y = 100, 100
speed = 200

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('#c8d6e5') #Limpa a tela em cada iteração

    pygame.draw.rect(screen, 'yellow', (x, y, 50, 50))
    #movimentação
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= speed * dt
    if keys[pygame.K_RIGHT]: x += speed * dt
    if keys[pygame.K_UP]: y -= speed * dt
    if keys[pygame.K_DOWN]: y += speed * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Movimentação de objeto')

dt = 0

x, y = 100, 100
screen_width, screen_height = screen.get_size()
player_size = 50
speed = 200
print(screen_width)
print(screen_height)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('#c8d6e5') #Limpa a tela em cada iteração

    pygame.draw.rect(screen, 'yellow', (x, y, player_size, player_size))
    #movimentação
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0: x -= speed * dt
    if keys[pygame.K_RIGHT] and x < screen_width - player_size: x += speed * dt
    if keys[pygame.K_UP] and y > 0: y -= speed * dt
    if keys[pygame.K_DOWN] and y < screen_height - player_size: y += speed * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
import pygame


pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
screen.fill('brown')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, 'white', event.pos, 20)

    pygame.display.flip()
    clock.tick(60)
 

pygame.quit()
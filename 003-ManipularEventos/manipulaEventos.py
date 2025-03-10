import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #detectar evento de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Pressionou SPACE!")
        #Detectar evento de mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse clicado em {event.pos}")

    screen.fill((0, 100, 0))

    pygame.display.flip()

pygame.quit()
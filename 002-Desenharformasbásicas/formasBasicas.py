import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Formas básicas")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Atualizar o fundo ada tela
    screen.fill((0, 0, 0))

    #Desenhos
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 60, 60)) # retangulo verde de 60x60 na posição (100, 100)
    pygame.draw.circle(screen, (255, 0, 0), (300, 300), 60) #círculo vermelho

    # Atualiza a tela para exibir os desenhos
    pygame.display.flip()

pygame.quit()
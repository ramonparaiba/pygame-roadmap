import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Formas básicas")

running = True
screen.fill((50, 0, 0))
triangulo_coordenadas = [
    (550, 30), (500, 100), (600, 100)
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Atualizar o fundo da tela
    

    #Desenhos
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 60, 60)) # retangulo verde de 60x60 na posição (100, 100)
    pygame.draw.circle(screen, (255, 0, 0), (300, 300), 60) #círculo vermelho de raio 60

    pygame.draw.polygon(screen, (0, 0, 100), triangulo_coordenadas)

    # Atualiza a tela para exibir os desenhos
    pygame.display.flip()

pygame.quit()
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Projetil Simples')
dt = 1/60

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Classe para o projetil
class Projetil:
    def __init__(self, x, y, angulo, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.rect = pygame.Rect(self.x, self.y, 10, 10)

    def update(self, dt):
        self.rect.x += self.velocidade * dt
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, RED, self.rect)

# Lista para armazenar projéteis
projeteis = []

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projeteis.append(Projetil(50, 550, 45, 100))

    #atualiando os projeteis
    for projetil in projeteis:
        projetil.update(dt)

    #Remover projéteis que saíram da tela
    projeteis = [projetil for projetil in projeteis if projetil.rect.x < 800]

    # Desenhar
    screen.fill(WHITE)
    for projetil in projeteis:
        projetil.draw(screen)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()


import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
pygame.display.set_caption('Projetil lançado automaticamente')
clock = pygame.time.Clock()
pygame.display.set_caption('Projetil lançado automaticamente')

dt = 0
# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

projetil_width = 10
projetil_height = 10
projetil_speed = 30


class Projetil:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, projetil_width, projetil_height)

    def update(self, dt):
        self.rect.x += projetil_speed

    def draw(self, screen):
        pygame.draw.ellipse(screen, RED, self.rect)

def criar_projetil():
    x = 0
    y = random.randint(0, 600)
    return Projetil(x, y)

projeteis = []

running = True
last_projetil_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    if current_time - last_projetil_time >= 500:
        projeteis.append(criar_projetil())
        last_projetil_time = current_time
    
    for projetil in projeteis:
        projetil.update(dt)
    
    #Remover projeteis que saem da tela
    projeteis = [projetil for projetil in projeteis if projetil.rect.x < 800]
    
    screen.fill(BLACK)
    for projetil in projeteis:
        pygame.draw.ellipse(screen, RED, projetil)
    
    pygame.display.flip()

    dt = clock.tick(60)
     
pygame.quit()
sys.exit()
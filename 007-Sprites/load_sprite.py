import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprite Loading")

# Load the sprite image
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "imgs/mario.png")
sprite_img = pygame.image.load(image_path)

# Get sprite retangle and screen rectangle
sprite_rect = sprite_img.get_rect()
sprite_rect.center = (400, 300)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    screen.blit(sprite_img, sprite_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
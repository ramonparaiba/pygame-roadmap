import pygame
import os

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sound and Music")

# Load the sound file
current_dir = os.path.dirname(__file__)
sound_path = os.path.join(current_dir, "ghost.mp3")

sound = pygame.mixer.Sound(sound_path)

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound.play() 
    
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()

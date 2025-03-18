import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprite Animation")

# Load the sprite sheet
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "imgs/mario.png")
sprite_sheet = pygame.image.load(image_path)

# Define the size of each frame
frame_width = 32  # Largura de cada frame
frame_height = 32  # Altura de cada frame
num_frames = 4  # Número de frames na animação

# Get sprite rectangle and screen rectangle
sprite_rect = pygame.Rect(0, 0, frame_width, frame_height)
sprite_rect.center = (400, 300)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the current frame
    frame = (pygame.time.get_ticks() // 100) % num_frames

    # Update the sprite rectangle to show the correct frame
    sprite_rect.x = frame * frame_width

    # Clear the screen
    screen.fill("white")

    # Draw the current frame
    screen.blit(sprite_sheet, sprite_rect, area=pygame.Rect(frame * frame_width, 0, frame_width, frame_height))

    # Update the display
    pygame.display.flip()

pygame.quit()
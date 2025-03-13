import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))

print(f"A altura da tela é {screen.get_height()}")
print(f"A largura da tela é {screen.get_width()}")

pygame.quit()
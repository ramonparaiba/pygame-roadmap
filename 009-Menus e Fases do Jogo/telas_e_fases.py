import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo e Fases')

#Cores do jogo
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

#Fontes
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

#estados do jogo
MENU = 0
Game = 1
GameOver = 2

#Variável de estado
game_state = MENU

#posiçao inicial do player
player_pos = [400, 300]

#Função para desenhar o menu

def draw_menu():
    screen.fill(PRETO)
    play_button = pygame.Rect(300, 200, 200, 100)
    pygame.draw.rect(screen, VERDE, play_button)
    text = font.render('Jogar', True, PRETO)
    screen.blit(text, (320, 220))
    return play_button

#Função para desenhar o jogo
def draw_game(player_pos):
    screen.fill(BRANCO)
    player = pygame.Rect(player_pos[0], player_pos[1], 50, 50)
    pygame.draw.rect(screen, VERMELHO, player)
    enemy = pygame.Rect(600, 300, 50, 50)
    pygame.draw.circle(screen, AZUL, (enemy.x, enemy.y), 25)
    return player, enemy

#Função para desenhar a tela de game over
def draw_game_over():
    screen.fill(AMARELO)
    text = font.render('Game Over', True, BRANCO)
    screen.blit(text, (300, 200))
    menu_button = pygame.Rect(300, 300, 400, 100)
    pygame.draw.rect(screen, PRETO, menu_button)
    text_button = small_font.render('Retornar ao Menu', True, BRANCO)
    screen.blit(text_button, (310, 320))
    return menu_button

#Loop principal do jogo
clock = pygame.time.Clock()
running = True
speed = 300
dt = 0

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        
        if game_state == MENU:
            play_button = draw_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    game_state = Game

        elif game_state == Game:
           keys = pygame.key.get_pressed()
           if keys[pygame.K_LEFT]: player_pos[0] -= speed * dt
           if keys[pygame.K_RIGHT]: player_pos[0] += speed * dt
           if keys[pygame.K_UP]: player_pos[1] -= speed * dt
           if keys[pygame.K_DOWN]: player_pos[1] += speed * dt
           
           player, enemy = draw_game(player_pos)
           if player.colliderect(enemy):
               game_state = GameOver

        elif game_state == GameOver:
            menu_button = draw_game_over()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    game_state = MENU

    dt = clock.tick(30) / 1000
    pygame.display.flip()
pygame.quit()

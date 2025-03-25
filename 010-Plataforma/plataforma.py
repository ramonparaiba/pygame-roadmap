import pygame

pygame.init()
Width = 800
Height = 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Exemplo simples de plataforma")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Configurações do Player
player_radius = 20
player_x = screen.get_width() // 2
player_y = screen.get_height() // 2
player_speed = 5
jump_force = 15
gravity = 1

#Variáveis de movimento
player_vel_x = 0
player_vel_y = 0
is_jumping = False

#Plataformas
platforms = [
    (0, Height - 40, Width, 40),
    (100, Height - 150, 200, 20),
    (400, Height - 200, 200, 20),
    (200, Height - 300, 150, 20),
]

#Game Loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #movimento Horizontal
    player_vel_x = 0
    if keys[pygame.K_LEFT]:
        player_vel_x = -player_speed
    if keys[pygame.K_RIGHT]:
        player_vel_x = player_speed
    
    #Jump
    if keys[pygame.K_SPACE] and not is_jumping:
        player_vel_y = -jump_force
        is_jumping = True
    
    #Aplicando a gravidade
    player_vel_y += gravity

    #Atualizando a posição do player
    player_x += player_vel_x
    player_y += player_vel_y

    #Manter o player dentro da tela
    if player_x - player_radius < 0:
        player_x = player_radius
    if player_x + player_radius > Width:
        player_x = Width - player_radius

    #Colisão com as plataformas
    is_jumping = True
    for platform in platforms:
        plat_x, plat_y, plat_w, plat_h = platform

        #verificar se o player está acima da plataforma
        if (player_y + player_radius > plat_y and 
            player_y - player_radius < plat_y + plat_h and
            player_x + player_radius > plat_x and 
            player_x - player_radius < plat_x + plat_w):
            
            player_y = plat_y - player_radius
            player_vel_y = 0
            is_jumping = False

    #Desenhar
    screen.fill(BLACK)

    #Desenhar plataformas
    for platform in platforms:
        pygame.draw.rect(screen, VERDE, platform)

    #Desenhar player
    pygame.draw.circle(screen, VERMELHO, (player_x, player_y), player_radius)


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
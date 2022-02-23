import pygame

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font_pixeltype.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)

pygame.init()
game_active = True
start_time = 0
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font_pixeltype = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()

# score_surface = font_pixeltype.render('Score', True, (64,64,64))
# score_rect = score_surface.get_rect(center = (400,50))

ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                snail_rect.left = 800
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
      
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen, (192,232,236), score_rect)
        # pygame.draw.rect(screen, (192,232,236), score_rect, 10)
    
        # screen.blit(score_surface, score_rect)
        display_score()
        screen.blit(snail_surface,snail_rect)
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: 
            player_rect.bottom = 300
        screen.blit(player_surface,player_rect)

        # collision
        if player_rect.colliderect(snail_rect):
            game_active = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if player_rect.bottom == 300:
                player_gravity = -20
    else:
        screen.fill('Blue')

    pygame.display.update()
    clock.tick(60)
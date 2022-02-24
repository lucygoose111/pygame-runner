from tkinter import CENTER
import pygame

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font_pixeltype.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time

pygame.init()
game_active = False
start_time = 0
screen = pygame.display.set_mode((800,400))
score = 0
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
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center=(400,200))
game_name = font_pixeltype.render('Pixel Runner', True, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))
game_ins = font_pixeltype.render('Press enter to start', False, (111,196,169))
game_ins_rect = game_ins.get_rect(center=(400,320))

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
        score = display_score()
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
        score_message = font_pixeltype.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center=(400,350))
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name,game_name_rect)
        screen.blit(game_ins,game_ins_rect)
        if score > 0: screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)
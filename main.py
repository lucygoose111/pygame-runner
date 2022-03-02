import pygame
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font_pixeltype.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):

        if (obstacle_list):
            for obstacle_rect in obstacle_list:
                obstacle_rect.x -= 5
                if obstacle_rect.bottom == 300:
                    screen.blit(snail_surf, obstacle_rect)
                else:
                    screen.blit(fly_surf, obstacle_rect)
        
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
            
            return obstacle_list
        else: return []

def collide(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    
    return True

def player_anim():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()
game_active = False
start_time = 0
screen = pygame.display.set_mode((800,400))
score = 0
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font_pixeltype = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('graphics/Sky.png').convert()

ground_surf = pygame.image.load('graphics/ground.png').convert()

# Obstacles
snail_move_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_move_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_move_1,snail_move_2]
snail_index = 0
snail_surf = snail_frames[snail_index]

fly_move_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_move_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_move_1,fly_move_2]
fly_index = 0
fly_surf = fly_frames[fly_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80,300))
player_gravity = 0
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center=(400,200))
game_name = font_pixeltype.render('Pixel Runner', True, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))
game_ins = font_pixeltype.render('Press enter to start', False, (111,196,169))
game_ins_rect = game_ins.get_rect(center=(400,320))

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

snail_anim_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_anim_timer, 500)

fly_anim_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_anim_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                if randint(0,1):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))
            if event.type == snail_anim_timer:
                if snail_index == 0: snail_index = 1
                else: snail_index = 0
                snail_surf = snail_frames[snail_index]
            if event.type == fly_anim_timer:
                if fly_index == 0: fly_index = 1
                else: fly_index = 0
                fly_surf = fly_frames[fly_index]

      
    if game_active:
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        score = display_score()

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: 
            player_rect.bottom = 300
        player_anim()
        screen.blit(player_surf,player_rect)

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision 
        game_active = collide(player_rect, obstacle_rect_list)

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
        obstacle_rect_list = []
        player_rect.midbottom = (80,300)
        player_gravity = 0

    pygame.display.update()
    clock.tick(60)
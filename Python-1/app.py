import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 100) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
test_font = pygame.font.SysFont('Calibri', 24)
game_active = True
start_time = 0

sky_surface = pygame.image.load('textures/layer 2.jpg').convert()
ground_surface = pygame.image.load('textures/layer 1.jpg').convert()

#score_surf = test_font.render('My game', False, (64,64,64))
#score_rect = score_surf.get_rect(center = (400, 50))

enemy_surface = pygame.image.load('textures/enemy1.jpg').convert_alpha()
enemy_rectangle = enemy_surface.get_rect(topleft = (500,250))

player_surface = pygame.image.load('textures/player.jpg').convert()
player_rectangle = player_surface.get_rect(topleft = (25,250))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('textures/player.jpg').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (400,200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:   
            if event.type == pygame.MOUSEBUTTONDOWN and player_rectangle.bottom >= 300:
                if player_rectangle.collidepoint(event.pos): 
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    enemy_rectangle.left = 800
                    start_time = int(pygame.time.get_ticks() / 100)

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surf,score_rect)
        display_score()

        enemy_rectangle.x -= 4
        if enemy_rectangle.right <= 0: enemy_rectangle.left = 800
        screen.blit(enemy_surface,enemy_rectangle)

        #PLAYER
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)

        #collision
        if enemy_rectangle.colliderect(player_rectangle):
            game_active = False

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

    pygame.display.update()
    clock.tick(60)



        #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')


    #if player_rectangle.colliderect(enemy_rectangle):
    #    print('collision')
    
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rectangle.collidepoint((mouse_pos)):
    #    print(pygame.mouse.get_pressed())
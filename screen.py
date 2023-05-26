import pygame
import os
from constants import button_image, window_screen, screen_col

from animations import menu_boxer_1, menu_boxer_2, player_one_idle, player_one_forward, player_one_backward, player_one_hurt, player_one_dizzy, player_two_idle, player_one_attack, player_two_forward, player_two_backward, player_two_attack, player_two_hurt, player_two_dizzy

player1_punches = []
player2_punches = []



index, player_one_speed, player_two_speed  = 0, 0, 0 
ring = pygame.image.load(os.path.join("assets", "ring.png"))

 

def main_screen(game_started, player_one, player_two, game_pause, game_end,  one_is_hit, two_is_hit, player_one_health, player_two_health):
    global index, player_one_speed, player_two_speed, player_one_is_hit
    index += 0.2
    player_one_speed += 0.2
    player_two_speed += 0.2



    print(f"Start: {game_started}, Pause: {game_pause}, End: {game_end}")

    if game_started and not game_pause and not game_end:
        window_screen.blit(ring, (0, 0))
        player_one_animated = player_one_animate(player_one, player_two)
        player_two_animated = player_two_animate(player_one, player_two)
        player_one_is_hit = one_is_hit
        player_two_is_hit = two_is_hit
        # player one action
        

        if player_one_animated == player_one_attack:
            if player_one_speed >= len(player_one_animated):
                player_one_speed = 0
            player_one_speed = 4
            window_screen.blit(player_one_animated[int(player_one_speed)], (player_one.x, player_one.y))
        elif player_one_is_hit !=0:
            print(f"P1: {player_one_health}")
            player_one.x -= 1
            if player_one_speed >= len(player_one_animated):
                player_one_speed = 0
            player_one_speed = 4.2
            window_screen.blit(player_one_hurt[int(player_one_speed)], (player_one.x, player_one.y))
        elif player_one_health <= 0:
            if index >= len(player_one_animated):
                index = 0
            window_screen.blit(player_one_dizzy[int(index)], (player_one.x, player_one.y))

            player_won = player_two
            has_winner = True
        else:
            if index >= len(menu_boxer_1):
                index = 0
            window_screen.blit(player_one_animated[int(index)], (player_one.x, player_one.y))
    
        # player two action
        
        if player_two_animated == player_two_attack:
            if player_two_speed >= len(player_two_animated):
                player_two_speed = 0
            player_two_speed = 4
            window_screen.blit(player_two_animated[int(player_two_speed)], (player_two.x, player_two.y))
        elif player_two_is_hit:
            print(f"P2: {player_two_health}")
            player_two.x += 1
            if player_two_speed >= len(player_two_animated):
                player_two_speed = 0
            player_two_speed = 4.2
            window_screen.blit(player_two_hurt[int(player_two_speed)], (player_two.x, player_two.y)) 
        elif player_two_health <= 0:
            if index >= len(player_two_animated):
                index = 0
            window_screen.blit(player_two_dizzy[int(index)], (player_two.x, player_two.y))   

            player_won = player_one
            has_winner = True
        else:
            if index >= len(menu_boxer_2):
                index = 0
            window_screen.blit(player_two_animated[int(index)], (player_two.x, player_two.y))
    elif game_end:
        window_screen.blit(ring, (0, 0))
        if player_two_health <= 0:
            if index >= len(menu_boxer_2):
                index = 0
            
            window_screen.blit(player_one_idle[int(index)], (player_one.x -3, player_one.y))
            window_screen.blit(player_two_dizzy[int(index)], (player_two.x, player_two.y))
        elif player_one_health <= 0:
            if index >= len(menu_boxer_2):
                index = 0
            window_screen.blit(player_one_dizzy[int(index)], (player_one.x, player_one.y))
            window_screen.blit(player_two_idle[int(index)], (player_two.x, player_two.y))
        

    else:
        window_screen.fill(screen_col)
        if index >= len(menu_boxer_1) or index >= len(menu_boxer_2):
            index = 0
        window_screen.blit(menu_boxer_1[int(index)], (180, 70))
        window_screen.blit(menu_boxer_2[int(index)], (380, 70))
        window_screen.blit(button_image, (250, 300))
    pygame.display.update()


def player_one_punches(player_one_punch, player_one, player_two, player_two_hit):
 
    # p1
    player_1_attack = player_one_animate(player_one, player_two)
    
    if player_two.colliderect(player_one_punch) and player_1_attack ==  player_one_attack:
        pygame.event.post(pygame.event.Event(player_two_hit))
        print("P2 is hit!")
        return player_two_hit
 
def player_two_punches(player_two_punch, player_one, player_two, player_one_hit):
    # p2
    player_2_attack = player_two_animate(player_two, player_two)
 
    if player_one.colliderect(player_two_punch) and player_2_attack ==  player_two_attack:
        pygame.event.post(pygame.event.Event(player_one_hit))
        print("P1 is hit!")
        return player_one_hit

def player_one_animate(player_one, player_two):
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_a]:
        player_one.x -= 1
        return player_one_backward
    elif key_pressed[pygame.K_d] and player_one.x != 748 and player_one.x != player_two.x - 100:
        player_one.x += 1
        return player_one_forward
    elif key_pressed[pygame.K_g]:
        return player_one_attack
    else:
        return player_one_idle

def player_two_animate(player_one, player_two):
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_j] and player_two.x != -36 and player_two.x != player_one.x + 100:
        player_two.x -= 1
        return player_two_backward
    elif key_pressed[pygame.K_l] and player_two.x != 748:
        player_two.x += 1
        return player_two_forward
    elif key_pressed[pygame.K_p]:
        return player_two_attack
    else:
        return player_two_idle
 
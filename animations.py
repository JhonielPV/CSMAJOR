import pygame 
import os
import constants
menu_boxer_1 = []
menu_boxer_2 = []


player_one_idle = []
player_one_forward = []
player_one_backward = []
player_one_attack = []
player_one_hurt = []
player_one_dizzy = []

player_two_idle = []
player_two_forward = []
player_two_backward = []
player_two_attack = []
player_two_hurt = []
player_two_dizzy = []

def generate_animation():
    for hurt in os.listdir("assets/left_boxer_1/hurt/hurt"):
        b_hurt = pygame.image.load(os.path.join("assets/left_boxer_1/hurt/hurt", hurt))
        menu_boxer_1.append(pygame.transform.scale(b_hurt, (301, 286)))

    for attacker in os.listdir("assets/Boxer06/3-Punch/1-JabRight"):
        b_attacker = pygame.image.load(os.path.join("assets/Boxer06/3-Punch/1-JabRight", attacker))
        menu_boxer_2.append(pygame.transform.scale(b_attacker, (301, 286)))

    # player one

    # player one idle 
    for player_idle in os.listdir("assets/left_boxer_1/idle"):
        idle = pygame.image.load(os.path.join("assets/left_boxer_1/idle", player_idle))
        player_one_idle.append(pygame.transform.scale(idle, (constants.boxer_width, constants.boxer_height)))

    # player one walk
    for player_walk_forward in os.listdir("assets/left_boxer_1/walk/forward"):
        walk = pygame.image.load(os.path.join("assets/left_boxer_1/walk/forward", player_walk_forward))
        player_one_forward.append(pygame.transform.scale(walk, (constants.boxer_width, constants.boxer_height)))

    for player_walk_backward in os.listdir("assets/left_boxer_1/walk/backward"):
        walk = pygame.image.load(os.path.join("assets/left_boxer_1/walk/backward", player_walk_backward))
        player_one_backward.append(pygame.transform.scale(walk, (constants.boxer_width, constants.boxer_height)))
    
    for player_walk_attack in os.listdir("assets/left_boxer_1/attack"):
        walk = pygame.image.load(os.path.join("assets/left_boxer_1/attack", player_walk_attack))
        player_one_attack.append(pygame.transform.scale(walk, (constants.boxer_width, constants.boxer_height)))
    
    for player_onee_hurt in os.listdir("assets/left_boxer_1/hurt/hurt"):
        hurt = pygame.image.load(os.path.join("assets/left_boxer_1/hurt/hurt", player_onee_hurt))
        player_one_hurt.append(pygame.transform.scale(hurt, (constants.boxer_width, constants.boxer_height)))
    
    for player_onee_dizzy in os.listdir("assets/left_boxer_1/hurt/dizzy"):
        dizzy = pygame.image.load(os.path.join("assets/left_boxer_1/hurt/dizzy", player_onee_dizzy))
        player_one_dizzy.append(pygame.transform.scale(dizzy, (constants.boxer_width, constants.boxer_height)))
    
     

    # player two
    for player_idle in os.listdir("assets/boxer_1/idle"):
        idle = pygame.image.load(os.path.join("assets/boxer_1/idle", player_idle))
        player_two_idle.append(pygame.transform.scale(idle, (constants.boxer_width, constants.boxer_height)))
    

    for player_walk_forward in os.listdir("assets/boxer_1/walk/forward"):
        walk = pygame.image.load(os.path.join("assets/boxer_1/walk/forward", player_walk_forward))
        player_two_forward.append(pygame.transform.scale(walk, (constants.boxer_width, constants.boxer_height)))

    for player_walk_backward in os.listdir("assets/boxer_1/walk/backward"):
        walk = pygame.image.load(os.path.join("assets/boxer_1/walk/backward", player_walk_backward))
        player_two_backward.append(pygame.transform.scale(walk, (constants.boxer_width, constants.boxer_height)))

    for player_walk_attack in os.listdir("assets/boxer_1/punch/2-JabLeft"):
        walk = pygame.image.load(os.path.join("assets/boxer_1/punch/2-JabLeft", player_walk_attack))
        player_two_attack.append(pygame.transform.scale(walk, (constants.boxer_width, constants.boxer_height)))
    
    for player_hurt in os.listdir("assets/boxer_1/hurt/2-HurtAlt"):
        hurt = pygame.image.load(os.path.join("assets/boxer_1/hurt/2-HurtAlt", player_hurt))
        player_two_hurt.append(pygame.transform.scale(hurt, (constants.boxer_width, constants.boxer_height)))
    
    for player_dizzy in os.listdir("assets/boxer_1/hurt/3-Dizzy"):
        dizzy = pygame.image.load(os.path.join("assets/boxer_1/hurt/3-Dizzy", player_dizzy))
        player_two_dizzy.append(pygame.transform.scale(dizzy, (constants.boxer_width, constants.boxer_height)))

     
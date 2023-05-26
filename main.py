import pygame
import constants
import animations
 
pygame.init()

from screen import main_screen, player_one_punches, player_two_punches

player_one_hit = pygame.USEREVENT + 1
player_two_hit = pygame.USEREVENT + 2

window = constants.window_screen
music = pygame.mixer.Sound("assets/music.ogg")

# music = pygame.mixer.music.load("assets/music.ogg")
music_end_event = pygame.USEREVENT + 3
pygame.mixer.music.set_endevent(music_end_event)

def main():
     
    run, game_started, game_end, game_pause = True, False, False, False
    
    player_one_health, player_two_health = 10, 10

    music.play()

    fps = pygame.time.Clock()
    
    player_one = pygame.Rect(100, 250, constants.boxer_width, constants.boxer_height)
    player_two = pygame.Rect(650, 250, constants.boxer_width, constants.boxer_height)

    player_won, player_lose = "", ""

    player_one_is_hit, player_two_is_hit = "", ""
    one_is_hit, two_is_hit = False, False

    while run:
        fps.tick(constants.screen_fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                # MENU KEYS
                if event.key == pygame.K_RETURN:
                    game_started = True                 
                elif not game_pause and event.key == pygame.K_F10:
                    game_pause = True
                elif game_pause and event.key == pygame.K_F10:
                    game_pause = False

                # ATTACK KEYS
                if event.key == pygame.K_g:
                    player_one_punch = pygame.Rect(
player_one.x - 50 + player_one.width, player_one.y + player_one.height//2 - 2, 10, 5)
                    player_two_is_hit = player_one_punches(player_one_punch, player_one, player_two, player_two_hit)

            
                if event.key == pygame.K_p:
                    player_two_punch = pygame.Rect(
player_two.x - 105 + player_two.width, player_two.y + player_two.height//2 - 2, 10, 5)
                    player_one_is_hit = player_two_punches(player_two_punch, player_one, player_two, player_one_hit)
            
            if event.type == player_one_is_hit:
                one_is_hit = True
                player_one_health -= 1
                print(f"P2 Health: {player_two_health}")
            elif event.type == player_two_is_hit:
                two_is_hit = True
                player_two_health -= 1
                print(f"P1 Health: {player_one_health}")
            elif event.type == music_end_event:
                pygame.mixer.music.play()
            else:
                one_is_hit, two_is_hit = False, False
        
        if player_one_health <= 0:
            player_won = player_two
            game_end = True
        elif player_two_health <= 0:
            player_won = player_one
            game_end = True
        else:
            print()

                


           
        main_screen(game_started, player_one, player_two, game_pause,  game_end, one_is_hit, two_is_hit, player_one_health, player_two_health)
    
    main()

if __name__ == "__main__":
    animations.generate_animation()
    main()

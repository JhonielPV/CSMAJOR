import pygame 


window_width, window_height = 900, 500
window_screen = pygame.display.set_mode((window_width, window_height))
screen_fps = 60
screen_col = "steelblue"
velocity = 2.5
boxer_width, boxer_height = 150, 130


 

button_image = pygame.image.load("assets/menu/play_button.png").convert_alpha()
menu_screen = pygame.image.load("assets/menu/menu_screen.png").convert_alpha()



 
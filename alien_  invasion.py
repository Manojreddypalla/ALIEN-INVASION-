import pygame 
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #initilze the screen and create a screen object 
    pygame.init()
    game_settings= Settings()
    screen=pygame.display.set_mode(
        (game_settings.screen_width,  game_settings.screen_height))
    # screen=pygame.display.set_mode((1200,800))

    #make a ship
    ship = Ship(screen)

    
    pygame.display.set_caption("alian invation ")
    # bg_color =(230,230,230)
    #set the background color 
   




#start the main loop buddy n
#from here ok 

    while True :
        gf.check_events(ship)
        # screen.fill(game_settings.bg_color)
        ship.update()

        # # Make the most recently drawn screen visible.
        # ship.blitme()
        # pygame.display.flip()        
        gf.update_screen(game_settings,screen,ship)



        
run_game()

import sys 
import pygame 
from settings import settings



def run_game():
    #initilze the screen and create a screen object 
    pygame.init()
    game_settings=settings()
    screen=pygame.display.setmode(game_settings.screen_width,game_settings.screen_height)

    
    pygame.display.set_caption("alian invation ")
    bg_color =(230,230,230)
    #set the background color 
   




#start the main loop buddy n
#from here ok 

    while True :
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()




        screen.fill(game_settings.bg_color)
           # Make the most recently drawn screen visible.
        pygame.display.flip()        
run_game()

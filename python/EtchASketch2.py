# Etch-a-sketch using Pygame

from sys import exit
import pygame
from pygame.locals import *


def main():
    """ called when the program starts.
        It initialises everything it needs and runs in a loop
        until the function returns """

    # Initialise everything
    pygame.init()
    window_size_x = 640
    window_size_y = 480

    screen = pygame.display.set_mode((window_size_x, window_size_y), 0, 32)
    pygame.display.set_caption("Etch-A-Sketch")
    clock = pygame.time.Clock()

    # Put the Turte in the middle of the window
    turtle_x = window_size_x / 2
    turtle_y = window_size_y / 2

    # The turtle doesn't move until we press a key
    offset_x = 0
    offset_y = 0

    # Normal speeed
    speed = 3

    # The cilour of the trail
    colour = (0, 255 ,0)

    # Main Loop
    hasQuit = False 

    while not hasQuit:

        # Make sure we don't run quicker than 60 fps
        clock.tick(60)

        # Handle input events
        for event in pygame.event.get():
            if event.type == QUIT:
                hasQuit = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                hasQuit = True
            # If the user pressed a key, set the direction
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    offset_y = -speed
                elif event.key == K_DOWN:
                    offset_y = speed
                elif event.key == K_LEFT:
                    offset_x = -speed
                elif event.key == K_RIGHT:
                    offset_x = speed
                elif event.key == K_1:
                    speed = 1
                elif event.key == K_2:
                    speed = 2
                elif event.key == K_3:
                    speed = 3
                elif event.key == K_4:
                    speed = 4
                elif event.key == K_5:
                    speed = 5
                    
            # If the user released a key, unset the direction
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    offset_y = 0 
                elif event.key == K_LEFT or event.key == K_RIGHT:
                    offset_x = 0

        # Update the turtle's position only if there's a direction key pressed
        if offset_x !=0 or offset_y != 0:
            # print("Drawing a line from (", turtle_x, ", ", turtle_y, ") to (", turtle_x + offset_x, ", ", turtle_y+offset_y, ")")
            rect = pygame.draw.line(screen, colour, (turtle_x,turtle_y), (turtle_x + offset_x, turtle_y + offset_y))
            pygame.display.update() # You have to call update or you won't see anything
            # Update the turtle's position
            turtle_x += offset_x 
            turtle_y += offset_y

    # We've back outside the loop because hasQuit is now true, so close pygame properly
    print("Shutting down Pygame")
    pygame.quit()
        

#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()

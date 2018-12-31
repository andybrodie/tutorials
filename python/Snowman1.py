from pygame.locals import *
import pygame
import pygame.key
import string
import sys
import random

# Initialise Pygame and set up a window
pygame.init()
pysurf = pygame.display.set_mode((1024,768))
width, height = pysurf.get_size()
scale = 10
snX = width / 2 - (scale * 10)
snY = 10

# Set up some colours
WHITE = (255,255,255)
YELLOW = (255,255,0)

def drawSnowman():
    count = 0
 
    if (count == badGuesses): return False
    count += 1

    # Ground
    snDrawLine(0, 20, 20, 20);
    if (count == badGuesses): return False
    count += 1

    # Body
    snDrawCircle(10, 15, 5);
    if (count == badGuesses): return False
    count += 1

    # Head
    snDrawCircle(10, 7, 3);
    if (count == badGuesses): return False
    count += 1

    # Hat
    snDrawLine(8, 1, 12, 1);
    snDrawLine(12, 1, 12, 3);
    snDrawLine(12, 3, 14, 3);
    snDrawLine(8, 1, 8, 3);
    snDrawLine(6, 3, 8, 3);
    snDrawLine(6, 3, 6, 4);
    snDrawLine(14, 3, 14, 4);
    snDrawLine(6, 4, 14, 4);
    if (count == badGuesses): return False
    count += 1

    # Buttons
    snDrawCircle(10, 12, 1);
    snDrawCircle(10, 15, 1);
    snDrawCircle(10, 18, 1);
    if (count == badGuesses): return False
    count += 1

    # Arms
    snDrawLine(2, 15, 5, 15);
    if (count == badGuesses): return False
    count += 1
    snDrawLine(15, 15, 17, 15);
    if (count == badGuesses): return False
    count += 1

    # Eyes
    snDrawCircle(11, 6, 0.3);
    snDrawCircle(9, 6, 0.3);

    return True


def snDrawLine(x1, y1, x2, y2):
    pygame.draw.line(pysurf, WHITE, (x1 * scale + snX, y1 * scale + snY), (x2 * scale + snX, y2 * scale + snY),3);
    
def snDrawCircle(x, y, radius):
    pygame.draw.circle(pysurf, WHITE, (int(snX + x * scale), int(snY + y * scale)), int(radius * scale),3)

def drawGame():
    drawSnowman()
    drawLetters()
    pygame.display.update() # Tell Python to update the screen

def initGame():
    global badGuesses
    badGuesses = 4
    global words
    words = ( "POINTLESS", "COMPUTER", "DECORATE", "CONSTRUCT", "PERIMETER" )
    global word
    word = random.choice(words)

    global letters
    letters = list(string.ascii_uppercase)

def drawText(text, x, y, size, colour):
    myfont = pygame.font.SysFont('monospace', size)
    printedText = myfont.render(text, True, colour)
    pysurf.blit(printedText, (x, y))
    
def drawLetters():
    posY = 350
    letterSpace = width / 26
    count = 0
    # Print out all the letters that are in the list of available letters
    for x in list(string.ascii_uppercase):
        if x in letters:  
            drawText(x, letterSpace * count, posY, 64, (255,255,255))
        count = count + 1


done = False
clock = pygame.time.Clock()
initGame()
drawGame()

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT: ## defined in pygame.locals
           done = True

pygame.quit()

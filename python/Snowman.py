from pygame.locals import *
import pygame
import pygame.key
import string
import sys
import random

# Initialise some words
pygame.init()
pysurf = pygame.display.set_mode((1024,768))
width, height = pysurf.get_size()
scale = 10
snX = width / 2 - (scale * 10)
snY = 10

# Set up some colours
WHITE = (255,255,255)
YELLOW = (255,255,0)

letters = ()
badGuesses = 0
gameLost = False
gameWon = False

def initGame():
    global letters
    letters = list(string.ascii_uppercase)
    
    global words
    words = ("COMPUTER", "PRICELESS")
    global word
    word = random.choice(words)

def drawSnowman():
    count = 0;

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
    
    snDrawCircle(11, 6, 0.3);
    snDrawCircle(9, 6, 0.3);

    return True

def snDrawLine(x1, y1, x2, y2):
        pygame.draw.line(pysurf, WHITE, (x1 * scale + snX, y1 * scale + snY), (x2 * scale + snX, y2 * scale + snY),3);
    
def snDrawCircle(x, y, radius):
    pygame.draw.circle(pysurf, WHITE, (int(snX + x * scale), int(snY + y * scale)), int(radius * scale),3)


def drawLetters():
    posY = 350
    letterSpace = width / 26
    count = 0
    # Go through all the letters, A-Z and print out any that are in the list of available letters
    for x in list(string.ascii_uppercase):
        if x in letters:  
            drawText(x, letterSpace * count, posY, 64, (255,255,255))
        count = count + 1

def drawWord():
    # Draw the letter marks for the guessed word, along with any correctly guessed letters
    posY = 250
    letterSpace = width / 26
    posX = (width / 2) - (letterSpace * len(word)/2)

    # Iterate over all the letters in word by turning it in to a list
    lettersGuessed = 0
    count = 0
    for x in list(word):
        if x not in letters:
            drawText(x, posX + letterSpace * count, posY, 64, (255,255,0))
            lettersGuessed += 1
        drawText("_", posX + letterSpace * count, posY, 64, (255,255,255))
        count = count + 1

    return lettersGuessed == len(word)
    

def drawText(text, x, y, size, colour):
    myfont = pygame.font.SysFont('monospace', size)
    printedText = myfont.render(text, True, colour)
    pysurf.blit(printedText, (x, y))

def drawTextMiddle(text, size, colour):
    myfont = pygame.font.SysFont('monospace', size)
    printedText = myfont.render(text, True, colour)
    textWidth, textHeight = myfont.size(text)
    x = (width - textWidth) / 2
    y = (height - textHeight) / 2
    pysurf.blit(printedText, (x, y))
    

def drawGameLost():
    drawTextMiddle("GAME OVER!", 64, (255,0,0))
     

def drawGameWon():
    drawTextMiddle("YOU WON!", 64, (0,255,0))

def drawGame():
    global gameLost
    global gameWon
    gameLost = drawSnowman()
    drawLetters()
    gameWon = drawWord()

    if (gameLost):
        drawGameLost()

    if (gameWon):
        drawGameWon()
    
    pygame.display.update()

def processKey(key):
    global letters
    pysurf.fill((0,0,0))
    key = key.upper()
    if (key.upper() in letters):
        if (key not in word):
            global badGuesses
            badGuesses = badGuesses + 1
        letters.remove(key)
        drawGame()

    

done = False
initGame()
drawGame()

while not done:
    for event in pygame.event.get():
        if event.type == QUIT: ## defined in pygame.locals
           done = True

        if (gameLost):
            # Manage game over scenario
            if (event.type == pygame.KEYDOWN):
                done = True
        elif (gameWon):
            # Print you have won
            if (event.type == pygame.KEYDOWN):
                done = True
        else:
            if event.type == pygame.KEYDOWN:
                keyname = pygame.key.name(event.key)
                if (keyname == "escape"):
                    done = True
                else:
                    processKey(keyname)

pygame.quit()

import pygame
import time
import random

pygame.init()

display_width = 1000
display_height = 1000

black = (0,0,0)
brown = (200, 155, 105)
red = (255,0,0)

char_width = 73
char_height = 70

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

charImg = pygame.image.load('not the main.png')

#HEDGE CLASS
def hedge(hedgex, hedgey, hedgew, hedgeh, colour):
    pygame.draw.rect(gameDisplay, colour, [hedgex, hedgey, hedgew, hedgeh])

def char(x,y):
    gameDisplay.blit(charImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#FORMAT TEXT
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display("you crashed")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

#Character
    x_change = 0
    y_change = 0
#Hedge
    hedge_startx = 0
    hedge_starty = 0
    hedge_speed = 7
    hedge_width = 1000
    hedge_height = 75
    

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#CHARACTER MOVMEMENT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(brown)
        char(x,y)

#HEDGE
        hedge(hedge_startx, hedge_starty, hedge_width, hedge_height, black)
        char(x,y)

        if x > display_width - char_width or x < 0:
            crash()
        if y > display_width - char_height or y < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

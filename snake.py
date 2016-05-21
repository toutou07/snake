#!/usr/bin/env python

#snake.py
#Plays the classic game of Snake
#Created by Andrew Davis
#Created on 5/21/2016
#Open source (SCL license)

#import libraries
import pygame, sys, time, random
from pygame.locals import *

#initialize pygame
pygame.init()

#create the fps clock
fpsClock = pygame.time.Clock()



#create the play surface
playSurface = pygame.display.set_mode((640,410))

#and caption it
pygame.display.set_caption("Snake")

#set the colors
redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)
grayColor = pygame.Color(150,150,150)

#define constants
EASY_FPS = 15
MED_FPS = 20
HARD_FPS = 25

#init global variables
score = 0 #the player's score
fps = EASY_FPS #the speed at which the game runs
snakePosition = [100,100] #where the snake's head starts
snakeSegments = [[100,100],[80,100],[60,100]] #where the snake's body starts
foodPosition = [300,300] #where the snake food starts
foodSpawned = 1 #is the food in the game currently?
direction = 'right' #where the snake is going
changeDirection = direction #where the snake will be going

#gameOver function - called when the game is over
def gameOver():
    #this font is shown at the game over screen
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    #now we render the font
    gameOverSurf = gameOverFont.render('Game Over', True, grayColor)
    #then we get a space to display it
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    #and display it
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    #wait 5 seconds
    time.sleep(5)
    #and quit the game
    pygame.quit()
    #and exit Python
    sys.exit()

#displayTitle function - displays title text
def displayTitle():
    #fill the screen with black
    playSurface.fill(blackColor)
    #this font is used for the title
    titleFont = pygame.font.Font('freesansbold.ttf', 72)
    #now we render the font
    titleSurf = titleFont.render('Snake', True, grayColor)
    #get a space to display the text
    titleRect = titleSurf.get_rect()
    titleRect.midtop = (320, 10)
    #display the text
    playSurface.blit(titleSurf, titleRect)
    pygame.display.flip()

#this function selects a game mode 
def selectGameMode():
    displayTitle() #display the title
    #this font is used for the difficulty choices
    choiceFont = pygame.font.Font('freesansbold.ttf',32)
    #now we prepare four renderings, one per menu choice
    quitSurf = choiceFont.render('Quit', True, redColor)
    easySurf = choiceFont.render('Easy', True, redColor)
    medSurf = choiceFont.render('Medium', True, redColor)
    hardSurf = choiceFont.render('Hard', True, redColor)
    #then we display the renderings
    quitRect = quitSurf.get_rect()
    easyRect = easySurf.get_rect()
    medRect = medSurf.get_rect()
    hardRect = hardSurf.get_rect()
    quitRect.midtop = (320,300)
    easyRect.midtop = (120,200)
    medRect.midtop = (320,200)
    hardRect.midtop = (520,200)
    playSurface.blit(quitSurf, quitRect)
    playSurface.blit(easySurf, easyRect)
    playSurface.blit(medSurf, medRect)
    playSurface.blit(hardSurf, hardRect)
    pygame.display.flip()
    while True:
        #then we detect button presses
        for event in pygame.event.get():
            if event.type == QUIT: #if the user quits the game
                #quit pygame
                pygame.quit()
                #and exit Python
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN: #if the mouse was clicked
                if quitRect.collidepoint(pygame.mouse.get_pos()): #quit
                    #quit pygame
                    pygame.quit()
                    #and exit Python
                    sys.exit()
                elif easyRect.collidepoint(pygame.mouse.get_pos()): #easy mode
                    fps = EASY_FPS #set the fps variable
                    return #and exit the function
                elif medRect.collidepoint(pygame.mouse.get_pos()): #medium mode
                    fps = MED_FPS #set the fps variable
                    return #and exit the function
                elif hardRect.collidepoint(pygame.mouse.get_pos()): #hard mode
                    fps = HARD_FPS #set the fps variable
                    return #and exit the function

#this function displays the player's score in the top left-hand corner
#of the screen
def displayScore():
    #this font is used to display the score of the player
    scoreFont = pygame.font.Font('freesansbold.ttf',18)
    #now we turn the score into a string
    scoreStr = 'Score: ' + str(score)
    #now we render the score string
    scoreSurf = scoreFont.render(scoreStr, True, greenColor)
    #now we display it
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (45,10)
    playSurface.blit(scoreSurf, scoreRect)
                    
#select the game mode
selectGameMode()

#main loop of the game
while True:
    #check events
    for event in pygame.event.get():
        if event.type == QUIT: #if the user quits the game
            #then quit pygame
            pygame.quit()
            #and exit Python
            sys.exit()
        elif event.type == KEYDOWN: #if the user pressed a key
            #if the user pressed right or D
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = 'right'
            #if the user pressed left or A
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            #if the user pressed up or W
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = 'up'
            #if the user pressed down or S
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = 'down'
            #if the user pressed escape
            if event.key == K_ESCAPE:
                #quit the game
                pygame.event.post(pygame.event.Event(QUIT))
    #now we make sure the snake is not reversing itself
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection #assign the direction
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection #assign the direction
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection #assign the direction
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection #assign the direction

    #now we move the snake
    if direction == 'right': #if the snake is heading right
        snakePosition[0] += 20 #move the snake right
    if direction == 'left': #if the snake is heading left
        snakePosition[0] -= 20 #move the snake left
    if direction == 'down': #if the snake is heading down
        snakePosition[1] += 20 #move the snake down
    if direction == 'up': #if the snake is heading up
        snakePosition[1] -= 20 #move the snake up

    #grow the snake
    snakeSegments.insert(0, list(snakePosition))

    #check if food has been eaten
    if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
        foodSpawned = 0 #make the food not there
        score += 100 #add 100 points to the scoreboard
    else:
        snakeSegments.pop() #remove the last segment from the snake


    #add back the food
    if foodSpawned == 0:
        #place the food at random coordinates
        x = random.randrange(1,32) #new x-coord of the food
        y = random.randrange(1,24) #new y-coord of the food
        foodPosition = [int(x * 20), int(y* 20)] #
    foodSpawned = 1 #spawn the food

    #draw the objects to the screen
    playSurface.fill(blackColor) #fill the screen with black
    #draw the snake
    for position in snakeSegments:
        pygame.draw.rect(playSurface,whiteColor,Rect(position[0], position[1], 20,20))
    #draw the food
    pygame.draw.rect(playSurface, redColor, Rect(foodPosition[0], foodPosition[1], 20,20))
    #now we display the score
    displayScore()
    #refresh the display
    pygame.display.flip()

    #handle game over scenarios
    if snakePosition[0] > 620 or snakePosition[0] < 0: #out of bounds
        gameOver() #call the game over routine
    if snakePosition[1] > 390 or snakePosition[1] < 0: #out of bounds
        gameOver() #call the game over routine
    for snakeBody in snakeSegments[1:]:
        #if the snake has collided with itself
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            gameOver() #call the game over routine
    #set the game timer
    fpsClock.tick(fps)
       
            

# Snake Game

import pygame
import sys
import random
import time

check_errors=pygame.init()

if(check_errors[1]>0):
    print("(!) Had {0} initializing errors, exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+)PyGame successfully initiated!")

playSurface=pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake Game!')

red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
brown=pygame.Color(165,42,42)
blue=pygame.Color(0,0,255)

fpsController=pygame.time.Clock()

snakePos = [100, 50]
snakeBody = [[100, 50],[90, 50],[80, 50]]

foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
foodSpawn=True

direction = 'RIGHT'
changeto = direction

score = 0

level=0

def gameOver():
    myFont=pygame.font.SysFont('Comic Sans Ms', 72)
    GOSurf=myFont.render('Game Over!', True, red)
    GORect=GOSurf.get_rect()
    GORect.midtop=(360, 15)
    playSurface.blit(GOSurf, GORect)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

def showScore(choice=1):
    myFont=pygame.font.SysFont('Comic Sans Ms', 24)
    Score=myFont.render('Score: '+str(score), True, black)
    ScoreRect=Score.get_rect()
    if choice==1:
        ScoreRect.midtop=(80,10)
    else:
        ScoreRect.midtop=(360, 120)
    playSurface.blit(Score, ScoreRect)

def levelup():
    myFont=pygame.font.SysFont('Comic Sans Ms', 48)
    Level=myFont.render('Level Up!!', True, blue)
    LevelRect=Level.get_rect()
    LevelRect.midtop=(360,15)
    playSurface.blit(Level,LevelRect)
    pygame.display.flip()
    time.sleep(2)

speed = 10
counter=0

while(1):
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif(event.type==pygame.KEYDOWN):
            if event.key==pygame.K_RIGHT or event.key==ord('d'):
                changeto='RIGHT'
            if event.key==pygame.K_LEFT or event.key==ord('a'):
                changeto='LEFT'
            if event.key==pygame.K_UP or event.key==ord('w'):
                changeto='UP'
            if event.key==pygame.K_DOWN or event.key==ord('s'):
                changeto='DOWN'
            if event.key==pygame.K_ESCAPE:
                pygame.event.post(pygame.event.EVENT(pygame.QUIT))
    if changeto=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if changeto=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if changeto=='UP' and not direction=='DOWN':
        direction='UP'
    if changeto=='DOWN' and not direction=='UP':
        direction='DOWN'
    
    if direction=='RIGHT':
        snakePos[0]+=10
    if direction=='LEFT':
        snakePos[0]-=10
    if direction=='UP':
        snakePos[1]-=10
    if direction=='DOWN':
        snakePos[1]+=10

    snakeBody.insert(0,list(snakePos))
    if snakePos[0]==foodPos[0] and snakePos[1]==foodPos[1]:
        foodSpawn=False
        score+=1
    else:
        snakeBody.pop()
        if foodSpawn==False:
            foodPos=[random.randrange(1,72)*10, random.randrange(1,46)*10]
            for pos in snakeBody:
                if foodPos[0]==pos[0] and foodPos[1]== pos[1]:
                    foodPos=[random.randrange(1,72)*10, random.randrange(1,46)*10]
            foodSpawn=True
    
    playSurface.fill(white)
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

    if snakePos[0]>710 or snakePos[0]<0 or snakePos[1]>450 or snakePos[1]<0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0]==block[0] and snakePos[1]==block[1]:
            gameOver()
    
    showScore()
    pygame.display.flip()
    if score%10 == 0 and not score == 0:
            if counter==0:
                levelup()
                counter+=1
                speed+=5

    else:
        counter=0

    fpsController.tick(speed)
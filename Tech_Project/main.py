# Libraries importing
import pygame                 # game dev friendly lib
from time import sleep        # time lib
from random import randrange  # rand lib


# Pygame's Inizialization
pygame.init()             # inizialize all the pygame's modules

pygame.font.init()        # inizilize all the fonts in pygame
# Variables (Pipe and Objects charateristics)
screen = pygame.display.set_mode((600, 300))
pipe_width = 30
space = 170
start = 600
score = 0
size = 100
x1 = start
x2 = start + space + pipe_width
x3 = start + 2 * (space + pipe_width)
gameover = False

v_pipes = 0
pipe_n = 3
gravity = 0

wide = 30
high = 30 
tailwide = 200
tailhigh = high
jump = True

# Variables (Physics)
x = 150   # starting point (x)
y = 150   # starting point (y)
vy = 0  # y axe velocity

cat = pygame.image.load ('cat.png')
catImg = pygame.transform.scale (cat, (wide,high))
tail = pygame.image.load ('coda.png')
tailImg = pygame.transform.scale (tail, (tailwide,tailhigh))
background_image = pygame.image.load ('background.jpeg')
pipeImg = pygame.image.load ('pipe.png')
pipeRev = pygame.image.load ('pipe reversed.png')
myfont = pygame.font.SysFont('Comic Sans MS', size)
sadcat = pygame.image.load('sadcat.png')
sadnyan = pygame.transform.scale(sadcat,(120,100))
game_over = pygame.image.load('gameover.png')
gameovertxt = pygame.transform.scale(game_over,(300,70))

def heights1():
  global height1, height21
  for i in range(0, pipe_n):
    height1 = randrange(50, 80)
    height21 = randrange(90,130)

def heights2():
  global height2,height22
  for i in range(0, pipe_n):
    height2 = randrange(90, 130)
    height22 = randrange(50,80)

def heights3():
  global height3,height23
  for i in range(0, pipe_n):
    height3 = randrange(60, 110)
    height23 = randrange(60,110)

heights1()
heights2()
heights3()

# Graphic render func
def render():
  # Varibles
  global x, y, high, wide,size, gameover, v_pipes, vy,x1,x2,x3, start, score
  screen.blit(background_image, (0,0))
  if not gameover:
   screen.blit(tailImg,(x-tailwide+20,y))
   screen.blit(catImg, (x, y))
   scoreboard = myfont.render(str(score), False,(255, 255, 255))
   screen.blit(scoreboard,(250,100))
  else:
    vy = 0
    v_pipes = 0
    screen.blit(sadnyan,(250,100))
    screen.blit(gameovertxt,(150,20))
    scoretxt = myfont.render(str(score), False,(255, 255, 255))
    screen.blit(scoretxt,(290,200))
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == 1:
     gameover = False
     x1 = start
     x2 = start + space + pipe_width
     x3 = start + 2 * (space + pipe_width)
     y = 150
     score = 0
# Pipes generator func
def Pipes():
  # Variables
  global pipe_width, space, pipe_width, x1, x2, x3, height1, height2, height3, height21, height22, height23, gameover
  
  if  not gameover:
   #1
   pipe1 = pygame.transform.scale(pipeImg,(pipe_width,height1))
   pipe21 = pygame.transform.scale(pipeRev,(pipe_width,height21))
   screen.blit(pipe1,(x1, 0))
   screen.blit(pipe21,(x1, 300 - height21))
   #2
   pipe2 = pygame.transform.scale(pipeImg,(pipe_width,height2))
   pipe22 = pygame.transform.scale(pipeRev,(pipe_width,height22))
   screen.blit(pipe2,(x2, 0))
   screen.blit(pipe22,(x2, 300 - height22))
   #3
   pipe3 = pygame.transform.scale(pipeImg,(pipe_width,height3))
   pipe23 = pygame.transform.scale(pipeRev,(pipe_width,height23))
   screen.blit(pipe3,(x3, 0))
   screen.blit(pipe23,(x3, 300 - height23))

def clouds():
  global gameover

  if not gameover:
   pygame.draw.circle(screen, (255, 255, 255), (0, 20), 50, 0)
   pygame.draw.circle(screen, (255, 255, 255), (0, 80), 50, 0)
   pygame.draw.circle(screen, (255, 255, 255), (0, 120), 50, 0)
   pygame.draw.circle(screen, (255, 255, 255), (0, 180), 50, 0)
   pygame.draw.circle(screen, (255, 255, 255), (0, 240), 50, 0)
   pygame.draw.circle(screen, (255, 255, 255), (0, 280), 50, 0)

def collision():
  global x1, x2, x3, pipe_width, x, y, height1, height2, height3, height21, height22, height23, high, wide, v_pipes, vy, gameover
  if x1 - wide < x < x1 + pipe_width:
   if not height1 < y < 300 - height21 - high:
     gameover = True
  if x2 - wide < x < x2 + pipe_width:  
   if not height2 < y < 300 - height22 - high:
     gameover = True
  if x3 - wide < x < x3 + pipe_width:
   if not height3 < y < 300 - height23 - high:
     gameover = True
  
def border_collision():
  global x, y, radius, vy, v_pipes, gameover
  if y <= 0 or y + high >= 300:
   gameover = True

# Frame scroller func
def Next_State():
  # Variables
  global pipe_x, v_pipes, x, y, vx, vy, x1, x2, x3, start, jump,score, pipe_width, gravity
  collision()
  border_collision()
  pygame.event.get()
  keys = pygame.key.get_pressed()
  if not gameover:
   if keys[pygame.K_SPACE] == 1:
     v_pipes = -8
     gravity = 0.4
     if not jump:
       vy = -5
       jump=True
   else:
     jump=False
  if x1 <= 0:
    x1 = start
    heights1()
  if x2 <= 0:
    x2 = start
    heights2()
  if x3 <= 0:
    x3 = start
    heights3()
  if x == x1 + pipe_width:
    score += 1
  if x == x2 + pipe_width:
    score += 1
  if x == x3 + pipe_width:
    score += 1 
  vy = vy + gravity
  y += vy
  x1 += v_pipes
  x2 += v_pipes
  x3 += v_pipes


# Main programm
while True:
  render()
  Pipes()
  clouds()
  Next_State()
  pygame.display.flip() #solves the lag problem
  sleep(0.04)
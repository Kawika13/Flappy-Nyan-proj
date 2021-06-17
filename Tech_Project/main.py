# Libraries importing
import pygame                 # game dev friendly lib
from time import sleep        # time lib
from random import randrange  # rand lib


# Pygame's Inizialization
pygame.init()       # inizialize all the pygame's modules
pygame.font.init()  # inizilize all the fonts in pygame


# Screen Obj Instantiate
screen = pygame.display.set_mode((600, 300))

# Variables (Pipe and Objects charateristics)
# Sizes
pipe_width = 30

# Positions&Physics
space = 170
start = 600
x1 = start
x2 = start + space + pipe_width
x3 = start + 2 * (space + pipe_width)
v_pipes = -2
pipe_n = 3

# Variables (Font)
# Sizes
font_size = 100

# Variables (Playable Character)
# Sizes
wide = 30
high = 30 
tailwide = 200
tailhigh = high

# Positions&Physics
x = 150   # starting point (x)
y = 150   # starting point (y)
vy = 0.1  # y axe velocity

# States
jump = True
score = 0


# File Uploading
cat = pygame.image.load ('cat.png')
catImg = pygame.transform.scale (cat, (wide,high))
tail = pygame.image.load ('coda.png')
tailImg = pygame.transform.scale (tail, (tailwide,tailhigh))
background_image = pygame.image.load ('background.jpeg')
pipeImg = pygame.image.load ('pipe.png')
pipeRev = pygame.image.load ('pipe reversed.png')
myfont = pygame.font.SysFont('Comic Sans MS', font_size)


# Heights random generator funcs
def first_high():
  # Variables
  global height1, height21
  # Generation
  for i in range(0, pipe_n):
    height1 = randrange(50, 80)
    height21 = randrange(90,130)

def second_high():
  # Variables
  global height2, height22
  # Generation
  for i in range(0, pipe_n):
    height2 = randrange(90, 130)
    height22 = randrange(50,80)

def third_high():
  # Variables
  global height3, height23
  # Generation
  for i in range(0, pipe_n):
    height3 = randrange(60, 110)
    height23 = randrange(60,110)

# Random heights generation
first_high()
second_high()
third_high()

# Graphic render func
def render():
  # Varibles
  global x, y, high, wide, font_size
  
  screen.blit(background_image, (0,0))
  screen.blit(tailImg,(x-tailwide+20,y))
  screen.blit(catImg, (x, y))
  scoreboard = myfont.render(str(score), False,(255, 255, 255))
  screen.blit(scoreboard,(250,100))

# Pipes generator func
def Pipes():
  # Variables
  global pipe_width, space, pipe_width, x1, x2, x3, height1, height2, height3, height21, height22, height23
  # First Pipe
  pipe1 = pygame.transform.scale(pipeImg,(pipe_width,height1))
  pipe21 = pygame.transform.scale(pipeRev,(pipe_width,height21))
  screen.blit(pipe1,(x1, 0))
  screen.blit(pipe21,(x1, 300 - height21))
  # Second Pipe
  pipe2 = pygame.transform.scale(pipeImg,(pipe_width,height2))
  pipe22 = pygame.transform.scale(pipeRev,(pipe_width,height22))
  screen.blit(pipe2,(x2, 0))
  screen.blit(pipe22,(x2, 300 - height22))
  # Third Pipe
  pipe3 = pygame.transform.scale(pipeImg,(pipe_width,height3))
  pipe23 = pygame.transform.scale(pipeRev,(pipe_width,height23))
  screen.blit(pipe3,(x3, 0))
  screen.blit(pipe23,(x3, 300 - height23))

def clouds():
  pygame.draw.circle(screen, (255, 255, 255), (0, 20), 50, 0)
  pygame.draw.circle(screen, (255, 255, 255), (0, 80), 50, 0)
  pygame.draw.circle(screen, (255, 255, 255), (0, 120), 50, 0)
  pygame.draw.circle(screen, (255, 255, 255), (0, 180), 50, 0)
  pygame.draw.circle(screen, (255, 255, 255), (0, 240), 50, 0)
  pygame.draw.circle(screen, (255, 255, 255), (0, 280), 50, 0)

def collision():
  global x1, x2, x3, pipe_width, x, y, height1, height2, height3, height21, height22, height23, high, wide, v_pipes, vy
  if x1 - wide < x < x1 + pipe_width:
   if not height1 < y < 300 - height21 - high:
     v_pipes = 0
     vy = 0
  if x2 - wide < x < x2 + pipe_width:  
   if not height2 < y < 300 - height22 - high:
     v_pipes = 0
     vy = 0
  if x3 - wide < x < x3 + pipe_width:
   if not height3 < y < 300 - height23 - high:
     v_pipes = 0
     vy = 0
  
def border_collision():
  global x, y, radius, vy, v_pipes
  if y <= 0 or y + high >= 300:
    v_pipes = 0
    vy = 0

# Frame scroller func
def Next_State():
  # wait for keyboard inputs
  pygame.event.get()
  # Variables
  global pipe_x, v_pipes, x, y, vx, vy, x1, x2, x3, start, jump,score, pipe_width
  keys = pygame.key.get_pressed()
  collision()
  border_collision()
  if vy == 0:
    pass
  else:
    vy = vy + 0.1
    if keys[pygame.K_SPACE] == 1:
      if not jump:
        vy = -3
        jump=True
      else:
        jump=False
  if x1 <= 0:
    x1 = start
    first_high()
  if x2 <= 0:
    x2 = start
    second_high()
  if x3 <= 0:
    x3 = start
    third_high()
  if x == x1 + pipe_width:
    score += 1
  if x == x2 + pipe_width:
    score += 1
  if x == x3 + pipe_width:
    score += 1
    
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
  sleep(0.02)

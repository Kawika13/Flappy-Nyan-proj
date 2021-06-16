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
pipe_color = (0, 255, 0)
space = 170
start = 600
x1 = start
x2 = start + space + pipe_width
x3 = start + 2 * (space + pipe_width)

v_pipes = -2
pipe_n = 3
objColor = (255, 100, 0)

flappyImg = pygame.image.load ('flappy.png')
flappyImg = pygame.transform.scale (flappyImg, (150,80))
background_image = pygame.image.load ('background.jpeg')

radius = 20 # Pg circle radius

# Variables (Physics)
x = 0   # starting point (x)
y = 150   # starting point (y)
vy = 0.1  # y axe velocity

def heights1():
  global height1,height21
  for i in range(0, pipe_n):
    height1 = randrange(50, 120)
    height21 = randrange(50,120)

def heights2():
  global height2,height22
  for i in range(0, pipe_n):
   height2 = randrange(50, 120)
   height22 = randrange(50,120)

def heights3():
  global height3,height23
  for i in range(0, pipe_n):
   height3 = randrange(50, 120)
   height23 = randrange(50,120)

heights1()
heights2()
heights3()

# Graphic render func
def render():
  # Varibles
  global x, y, radius
  screen.blit(background_image, [0,0])
  screen.blit(flappyImg, (x, y))
  pygame.display.flip()

# Pipes generator func
def Pipes():
  # Variables
  global pipe_width, pipe_color,space,pipe_width,x1,x2,x3,height1,height2,height3,height21,height22,height23
  #1
  pygame.draw.rect(screen,pipe_color,(x1, 0, pipe_width, height1))
  pygame.draw.rect(screen,pipe_color,(x1, 300 - height21,pipe_width, height21))
  #2
  pygame.draw.rect(screen,pipe_color,(x2, 0, pipe_width, height2))
  pygame.draw.rect(screen,pipe_color,(x2, 300 - height22,pipe_width, height22))
  #3
  pygame.draw.rect(screen,pipe_color,(x3, 0, pipe_width, height3))
  pygame.draw.rect(screen,pipe_color,(x3, 300 - height23,pipe_width, height23))

  pygame.display.flip()

def clouds():
  pygame.draw.circle(screen,(255,255,255),(0,20),50,0)
  pygame.draw.circle(screen,(255,255,255),(0,80),50,0)
  pygame.draw.circle(screen,(255,255,255),(0,120),50,0)
  pygame.draw.circle(screen,(255,255,255),(0,180),50,0)
  pygame.draw.circle(screen,(255,255,255),(0,240),50,0)
  pygame.draw.circle(screen,(255,255,255),(0,280),50,0)

  pygame.display.flip()

def collision():
  global pipe_x,pipe_width,pipe_height,i,x,y
  
def border_collision():
  global x,y,radius,vy,v_pipes
  if y-radius<=0 or y+radius>=300:
    pass
    #vy=0
    #v_pipes=0

# Frame scroller func
def Next_State():
  # wait for keyboard inputs
  pygame.event.get()
  # Varibles
  global pipe_x, v_pipes, x, y, vx, vy, x1, x2, x3, start
  keys = pygame.key.get_pressed()
  if collision()==True:
    print("collision")
  border_collision()
  if vy == 0:
    pass
  else:
    vy = vy + 0.1
    if keys[pygame.K_SPACE] == 1:
      vy = -3
  if x1 <= 0:
    x1 = start
    heights1()
  if x2 <= 0:
    x2 = start
    heights2()
  if x3 <= 0:
    x3 = start
    heights3()
  y = y + vy
  x1 += v_pipes
  x2 += v_pipes
  x3 += v_pipes


# Main programm
while True:
  render()
  Pipes()
  clouds()
  Next_State()
  sleep(0.01)

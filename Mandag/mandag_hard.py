
'''Denne oppgaven krever litt mer kunnskap i Python enn "easy" og "medium" og du må ha
litt erfaring med OOP (object orientert programming). Her skal du jobbe
med klasser. hvis du ikke vet hva en klasse er, så kan du velge oppgaver 
i level "easy" eller "medium".
'''

############ Your task #########
''' 
   Your taks is to implement the method "intersect_rectangle_circle"
   the main purpose of this method is to determinate the effect when the ball collides 
   with the paddel: speed of the ball after collision and direction of the ball. 
'''

import pygame as p
from pygame import Vector2, event, sprite
import random as r
import os
from random import randint
import sys
import numpy as np

p.init

black = (0, 0, 0)
blue = (0, 0, 200)
seablue = (0, 10, 120)
yellow = (255, 165, 0)
green = (0, 255, 0)
orange = (255, 165, 0)
aqua = (0, 128, 128)
purple = (255, 0, 255)
roj = (255, 0, 0)
white = (255, 255, 255)

# #blocks
BLOCKWIDTH = 90
BLOCKHEIGHT = 45

#paddel
pad_width = 220
pad_heidht = 40

# Screen / size / background 
scr = (w, h) = 1300, 1031
scr = p.display.set_mode((w, h))
p.display.set_caption("Oppgave_1")
background_image = p.image.load("the_fall.jpg").convert()

# Screen Message after lose the ball 
p.font.init()
fuente = p.font.SysFont('Comic Sans MS', 120, bold=True, italic=False)
textscr_lose = fuente.render('GAME OVER', False, (white))
textscr_win = fuente.render('YOU WIN', False, (white))

clock = p.time.Clock()

class Ball(p.sprite.Sprite):
    def __init__(self,vel,x ,y, w =1300, h =1031):
        p.sprite.Sprite.__init__(self)
        self.pos = Vector2(x, y)
        self.radius = 15
        direction =(np.random.random(2)*2)
        self.velocity = (Vector2(*direction).normalize())
        direction = (np.random.random(2))
        self.acc = (Vector2(*direction).normalize())
        self.max_velocity = 8
        self.w = w
        self.h = h

    def update(self):

        if self.pos.x > self.w:
            self.velocity.x *= -1
        elif self.pos.x < 0:
            self.velocity.x *= -1

        if self.pos.y < 0:
            self.velocity.y *= -1

        self.pos += self.velocity
        if self.velocity.length() < self.max_velocity:
            self.velocity += self.acc
        

    def draw(self):
        p.draw.circle(scr, blue, (int(self.pos.x), int(self.pos.y)), self.radius)

class Paddle(p.sprite.Sprite):
    def __init__(self, color,x, y):

        self.mid_paddle = 110 
        self.paddle_rect = p.Rect(x, y, pad_width, pad_heidht)
        self.pad_pos = Vector2(x, y)
        self.color = color 
       
    def move(self):
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                self.paddle_rect.x -= 30
            elif event.key == p.K_RIGHT:
                self.paddle_rect.x += 30

    def draw(self):
        p.draw.rect(scr,self.color, self.paddle_rect)

    def collide_ball(self, ball):
        collided = intersect_rectangle_circle(self.paddle_rect, ball.pos, ball.radius, ball.velocity)
        if collided:
            if ball.pos.x > self.paddle_rect.x + 2*self.paddle_rect.w/3:
                prev_len = ball.velocity.length()
                ball.velocity = Vector2(1,-1) *prev_len
            elif ball.pos.x > self.paddle_rect.x + self.paddle_rect.w/3:
                prev_len = ball.velocity.length()
                ball.velocity = Vector2(0,-1) *prev_len
            elif ball.pos.x > self.paddle_rect.x:
                prev_len = ball.velocity.length()
                ball.velocity = Vector2(-1,-1) *prev_len

class Wall():
    def __init__(self, color, x, y):

        self.color = color
        self.rect = p.Rect(x,y,BLOCKWIDTH, BLOCKHEIGHT)
        
    def draw(self):
        p.draw.rect(scr, self.color, self.rect) 

def make_wall():
    WallList = []
    for i in range(15):
        for a in range(3):
            wall = Wall(r.choice(color), 100*i + 15, 100*a + 15)
            WallList.append(wall)

    return WallList  

# The following function is a copy extracted from vector.py file, on Assignment1 folder  
# and re-definded by me. 

def intersect_rectangle_circle(rect, circle_pos, circle_radius, circle_speed):
    

    # YOUR IMPLEMENTATION HERE
    # Position of the walls relative to the ball
    pass

# List of colors and objects
color = [green, yellow, roj, seablue, yellow, green, orange,purple]
Wall_list = make_wall()

p1 = Paddle(white, 500, 990)
paddle_list = [p1]    

b0 = Ball(Vector2(1,0).normalize(), r.randint(10,700), r.randint(100,650))
blist = [b0]




# ----------main loop---------------
while True:
    for event in p.event.get():
        if(event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE)):
            p.QUIT()
            sys.exit()
        
    time = clock.tick(60)
    
    scr.blit(background_image, [0, 0])
    for pad in paddle_list:
        pad.draw()
        pad.move()
        for balls in blist:
            pad.collide_ball(balls)
            
    for wall in Wall_list:
        wall.draw()
        for balls in blist:
            new_vel = intersect_rectangle_circle(wall.rect, balls.pos, balls.radius, balls.velocity)
            if new_vel != None:
                balls.velocity = new_vel
                Wall_list.remove(wall)

        if make_wall == 0:
            scr.blit(textscr_lose, (w/2, h/2))
    for balls in blist:
        balls.update()
        balls.draw()
        if balls.pos.y > h:
            scr.blit(textscr_win, (w/2, h/2))
        break
        
    p.display.update()
    

  


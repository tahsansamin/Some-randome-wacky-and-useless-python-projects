import pygame
from pygame import *
import time
import random



pygame.init()


screen = pygame.display.set_mode((800,700))
centre_flappy = [255,400]
descent_speed = 5
flappy_x = 255
flappy_y = 400
green = (0,255,0)
rad = 30
y_speed = 40
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
clock = pygame.time.Clock()
screen.fill(white)
score = 0
class Bird:
    def __init__(self,surface,color,centre,radius,width):
        self.surface = surface
        self.color = color
        self.centre = centre
        self.radius = radius
        self.width = width
    def draw_circle(self):
       
        pygame.draw.circle(self.surface,self.color,self.centre,self.radius,self.width)

font = pygame.font.SysFont('bahaus 93',30)
gameo_font = pygame.font.SysFont('bahaus 93',50)

xloc = 600
yloc = 0 
xsize = 100
ysize = random.randint(0,500)
def obstacle(xloc , yloc , xsize,ysize):
    pygame.draw.rect(screen,green, (xloc,yloc,xsize,ysize))
    pygame.draw.rect(screen,green, (xloc,yloc+ysize+150,xsize,500))
    



        
    


def game_loop():
    global flappy_y,flappy_x,descent_speed,xloc,ysize,xsize,score,font,rad,yloc,gameo_font
    game_over = False
    ground_y = 650
    
        
    while not game_over:
        
        f_score = 'score: '+str(score)
        score_text = font.render(f_score,False,(255,0,0))

        xloc -=4
        flappy = Bird(screen,red,(flappy_x,flappy_y),rad,0)
        flappy_y += descent_speed
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    
                    flappy_y -= y_speed
        if flappy_y + 25 >ground_y :
            game_over = True
            print('flappy')
        if flappy_y -25 <= 0:
            flappy_y +=2

        if xloc <= 0 :
            xloc = 600
            ysize = random.randint(0,500)
        if flappy_x > xloc+xsize:
            score += 1
        if flappy_x + rad >= xloc and flappy_x < xloc+xsize and flappy_y in range(yloc,yloc+ysize) or flappy_x + rad >= xloc and flappy_x < xloc+xsize and flappy_y in range(yloc+ysize+150,yloc+ysize+150+ysize)  :
            print('done')
            
            game_over = True
            
        screen.fill(white)
        
        pygame.draw.rect(screen,green,(0,ground_y,800,50))
        flappy.draw_circle()
        obstacle(xloc,yloc,xsize,ysize)
        screen.blit(score_text,(10,0))
        clock.tick(30)
        pygame.display.update()
        pygame.display.flip()

        
game_loop()

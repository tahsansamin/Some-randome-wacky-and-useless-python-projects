import pygame


pygame.init()

screen = pygame.display.set_mode((700,700))

screen.fill((255,255,255))

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
pink = (255,0,138)
width = 10
z = 0
black = (0,0,0)
current_color = red
font = pygame.font.SysFont('cambria',30)
text = font.render('Clear',False,(0,0,0))


   
pygame.display.set_caption('PyDoodle')    
    



def paint_loop():
    global z
    global width
    global current_color
    game_loop = False
    #different pixel sizes

    px1 = 5
    px2 = 10
    px3 = 15
    px4 = 20
    #creating the color buttons sixe


    c_size = 40

    while not game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                z=1
            if z == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                pygame.draw.circle(screen,current_color,(pos[0],pos[1]),width)
            if event.type == pygame.MOUSEBUTTONUP:
                z = 0
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(10,10+100) and pos[1] >= 620 and pos[1] < 620+50:
                print('clear')
                screen.fill((255,255,255))
            
                
                


            pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen,(83,77,89),(0,600,700,100))
            #drawing the button1 clear button
            pygame.draw.rect(screen,(89,223,132),(10,620,100,50))
            #drawing the different sizes
            pygame.draw.rect(screen,black,(200,650,10,10))
            pygame.draw.rect(screen,black,(240,650,20,20))
            pygame.draw.rect(screen,black,(280,650,25,25))
            pygame.draw.rect(screen,black,(320,650,30,30))
            #drawing the color buttons

            pygame.draw.rect(screen,green,(400,650,c_size,c_size))
            pygame.draw.rect(screen,red,(450,650,c_size,c_size))
            pygame.draw.rect(screen,blue,(500,650,c_size,c_size))
            pygame.draw.rect(screen,pink,(550,650,c_size,c_size))
        #check_press(cur_pos,circle_x,circle_y,rad)
            #checking for clicks in the pixel buttons
            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(200,200+10) and pos[1] >= 650 and pos[1] < 650+10:
                print('px1')
                width = px1
            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(240,240+20) and pos[1] >= 650 and pos[1] < 650+20:
                width = px2
                print('px2')
            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(280,280+25) and pos[1] >= 650 and pos[1] < 650+25:
                width = px3
                print('px3')
            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(320,320+30) and pos[1] >= 650 and pos[1] < 650+30:
                width=px4
                print('px4')
            #checking the clicks in the color buttons
            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(400,400+c_size) and pos[1] >= 650 and pos[1] < 650+c_size:
                current_color = green
            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(450,450+c_size) and pos[1] >= 650 and pos[1] < 650+c_size:
                current_color = red
            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(500,500+c_size) and pos[1] >= 650 and pos[1] < 650+c_size:
                current_color = blue
            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(550,550+c_size) and pos[1] >= 650 and pos[1] < 650+c_size:
                current_color = pink
            
        screen.blit(text,(10,620))
        pygame.display.update()
                
            


    


paint_loop()

















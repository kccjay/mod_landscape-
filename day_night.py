# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import os 
import pygame
import random

# Initialize game engine
pygame.init()

# Window
'''change to 800, 600'''
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
D_GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
D_WHITE = (228, 228, 228)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BLACK = (0, 0, 0)
GREY = (230, 230, 230)
C_GREY = (182, 182, 182)
RAIN = (51, 153, 255)
W_GREY = (191, 191, 191)


#Images
llama = pygame.image.load('images/llama.png')
bats = pygame.image.load('images/bat.png')
turtle = pygame.image.load('images/turtle.png')
poke = pygame.image.load('images/pokeball.png')
kirby = pygame.image.load('images/kirby.png')
twitter = pygame.image.load('images/twitter.png')
mario = pygame.image.load('images/mario.png')
goku = pygame.image.load('images/goku.png')
pac = pygame.image.load('images/pac1.png')
c_llama = pygame.image.load('images/c_llama.png')


# sun/moon
s_pla = [575, 100]
s_vel = [0, 0]
sp = 5

#moveable llama
p_pla = [-60, 450]
p_vel = [0, 0]
psp = 5


#cloud
def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, moon, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, moon, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, moon, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, moon, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, moon, [x + 20, y + 20, 60, 40])

''' make clouds '''

num_clouds = 25
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    s = random.randrange(1, 3)
    loc = [x, y, s]
    clouds.append(loc)

daytime = True
lights_on = False
rain = True


#The rain drops
num_rain = 1000
rain = []
for i in range(num_rain):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    r = random.randrange(1,5)
    drops = [x, y, r, r]
    rain.append(drops)

# The bat army
num_bats = 6
colony = []
for i in range(num_bats):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    bat_loc = [x, y]
    colony.append(bat_loc)
    
def bbat(bat_loc):
    x = bat_loc[0]
    y = bat_loc[1]

    screen.blit(bats, (x, y))

# The Llama
num_llama = 4
l_herd = []
for i in range(num_llama):
    x = random.randrange(0, 800)
    y = random.randrange(400, 500)
    place = [x, y]
    l_herd.append(place)

def animal(place):
    x = place[0]
    y = place[1]

    screen.blit(llama, (x, y))
  
#Only for the sun and the moon
def draw_sun(s_pla):
    x = s_pla[0]
    y = s_pla[1]

    pygame.draw.ellipse(screen, YELLOW, [x, y, 100, 100])

def draw_moon(s_pla):
    x = s_pla[0]
    y = s_pla[1]

    pygame.draw.ellipse(screen, GREY, [x, y, 100, 100])

#The Turtles
num_turtle = 3
bale = []
for i in range(num_turtle):
    x = random.randrange(0, 800)
    y = random.randrange(450, 510)
    loc = [x, y]
    bale.append(loc)

def tturtle(loc):
    x = loc[0]
    y = loc[1]

    screen.blit(turtle, (x, y))


#The controlable characters
#appear from the left of the screen
def player(p_pla):
    x = p_pla[0]
    y = p_pla[1]

    screen.blit(switch, (x, y))

#Ghost
ghosts = []
for i in range(1):
    x = random.randrange(810, 850)
    y = random.randrange(0, 600)
    loc = [x, y]
    ghosts.append(loc)

def ghost(loc):
    x = loc[0]
    y = loc[1]

    screen.blit(pac, (x, y))




#Variables needed inside the loop
estella = True
droplets = True
planetary = True
bbbats = True
appear = True 
p2p = 1
number = 25
s_llama = 2

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 s_vel[0] = -sp
            elif event.key == pygame.K_RIGHT:
                 s_vel[0] = sp
            elif event.key == pygame.K_UP:
                 s_vel[1] = -sp
            elif event.key == pygame.K_DOWN:
                 s_vel[1] = sp
            elif event.key == pygame.K_KP5 or event.key == pygame.K_5:
                 droplets = not droplets
            elif event.key == pygame.K_F1:
                 bbbats = not bbbats
            elif event.key == pygame.K_w:
                 p_vel[1] = -psp
            elif event.key == pygame.K_a:
                 p_vel[0] = -psp
            elif event.key == pygame.K_d:
                 p_vel[0] = psp
            elif event.key == pygame.K_s:
                 p_vel[1] = psp
            elif event.key == pygame.K_LCTRL:
                 appear = not appear
            elif event.key == pygame.K_RALT:
                 p2p = p2p + 1
            elif event.key == pygame.K_RCTRL:
                 p2p = p2p - 1
            elif event.key == pygame.K_KP_MINUS:
                 s_llama = s_llama - 1
            elif event.key == pygame.K_KP_PLUS:
                 s_llama = s_llama + 1
            elif event.key == pygame.K_KP_ENTER:
                 s_llama = 0
                 
        elif event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT:
                 s_vel[0] = 0
             elif event.key == pygame.K_RIGHT:
                 s_vel[0] = 0
             elif event.key == pygame.K_UP:
                 s_vel[1] = 0
             elif event.key == pygame.K_DOWN:
                 s_vel[1] = 0
             elif event.key == pygame.K_w:
                 p_vel[1] = 0
             elif event.key == pygame.K_a:
                  p_vel[0] = 0
             elif event.key == pygame.K_d:
                  p_vel[0] = 0
             elif event.key == pygame.K_s:
                 p_vel[1] = 0
            # google 'pygame key constants' for more keys

         
    # Game logic
    s_pla[0] += s_vel[0]
    s_pla[1] += s_vel[1]
    p_pla[0] += p_vel[0]
    p_pla[1] += p_vel[1]
    
    ''' move clouds '''
    #clouds
    for c in clouds:
        c[0] -= c[2]

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)
            
    #The rain "5"
    for r in rain:
        r[0] -= 1
        r[1] += 7

        if r[1] > 620:
            r[0] = random.randrange(0, 1200)
            r[1] = random.randrange(-50, -1)

    #llamas
    for l in l_herd:
        l[0] += s_llama

        if l[0] > 850:
            l[0] = random.randrange(-75,-50)
            l[1] = random.randrange(400, 500)
            
    #bats
    for c in colony:
        if c[1] or c[0]:
            c[0] = random.randrange(0, 755)
            c[1] = random.randrange(0, 550)

    #A Ghost!!!!
    for g in ghosts:
        g[0] -= 2
        if g[0] < -75:
            g[0] = random.randrange(900, 1000)
            g[1] = random.randrange(0, 600)
            

    if s_pla[0] > 850:
        estella = not estella
        planetary = not planetary
        s_pla[0] = (-50)
    elif s_pla[0] < -75:
        estella = not estella
        planetary = not planetary
        s_pla[0] = (840)
    elif s_pla[1] < -75:
        estella = not estella
        planetary = not planetary
        s_pla[1] = (450)
    elif s_pla[1] > 475:
        estella = not estella
        planetary = not planetary
        s_pla[1] = (-50)
        
    
    '''
    if p_pla[0] > 850:
        p_pla[0] = (-75)
    elif p_pla[0] < -50:
        p_pla[0] = (848)
    elif p_pla[1] > 400:
        p_pla[1] = (420)
    elif p_pla[1] < 600:
        p_pla[1] = (599)
    '''

    #For the player characters
    if p2p == 1:
        switch = llama
    elif p2p == 2:
        switch = c_llama
    elif p2p == 3:
        switch = turtle
    elif p2p == 4:
        switch = goku
    elif p2p == 5:
        switch = kirby

        
   
    ''' set sky color '''
    if estella:
        sky = BLUE
    else:
        sky = BLACK

    ''' Sky
    if not droplets == estella:
        sky = BLUE
    elif droplets == estella:
        sky = W_GREY
    elif droplets == estella:
        sky = BLUE
    '''

    '''Set to Moon'''
    if estella:
        color = YELLOW
    else:
        color = GREY

    '''Set Clouds'''
    if estella:
        moon = WHITE

    else:
        moon = C_GREY

    ''' Dark Grass '''
    if estella:
        grass = GREEN
    else:
        grass = D_GREEN

    ''' Fence '''
    if estella:
        fence = WHITE
    else:
        fence = D_WHITE
    

    ''' set window color (if there was a house)'''
    if lights_on:
        window_color = YELLOW
    else:
        window_color = WHITE
        
    # Drawing code
    ''' sky '''
    screen.fill(sky)

    ''' sun and moon '''
    if estella:
        draw_sun(s_pla)
    else:
        draw_moon(s_pla)

    ''' grass '''
    pygame.draw.rect(screen, grass, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],[x+10, y+40], [x, y+40],[x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    '''llama'''
    for l in l_herd:
        animal(l)
        
    '''moving llama'''
    if appear:
        pass
    else:
        player(p_pla)
    

    '''turtles
    for b in bale:
        tturtle(b)
    '''
    
    '''bats'''
    if bbbats:
        pass
    else:
        for c in colony:
            bbat(c)

    '''A Ghost!!'''
    if estella:
        pass
    else:
        for g in ghosts:
            ghost(g)
    
    ''' rain '''
    if droplets:
         pass
    else:
         for drops in rain:
            pygame.draw.ellipse(screen, RAIN, drops)
    
    ''' clouds '''
    for c in clouds:
        draw_cloud(c)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()


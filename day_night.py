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
GREY = (242, 242, 242)
C_GREY = (182, 182, 182)
RAIN = (51, 153, 255)


#Images
llama = pygame.image.load('llama.png')

# sun/moon
s_pla = [575, 100]
s_vel = [0, 0]
sp = 5
'''
def draw_moon(s_pla):
    x = s_pla[0]
    y = s_pla[1]

    pygame.draw.ellipse(screen, WHITE, [x, y, 100, 100])
'''
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
    s = random.randrange(1, 2)
    loc = [x, y, s]
    clouds.append(loc)

daytime = True
lights_on = False
rain = True


#The rain drops
num_rain = 500
rain = []
for i in range(num_rain):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    r = random.randrange(1,5)
    drops = [x, y, r, r]
    rain.append(drops)

# The Llama
num_llama = 4
stand = []
for i in range(num_llama):
    x = random.randrange(0, 800)
    y = random.randrange(400, 500)
    v = random.randrange(1, 2)
    place = [x, y, v]
    stand.append(place)

def animal(place):
    x = place[0]
    y = place[1]

    screen.blit(llama, (x,y))

#for the sun 
hack = []
for i in range(1):
    s_pla
    hack.append(s_pla)
    

def draw_sun(s_pla):
    x = s_pla[0]
    y = s_pla[1]

    pygame.draw.ellipse(screen, YELLOW, [x, y, 100, 100])
    
estella = True



# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            '''
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            '''
            if event.key == pygame.K_LEFT:
                 s_vel[0] = -sp
            elif event.key == pygame.K_RIGHT:
                 s_vel[0] = sp
            elif event.key == pygame.K_UP:
                 s_vel[1] = -sp
            elif event.key == pygame.K_DOWN:
                 s_vel[1] = sp

        elif event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT:
                 s_vel[0] = 0
             elif event.key == pygame.K_RIGHT:
                 s_vel[0] = 0
             elif event.key == pygame.K_UP:
                 s_vel[1] = 0
             elif event.key == pygame.K_DOWN:
                 s_vel[1] = 0

            # google 'pygame key constants' for more keys

                
    # Game logic
    s_pla[0] += s_vel[0]
    s_pla[1] += s_vel[1]
    
    ''' move clouds '''
    for c in clouds:
        c[0] -= c[2]

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    for r in rain:
        r[0] -= 1
        r[1] += 7

        if r[1] > 620:
            r[0] = random.randrange(0, 1200)
            r[1] = random.randrange(-50, -1)
            
    for s in stand:
        s[0] += s[2]

        if s[0] > 850:
            s[0] = random.randrange(-100,-50)
            s[1] = random.randrange(400, 500)

    if s_pla[0] > 850:
        estella = not estella
        s_pla[0] = (-50)
    elif s_pla[0] < -75:
        estella = not estella
        s_pla[0] = (840)
        
        
        

    ''' set sky color '''
    if estella:
        sky = BLUE
    else:
        sky = BLACK

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

    #Toggle Rain 

    ''' set window color (if there was a house)'''
    if lights_on:
        window_color = YELLOW
    else:
        window_color = WHITE

    
        
    # Drawing code
    ''' sky '''
    screen.fill(sky)

    ''' sun and moon '''
    draw_sun(s_pla)

    ''' grass '''
    pygame.draw.rect(screen, grass, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],[x+10, y+40], [x, y+40],[x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    '''llama'''
    for s in stand:
        animal(s)    

    ''' rain ''' 
#    for drops in rain:
#        pygame.draw.ellipse(screen, RAIN, drops)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

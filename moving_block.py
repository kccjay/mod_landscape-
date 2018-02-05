# Imports
import pygame

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Moving Block"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Block
loc = [380, 280]
vel = [0, 0]
speed = 5

def draw_block(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.rect(screen, WHITE, [x, y, 40, 40])
    
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel[0] = speed

                
    # Game logic
    loc[0] += vel[0]
    
    # Drawing code
    screen.fill(BLACK)
    draw_block(loc)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

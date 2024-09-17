import pygame

## Moves a circle around on screen

## =================
## Constants:

pygame.init()
WIDTH      = 1280
HEIGHT     = 720 
screen     = pygame.display.set_mode((WIDTH, HEIGHT))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
clock      = pygame.time.Clock()
running    = True
dt         = 0

## =================
## Data definitions:

## =================
## Functions:

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")

    # render your game here
    pygame.draw.circle(screen, "red", player_pos, 40)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
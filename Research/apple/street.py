# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
imp = pygame.image.load("C:\\Users\\noahj\\OneDrive\\Pictures\\little guy.png").convert()
imp_1 = pygame.image.load("C:\\Users\\noahj\\OneDrive\\Pictures\\leaf.png").convert()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
rect_1 = pygame.Rect(random.randint(0,500), random.randint(0,500), 25, 25)

energy = 1.0
health = 1.0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    screen.blit(imp, (player_pos))
    screen.blit(imp_1, (rect_1))
    pygame.draw.rect(screen, "green", pygame.Rect(0,0, 80 * energy, 20))
    pygame.draw.rect(screen, "red", pygame.Rect(80 * energy,0, 80 * (1 - energy), 20))
    pygame.draw.rect(screen, "red", pygame.Rect(1200, 0, 80 * health, 20))
        

    keys = pygame.key.get_pressed()
    speed = 300
    moving = keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]
    if (not keys[pygame.K_LSHIFT] or not moving) and energy < 1:
        energy += dt/10
    if keys[pygame.K_LSHIFT] and energy > 0 and moving:
        speed = 600
        energy -= dt / 5
    if keys[pygame.K_t]:
        screen.fill("green")
    if keys[pygame.K_p]:
        screen.fill("purple")
    if keys[pygame.K_w]:
        player_pos.y -= speed * dt
    if keys[pygame.K_s]:
        player_pos.y += speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= speed * dt
    if keys[pygame.K_d]:
        player_pos.x += speed * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
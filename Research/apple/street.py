# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
imp = pygame.image.load("little guy.png").convert()
imp_1 = pygame.image.load("leaf1.png").convert()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
rect_1 = pygame.Rect(random.randint(0,500), random.randint(0,500), 60, 60)
game_over = False
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

    player_rect = pygame.Rect(player_pos, imp.get_size())
    screen.blit(imp, (player_pos))
    screen.blit(imp_1, (rect_1))
    pygame.draw.rect(screen, "yellow", pygame.Rect(0,0, 640 * energy, 20))
    pygame.draw.rect(screen, "red", pygame.Rect(640 * energy,0, 640 * (1 - energy), 20))
    pygame.draw.rect(screen, "green", pygame.Rect(640, 0, 640 * health, 20))
    pygame.draw.rect(screen, "red", pygame.Rect(640 + 640 * health,0, 640 * (1 - health), 20))
    up = True
    down = True
    left = True
    right = True
    if player_rect.colliderect(rect_1)and health >= 0:
        health -= dt/5
        if (health < 0):
            game_over = True
        if player_pos.x < rect_1.x and player_pos.y < rect_1.y:
            down = False
            right = False
        if player_pos.x >= rect_1.x and player_pos.y < rect_1.y:
            down = False
            left = False
        if player_pos.x < rect_1.x and player_pos.y >= rect_1.y:
            right = False
            up = False
        if player_pos.x >= rect_1.x and player_pos.y >= rect_1.y:
            left = False
            up = False
    if not player_rect.colliderect(rect_1) and health < 1:
        health += dt/30
    if game_over:
        screen.fill("black")
        pygame.display.flip()
        continue       

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
    if keys[pygame.K_w] and up:
        player_pos.y -= speed * dt
    if keys[pygame.K_s] and down:
        player_pos.y += speed * dt
    if keys[pygame.K_a] and left:
        player_pos.x -= speed * dt
    if keys[pygame.K_d] and right:
        player_pos.x += speed * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
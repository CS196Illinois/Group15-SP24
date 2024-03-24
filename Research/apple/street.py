# Example file showing a circle moving on screen
import pygame
import random
from pineapple import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
imp = pygame.image.load("little guy.png").convert()
imp_1 = pygame.image.load("leaf1.png").convert()

wall_top = pygame.Rect(0,40, 40, 580)
wall_right = pygame.Rect(1240,40, 40, 700)
wall_left = pygame.Rect(0,20 , 40, 700)
wall_bottom = pygame.Rect(0, 680, 1280, 40)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
obstacles = []
for _ in range(1):
  rect_1 = pygame.Rect(random.randint(40,1000), random.randint(60,620), 60, 60)
  obstacles.append(rect_1)
game_over = False
health = 1.0
player = Player(player_pos, 300, imp)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    player_rect = pygame.Rect(player.pos, imp.get_size())
    #screen.blit(imp, (player.pos))
    player.draw(screen)
    player.walls(screen, wall_bottom, wall_left, wall_right, wall_top)
    for obstacle in obstacles:
      screen.blit(imp_1, (obstacle))
    player.bars(screen)
    directions = {
    "up" : True,
    "down" : True,
    "left" : True,
    "right" : True,
    }
    player.collisions(obstacles, player_rect, dt, directions, game_over, screen)
    if player.health < 0:
        screen.fill("black")
        pygame.display.flip()
        continue       

    keys = pygame.key.get_pressed()
    moving = keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]
    player.move(keys, dt, directions, moving)
    player.pos.x = player.pos.x % screen.get_width()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
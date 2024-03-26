# Example file showing a circle moving on screen
import pygame
import random
from pineapple import *
from time import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
respawning = False
imp = pygame.image.load("little guy.png").convert()
imp_1 = pygame.image.load("leaf1.png").convert()
imp_cash =pygame.image.load("cash.png").convert()
wall_top = pygame.Rect(0,20, 40, 580)
wall_right = pygame.Rect(1240,40, 40, 700)
wall_left = pygame.Rect(0,40 , 40, 700)
wall_bottom = pygame.Rect(0, 680, 1280, 40)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
music = pygame.Rect(600, 320, 60, 60)
obstacles = []
for _ in range(1):
  rect_1 = pygame.Rect(random.randint(40,1000), random.randint(100,620), 60, 60)
  obstacles.append(rect_1)
game_over = False
health = 1.0
money = 0.0
player = Player(player_pos, 300, imp)
cash_1 = pygame.Rect(random.randint(200,1000), random.randint(250,570), 50, 50)
time_1 = time()

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
    screen.blit(imp_cash, cash_1)
    player.draw(screen)
    pygame.draw.rect(screen, "blue", music)
    player.walls(screen, wall_top, wall_bottom, wall_left, wall_right)
    for obstacle in obstacles:
      screen.blit(imp_1, (obstacle))
    player.bars(screen)
    directions = {
    "up" : True,
    "down" : True,
    "left" : True,
    "right" : True,
    }
    if player_rect.colliderect(cash_1):
      shove = 1
      if keys[pygame.K_LSHIFT] and player.energy > 0 and moving:
        shove = 10
      if keys[pygame.K_d] and (player.pos.x < cash_1.x):
        cash_1.x += shove
      if keys[pygame.K_w] and (player.pos.y >= cash_1.y):
        cash_1.y -= shove
      if keys[pygame.K_s] and (player.pos.y < cash_1.y):
        cash_1.y += shove
      if keys[pygame.K_a] and (player.pos.x >= cash_1.x):
        cash_1.x -= shove
      money += 1
    if player.pos.y <= 0 and not respawning:
      respawning = True
      time_1 = time()
      print(time_1)
    if respawning:
      screen.fill("black")
      pygame.display.flip()
      player.pos.x = screen.get_width() / 2
      player.pos.y = screen.get_height() / 2
      rect_1.x = random.randint(40,1000)
      rect_1.y = random.randint(100,620)
      money = 0
      cash_1.x = random.randint(200,1000)
      cash_1.y = random.randint(250,570)
      player.energy = 1
      player.health = 1
      money += 1
    if time() >= time_1 + 1:
      respawning = False
    if cash_1.x <= 40:
      cash_1.x = random.randint(200,1000)
    if (cash_1.x + 50 >= 1240):
      cash_1.x = random.randint(200,1000)
    if (cash_1.y <= 120):
      cash_1.y = random.randint(250,570)
    if ((cash_1.y + 50) >= 680):
      cash_1.y = random.randint(250,570)
    player.collisions(obstacles, player_rect, dt, directions, game_over, cash_1, money, screen)
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
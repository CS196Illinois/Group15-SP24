import pygame
import random
class Player(object):
    def __init__(self, pos, speed, img):
        self.pos = pos
        self.speed = speed
        self.img = img
        self.wall_top_img = pygame.image.load("wall_top.png").convert()
        self.wall_left_img = pygame.image.load("wall left.png").convert()
        self.wall_bottom_img = pygame.image.load("wall bottom.png").convert()
        self.health = 1.0
        self.energy = 1.0
    def draw(self, screen):
       screen.blit(self.img, self.pos)
    def move(self, keys, dt, directions, moving):
        speed = self.speed
        if (not keys[pygame.K_LSHIFT] or not moving) and self.energy < 1:
            self.energy += dt/10
        if keys[pygame.K_LSHIFT] and self.energy > 0 and moving:
            speed = speed * 2
            self.energy -= dt / 5
        if keys[pygame.K_w] and directions["up"]:
            self.pos.y -= speed * dt
        if keys[pygame.K_s] and directions["down"]:
            self.pos.y += speed * dt
        if keys[pygame.K_a] and directions["left"]:
            self.pos.x -= speed * dt
        if keys[pygame.K_d] and directions["right"]:
            self.pos.x += speed * dt
    def collisions(self, obstacles, player_rect, dt, directions, game_over, cash_1, money,screen):
        if self.pos.y <= 100:
            directions["up"] = False
            if (cash_1.x > 600 and cash_1.x < 660) and (cash_1.y > 320 and cash_1.y < 380) and self.pos.x >= 561 and self.pos.x <= 625:
                directions["up"] = True
        if self.pos.y >= 580:
            directions["down"] = False
        if self.pos.x <= 40:
            directions["left"] = False
        if self.pos.x >= 1140:
            directions["right"] = False
        for obstacle in obstacles:
            if (player_rect.colliderect(obstacle) or player_rect.colliderect(cash_1)) and self.health >= 0:
                self.health -= dt/1000
                if (self.health < 0):
                    game_over = True
                if (self.pos.x < obstacle.x and self.pos.y < obstacle.y) or (self.pos.x < cash_1.x and self.pos.y < cash_1.y):
                    directions["down"] = False
                    directions["right"] = False
                if (self.pos.x >= obstacle.x and self.pos.y < obstacle.y) or (self.pos.x >= cash_1.x and self.pos.y < cash_1.y):
                    directions["down"] = False
                    directions["left"] = False
                if (self.pos.x < obstacle.x and self.pos.y >= obstacle.y) or (self.pos.x < cash_1.x and self.pos.y >= cash_1.y):
                    directions["right"] = False
                    directions["up"] = False
                if (self.pos.x >= obstacle.x and self.pos.y >= obstacle.y) or (self.pos.x >= cash_1.x and self.pos.y >= cash_1.y):
                    directions["left"] = False
                    directions["up"] = False
            if not player_rect.colliderect(obstacle) and self.health < 1:
                self.health += dt/30
    def bars(self, screen):
        pygame.draw.rect(screen, "yellow", pygame.Rect(0,0, 640 * self.energy, 20))
        pygame.draw.rect(screen, "red", pygame.Rect(640 * self.energy,0, 640 * (1 - self.energy), 20))
        pygame.draw.rect(screen, "green", pygame.Rect(640, 0, 640 * self.health, 20))
        pygame.draw.rect(screen, "red", pygame.Rect(640 + 640 * self.health,0, 640 * (1 - self.health), 20))
    def walls(self, screen, wall_top, wall_bottom, wall_left, wall_right):
        screen.blit(self.wall_bottom_img, wall_bottom)
        screen.blit(self.wall_left_img, wall_right)
        screen.blit(self.wall_left_img, wall_left)
        screen.blit(self.wall_top_img, wall_top)

import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
# Render the graphics here.
class Player(object):
    def __init__(self, x, y, speed, img,):
        self.x = x
        self.y = y
        self.speed = speed
        self.img = img
        self.health = 1.0
        self.energy = 1.0
    def draw():
        pygame.draw.rect(self.x, self.y, self.speed, self.img)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("white")  # Fill the display with a solid color



    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
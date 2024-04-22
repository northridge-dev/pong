import pygame

pygame.init()
running = True  # game loop control flag

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

while running:
    clock.tick(60)  # throttle to 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

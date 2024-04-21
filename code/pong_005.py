import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

count = 0
events = 0

while count < 300:  # at 60 fps, 300 ticks will take 5 seconds
    clock.tick(60)  # throttle to 60 fps
    for event in pygame.event.get():
        events += 1
        print(event)
    count += 1

print("event count: ", events)

pygame.quit()

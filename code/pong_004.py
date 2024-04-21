import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

count = 0
events = 0

while count < 1e6:  # 1 million
    for event in pygame.event.get():
        events += 1
        print(event)
    count += 1

print("event count: ", events)

pygame.quit()

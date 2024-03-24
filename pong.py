import pygame

pygame.init()

# color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# game constants
FPS = 60
WIDTH, HEIGHT = 900, 700
TOP, BOTTOM = 0, HEIGHT
LEFT, RIGHT = 0, WIDTH
MID_HEIGHT = HEIGHT // 2
MID_WIDTH = WIDTH // 2

# create window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knight's Pong")


class Paddle:
    def __init__(self, side, up_key, down_key):
        self.width = 20
        self.height = 120
        self.padding = 10
        self.border_radius = 7
        self.side = side

        self.starting_x = (
            LEFT + self.padding if side == "left" else RIGHT - self.padding - self.width
        )
        self.starting_y = MID_HEIGHT - (self.height // 2)
        self.rect = pygame.Rect(
            self.starting_x, self.starting_y, self.width, self.height
        )
        self.up_key = up_key
        self.is_moving_up = False
        self.down_key = down_key
        self.is_moving_down = False

    def draw(self, window):
        pygame.draw.rect(window, BLACK, self.rect, 0, self.border_radius)

    def change_movement(self, key_pressed):
        if key_pressed == self.up_key:
            self.is_moving_up = not self.is_moving_up
        if key_pressed == self.down_key:
            self.is_moving_down = not self.is_moving_down

    def move(self):
        if self.is_moving_up and self.rect.top > TOP:
            self.rect.move_ip(0, -5)
        if self.is_moving_down and self.rect.bottom < BOTTOM:
            self.rect.move_ip(0, 5)

    def update(self):
        pass

    def check_collision(self):
        pass

    def check_bounds(self):
        pass

    def reset(self):
        pass


def draw_window(left_paddle, right_paddle):
    window.fill(WHITE)
    left_paddle.draw(window)
    right_paddle.draw(window)
    pygame.display.flip()


def main():
    left_paddle = Paddle("left", pygame.K_w, pygame.K_s)
    right_paddle = Paddle("right", pygame.K_UP, pygame.K_DOWN)

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                left_paddle.change_movement(event.key)
                right_paddle.change_movement(event.key)

        left_paddle.move()
        right_paddle.move()
        draw_window(left_paddle, right_paddle)

    pygame.quit()


if __name__ == "__main__":
    main()

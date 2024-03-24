import pygame

pygame.init()

# color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# game constants
FPS = 60
WIDTH, HEIGHT = 900, 600
TOP, BOTTOM = 0, HEIGHT
LEFT, RIGHT = 0, WIDTH
MID_HEIGHT = HEIGHT // 2
MID_WIDTH = WIDTH // 2

# create window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knight's Pong")


class Scoreboard:
    def __init__(self):
        pass

    def draw(self, window, left_score, right_score):
        font = pygame.font.Font(None, 200)
        left_score_text = font.render(str(left_score), True, BLACK)
        left_score_text.set_alpha(25)
        right_score_text = font.render(str(right_score), True, BLACK)
        right_score_text.set_alpha(25)
        window.blit(left_score_text, (LEFT + 200, MID_HEIGHT - 100))
        window.blit(right_score_text, (RIGHT - 200, MID_HEIGHT - 100))


class Ball:
    def __init__(self):
        self.radius = 10
        self.starting_x = MID_WIDTH
        self.starting_y = MID_HEIGHT
        self.starting_x_speed = 3.5
        self.x_speed = self.starting_x_speed
        self.starting_y_speed = 1.5
        self.y_speed = self.starting_y_speed
        self.x_direction = 1
        self.y_direction = 1
        self.rect = pygame.draw.circle(
            window, BLACK, (self.starting_x, self.starting_y), self.radius
        )

    def draw(self, window):
        pygame.draw.rect(window, BLACK, self.rect, 0, self.radius)

    def move(self):
        self.rect.move_ip(
            self.x_direction * self.x_speed, self.y_direction * self.y_speed
        )

    def check_wall_collision(self):
        if self.rect.top <= TOP or self.rect.bottom >= BOTTOM:
            self.y_direction *= -1

    def check_paddle_collision(self, left_paddle, right_paddle):
        if self.rect.colliderect(left_paddle.rect) or self.rect.colliderect(
            right_paddle.rect
        ):
            self.x_direction *= -1

            # increase speed by 10% on each paddle collision
            self.x_speed *= 1.1
            self.y_speed *= 1.1

    def check_point_scored(self, left_paddle, right_paddle):
        if self.rect.x <= left_paddle.score_line:
            right_paddle.score_point()
            self.reset()
        if self.rect.x >= right_paddle.score_line:
            left_paddle.score_point()
            self.reset()

    def reset(self):
        self.x_speed = self.starting_x_speed
        self.y_speed = self.starting_y_speed
        self.x_direction *= -1
        self.y_direction *= -1
        self.rect = pygame.draw.circle(
            window, BLACK, (self.starting_x, self.starting_y), self.radius
        )


class Paddle:
    def __init__(self, side, up_key, down_key):
        self.width = 20
        self.height = 120
        self.padding = 10
        self.border_radius = 7
        self.side = side
        self.score = 0
        self.score_line = (
            LEFT + self.padding if side == "left" else RIGHT - self.padding
        )

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

    def score_point(self):
        self.score += 1


def render(scoreboard, ball, left_paddle, right_paddle):
    window.fill(WHITE)
    scoreboard.draw(window, left_paddle.score, right_paddle.score)
    ball.draw(window)
    left_paddle.draw(window)
    right_paddle.draw(window)
    pygame.display.flip()


def check_collision(ball, left_paddle, right_paddle):
    ball.check_wall_collision()
    ball.check_paddle_collision(left_paddle, right_paddle)
    ball.check_point_scored(left_paddle, right_paddle)


def next_tick(ball, left_paddle, right_paddle):
    ball.move()
    left_paddle.move()
    right_paddle.move()


def main():
    ball = Ball()
    left_paddle = Paddle("left", pygame.K_w, pygame.K_s)
    right_paddle = Paddle("right", pygame.K_UP, pygame.K_DOWN)
    scoreboard = Scoreboard()

    paused = False

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

        if not paused:
            check_collision(ball, left_paddle, right_paddle)
            next_tick(ball, left_paddle, right_paddle)
            render(scoreboard, ball, left_paddle, right_paddle)

    pygame.quit()


if __name__ == "__main__":
    main()

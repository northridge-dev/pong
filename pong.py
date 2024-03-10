import turtle


def play_pong():
    # screen dimensions, borders
    screen_width = 800
    right_edge = screen_width / 2
    left_edge = -right_edge

    screen_height = 600
    top_edge = screen_height / 2
    bottom_edge = -top_edge

    middle = 0

    # initialize screen
    screen = turtle.Screen()
    screen.title("Knight's Pong")
    screen.bgcolor("black")
    screen.setup(width=screen_width, height=screen_height)
    screen.tracer(0)  # control screen updates with game loop

    # main game loop
    while True:
        screen.update()  # redraws screen on each tick


play_pong()

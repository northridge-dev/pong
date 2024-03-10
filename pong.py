import turtle

"""
Global constants
"""
# screen dimensions, borders
screen_width = 800
screen_height = 600
right_edge = screen_width / 2
left_edge = -right_edge
top_edge = screen_height / 2
bottom_edge = -top_edge
middle = 0

# font
font = ("Courier", 24, "normal")

"""
Game State
"""
score_right = 0
score_left = 0
winning_score = 7

"""
Window
"""
window = turtle.Screen()
window.title("Knight's Pong")
window.bgcolor("black")
window.setup(width=screen_width, height=screen_height)
window.tracer(0)  # control screen updates with game loop

""" 
Ball
"""
# add code here to initialize the ball

""" 
Left Paddle
"""
# add code here to initialize paddle A

""" 
Right Paddle
"""
# add code here to initialize paddle B


""" 
Scoreboard
"""
# add code here to initialize the scoreboard

"""
Message 
"""
message = turtle.Turtle()
message.color("white")

"""
Helper Functions
"""


def start_game():
    message.clear()  # clear start message
    play_pong()


def game_over():
    message.write("GAME OVER", align="center", font=font)
    message.sety(message.ycor() - 50)
    message.write(
        "Lefty wins!" if score_left > score_right else "Righty wins!",
        align="center",
        font=font,
    )


"""
Main Game Loop
"""


def play_pong():
    # main game loop
    if max(score_left, score_right) < winning_score:
        window.ontimer(play_pong, 1000 // 60)
    else:
        game_over()


"""
Event listeners
"""
window.onkey(start_game, "space")
window.listen()


message.write("Press space to start", align="center", font=font)
turtle.mainloop()

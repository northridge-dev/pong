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


"""
Game State
"""
score_a = 0
score_b = 0
winning_score = 5
higher_score = max(score_a, score_b)

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
Paddle A
"""
# add code here to initialize paddle A

""" 
Paddle B
"""
# add code here to initialize paddle B


""" 
Scoreboard
"""
# add code here to initialize the scoreboard

"""
Start Message 
"""
start_message = turtle.Turtle()
start_message.color("white")
start_message.write(
    "Press space to start", align="center", font=("Courier", 24, "normal")
)

"""
Helper Functions
"""


"""
Main Game Loop
"""


def play_pong():
    start_message.clear()  # clear start message

    # main game loop
    while higher_score < winning_score:
        window.update()  # redraws screen on each tick


"""
Event listeners
"""
window.onkey(play_pong, "space")
window.listen()


turtle.mainloop()

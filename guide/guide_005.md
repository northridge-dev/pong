# the game loop

Let's recap. We said that video games:

1. take in player input
2. keep track of game state and update it with player input
3. draw the current state of the game to the screen

Those three jobs have to be done again and again and again, 30 or 60 or
more times per second, for as long as the game is running. The same three jobs
"again and again and again" . . . that's a loop. **A game loop.**

Here's a little pseudocode to illustrate:

```text
game_is_running = True

while game_is_running:
    # important: we have to have some way(s) to break out of the game loop
    if player_quit or game_over:
      game_is_running = False

    process_player_input()
    update_game_state()
    draw_game()

```

The code we eventually write will be more complex, but it will follow this basic
pattern.

We'll use `pygame` to help us with handle player input, draw the game, and for a
few other things. The rest is up to us. Us and Python.

[<<](guide_004.md) | [>>](guide_006.md) | [ToC](toc.md)

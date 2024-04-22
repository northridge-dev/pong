# quitting the game

Now that we know how to listen for a `QUIT` event, we can change our `while`
loop logic. Instead of running a fixed number of times, we can let it run
forever because we can now send (and receive) a signal to kill it.

We need to make a few changes:

1. Remove the `count` and `events` variables. We don't need them anymore.2. Just
   after you initialize `pygame`, add a variable named `running` and set it
   equal to `True`. We'll call this variable the "game control flag."
2. Change the `while` loop condition to `while running:`.
3. Last, we need a way to toggle the `running` variable to `False`. Instead of
   printing a message when we receive a `QUIT` event, reassign `running` to
   `False`.

That's it. Now your code should look like this:

```python
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
```

Test it. The window should stay open until you click the "X" button. Once you
click it, the game window should close and your terminal should return to the
prompt (because Python will have no more instructions to execute).

We _could_ have called `pygame.quit` as soon as we detected the `QUIT` event,
but by using the control flag, we have more . . . control. For example, we might
want to try to save the game state or do other useful work before triggering a
hard exit.

[<<](guide_022.md) | [>>](guide_024.md) | [ToC](toc.md)

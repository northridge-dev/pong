# a loop to keep the game going

It's probably occurred to you that the `wait` function isn't a great solution.
If we need our game to recalculate and draw a frame every 1/60th of a second, we
can't just pause execution for 5 seconds. We need to keep the game running until
we tell it to stop.

Before we implement something better, let's clean up our throw-away code. Remove
the `wait` import and the `wait(5)` lines. This is what your `pong.py` file
should look like now:

```python
import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.quit()
```

We've discovered that we need to keep Python busy between the `set_mode` method
that opens the window and the `pygame.quit` method that closes it. Let's do one
more experiment. Insert this code in between the two:

```python
count = 0

while count < 5e7: # 50 million: a 5 followed by 7 zeros
    count += 1
```

This code makes Python count to 50 million. On my computer, that takes about 5
seconds. Consequently, when I run this code, the window stays open for about 5
seconds, just as we'd expect.

Try it yourself. When I ran the same code in a Codespace, it took about 8 or 10
seconds to finish. That's reasonable. You can adjust up or down as you wish, but
don't make the number _too_ big or you'll be waiting a long time.

[<<](guide_018.md) | [>>](guide_020.md) | [ToC](toc.md)

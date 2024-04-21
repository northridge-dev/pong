# game loop speed limit

We looked for events in the queue 1 million times and found maybe a few hundred
events. The queue was empty more than 99.9% of the times we looked and rarely or
never did we find more than one event in the queue. That's because the game loop
is running so fast. Even though processing the events made our loop ~50x slower,
we were still executing the loop ~200,000 times per second. Now _that's_ a fast
frame rate!

Too fast. And too variable. Imagine we were moving a pong ball 1 pixel on each
tick of the game loop. We'll discover that drawing surfaces slows down the loop
even more, but it still might be too fast. And we'd want the ball speed to move
just as fast on an old, slow computer as it moves on a blazingly fast one.

We can't make the game loop run faster than the computer can handle, but we can
slow it down or _throttle_ it. `pygame` gives us some tools. We only need a few
extra lines of code:

```python

clock = pygame.time.Clock()

count = 0
events = 0

while count < 300:  # at 60 fps, 300 "ticks" will be 5 seconds
  clock.tick(60)  # 60 frames per second
  for event in pygame.event.get():
    events += 1
      print(event)
  count += 1

print("event count: ", events)
```

`pygame.time.Clock()` creates a new clock object that we've stored in the
`clock` variable. Inside the `while` loop, we call the
[`tick` method](https://www.pygame.org/docs/ref/time.html?highlight=clock#pygame.time.Clock.tick)
on the object we stored at `clock`. Like the `wait` function we used earlier,
`tick` will pause the loop, but unlike `wait`, it can calculate how long to
pause execution in order to reach a (more or less) consistent frame rate.

Try it out. The window should stay open for 5 seconds on your computer or mine
and you should still see events like mouse movements and key strokes being
printed to the terminal screen.

[<<](guide_019.md) | [>>](guide_022.md) | [ToC](toc.md)

# listening for events

Obviously this counting loop isn't going to do the trick. But we can learn a few
important things if we stick with it just a bit longer.

We said that we have three tasks to accomplish in our game loop:

1. get and process player input
2. calculate the new state of the game
3. draw the next frame

Let's add that first task to our `while` loop.

`pygame` listens for _**events**_ that happen in the game window, for example:

- mouse movements
- mouse clicks
- key presses

As events occur, `pygame` puts them in a queue in the same order they're
received On each "tick" of the game loop, we can ask for all the events that
have been _enqueued_.

![event queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/220px-Data_Queue.svg.png)

Modify your loop to look like this:

```python
count = 0
events = 0

while count < 1e6: # 1 million
  for event in pygame.event.get():
    print(event)
    events += 1
  count += 1

print('event count: ', events)
```

- `pygame.event.get()` returns a list of all the events that have occurred since
  the last time it was called, and we loop through that list.
- We're counting and printing each event.
- When the loop ends, we'll print out the total number of events we processed.
- **Notice that we're only counting to 1 million now.** On my machine, adding
  just this minimal event handling made the loop 50x slower.

Run this code and try to trigger as many events as you can. Move your mouse
around the game window, click mouse buttons, and press keys. You should see a
stream of events being printed to your Codespace terminal. When the loop ends,
you'll see the total number of events processed. How many events did you
trigger?

[<<](/guide/guide_019.md) | [>>](/guide/guide_021.md) | [ToC](toc.md)

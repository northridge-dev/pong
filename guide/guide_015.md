# create a window

Almost every application you use on your computer creates a window.
(Incidentally, that's probably why Microsoft named their operating system
"Windows.") It's the operating system's job to create and manage windows;
`pygame` is asking the operating system (in our Codespace, that's Linux)
to create a window for us.

Here's `pygame`'s window-creating method. All that's required are the window's
dimensions, measured in pixels.

```python
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
```

We could have just passed the _tuple_ `(800, 600)` directly to
`pygame.display.set_mode`. But by creating variables for the window's width
and height, we can refer to them later in our program.

We also stored the return value from `pygame.display.set_mode` in a variable
called `window`. This is a reference to the display surface that `pygame`
created. We'll learn more about surfaces very soon. By storing a reference to
that surface, we can access it later in our program.

[<<](guide_0014.md) | [>>](guide_016.md) | [ToC](toc.md)

# Toolbox: Python & pygame

Python is well-suited to keeping track of game state. You already have some
experience using variables, lists, and dictionaries to store and retrieve
information.

But on it's own, Python isn't adept at processing player input or drawing to
the screen. So to handle player input and game output, we'll use a library
called [`pygame`](https://www.pygame.org/news).

`pygame` is Python code that interacts with some code written in C (a different
programming language). That C code specializes in interacting with the drivers
that control your computer's screen, keyboard, and mouse.(1) `pygame` also provides
a few other tools that make it easier to write games -- stuff like a way to load
and animate images, play sound, and detect collisions between objects.

---

## footnotes

(1) It is very common for tasks to require work orchestrated across multiple
abstraction layers, in this case: `pygame` & Python -> Simple
DirectMedia Layer (SDL) & C -> operating system -> drivers -> hardware.

[<<](guide_003.md) | [>>](guide_005.md) | [ToC](toc.md)

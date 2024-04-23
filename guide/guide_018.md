# experimenting with ways to keep the window open

Hypothesis: maybe the problem is that the `pygame.quit()` command is closing the
window too quickly. Let's experiment! Try commenting out the command and running
the code again.

```python
# pygame.quit()
```

Now run the code again. Did the window stay open? No? Why not?

Run your code again, but this time watch the terminal instead of the virtual
desktop. What do you notice? The program finishes almost as soon as it prints
out the pygame welcome message, doesn't it. That makes sense. We got to the end
of the code. There were no more instructions for Python to execute, so it closed
itself.

We can test this theory by adding some code we'll quickly delete. At the top of
the file, add this import:

```python
from time import sleep
```

and just before the `pygame.quit()` command, add this line:

```python
sleep(5)
```

The `sleep` function asks Python to pause its execution for a number of seconds,
in this case 5. Now try running your code . . .

Eureka! The window stays open!

Our first hypothesis wasn't completely wrong, though. Let's try one more
experiment. Uncomment the `pygame.quit()` command and add `sleep(5)` on the line
after it. When you run your code, watch both the terminal and the virtual
desktop. Try to explain to yourself what you see happen.

[<<](guide_017.md) | [>>](guide_019.md) | [ToC](toc.md)

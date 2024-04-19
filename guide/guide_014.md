# initialize and quit `pygame`

Every `pygame` tutorial you read or watch will tell you to add this line of code
just after importing `pygame`:

```python
pygame.init()
```

But most won't tell you why. To get better as a developer, you should try, as
best you can, to understand every line of code you write. When you're a little
more experienced, you might look at the `pygame` code to figure out what this
`init` method does. Another great place to look is the `pygame` documentation.
Take a moment to read the [relevant section](https://www.pygame.org/docs/ref/pygame.html?highlight=init#pygame.init).

The counterpart to the `init` method is `pygame`'s `quit` method. It's
`pygame`'s way of cleaning up after itself. It's good practice to call this
method at the end of your program. Let's add it now:

```python
pygame.quit()
```

[<<](guide_013.md) | [>>](guide_015.md) | [ToC](toc.md)

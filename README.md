# Knight's Pong

Build your own version of the classic arcade game, Pong, using the `turtle`
library.

## Getting Started

Fork this repository. In your own fork, add game logic to `pong.py`. Start your
game by typing `python pong.py` in the terminal. IMPORTANT: see the next section
on graphical output.

## Graphical output and Codespaces

If you were running your game code locally, a window would pop up and display
your game. Getting the graphical output in Codespaces is trickier since the
virtual machine running your code on some faraway server isn't connected to a
display.

But I've added some configuration to this repository that will install some extra
software and send any graphical output to a remote display. If you're curious
about how it works (but only if you're curious), take a look at `.devcontainer/devcontainer.json`.

To see the graphical output of your game in Codespaces, toggle to the "Ports"
tab in the bottom panel, find port 6080, hover over the globe icon, and click
"Open in Browser".

![open remote desktop in browser](./images/launch_remote_desktop.webp)

This should open a new tab in your browser. It will ask you for a password; just
hit enter.

You'll see a bare bones desktop. Except for the fact that you're seeing a remote
desktop in your browser (!!), there's nothing exciting to see.

Now toggle back to the browser tab where you have the Codespaces editor open.
Toggle from the "Ports" tab to the "Terminal" tab and type `python pong.py` at
the command line. It will look like your terminal got stuck, but it's actually
running the pong starter code. Return to the remote desktop browser tab. You
should see a window with a black background. That's how your game will show up!

To stop your game, return to the terminal tab and press `Ctrl+C`.

## `pygames` instead of `turtle`?

The starter code and instructions for this project assume that you'll build Pong
using the `turtle` library, you may instead use the `pygame` library. It's a
more advanced library -- which is great -- but it is a little more complicated
to use and you'll have less guidance.

Before deciding to use `pygames`, take a look at the [documentation](https://www.pygame.org/docs/).

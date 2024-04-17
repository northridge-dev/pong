# virtual machines and version control

Your Codespace is a _virtual machine_ that exists on a GitHub server in a data
center somewhere in Ulaanbaatar or Baku or the Falkland Islands or somewhere
(or more likely Des Moines or Chicago, the two closest Microsoft Azure data
centers). _Virtualization_ in this case means that one physical server can
"host" or act as many different computers, each with its own operating system
and software.

Your _virtual machine_ acts in most ways just like your laptop or your home PC.
The browser-based code editor you'll use saves your code as you write or edit
it. And just like the code you write on your laptop or PC, that code is trapped
on your virtual machine unless you send a copy of it to another computer (virtual
or "real"). GitHub (probably) isn't going to bork your Codespace, but if you
accidentally delete your Codespace and you haven't sent a copy of your code
elsewhere, it's gone. Forever.

Maybe you've emailed an essay to yourself to have a backup copy. If you update
it, you'd email it again, and you'd end up with two non-identical copies. How
does the second version differ from the first? It's hard to tell.

That's a clumsy and impractical way to manage code, especially if more than one
person is making changes to the same files at roughly the same time. Instead, we
use a _version control system_ called `git` (which is where the "Git" in GitHub
comes from). `git` is a tool that helps you:

- see what files you've changed (and what you've changed in them)
- save those changes in a _commit_
- send those changes to another computer (like your GitHub repo)

Using a version control system like `git` gives you superpowers. You can easily
revert to an earlier version, start a new time line from any point in your
code's history, create a kind of alternate time line, combine that alternate
timeline with the main timeline, merge changes made by many developers into a
shared history, and see who is to blame for each line of code.

Here's a visualization. Each circle represents a _commit_, and you can see how
we have commits that "branch off" from the main commit line.

<figure>
  <img src="https://the-turing-way.netlify.app/_images/sub-branch.png" alt="commit graph">
  <figcaption>Image from <a href="https://the-turing-way.netlify.app/reproducible-research/vcs/vcs-git-branches.html">The Turing Way</a></figcaption>
  <br>
</figure>

[<<](guide_008.md) | [>>](guide_010.md) | [ToC](toc.md)

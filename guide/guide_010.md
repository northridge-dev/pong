# git in practice, or your first commit

Enough theory. Let's use `git` to add a commit and push it to GitHub.

Open your Codespace. If it's not open already, open the `README.md` file from
the file explorer on the left. Let's update the README with a more appropriate
title and a brief description.

## checking `git` status

Once you have, let's see what `git` has to say about the changes you've made.
Try running the following command in the terminal:

```bash
git status
```

You should see something like this:

```bash
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Here's what that all means:

1. `Your branch is up to date with 'origin/main'`: your local branch is in sync
   with the remote branch on GitHub. They have the same list of commits.
2. `Changes not staged for commit`: you've made changes to the files listed,
   but you haven't told `git` to include them in the next commit. `git` tells us
   that `README.md` was _modified_. `git` will also tell us about files we've
   _added_ or _deleted_ (or moved).
3. `no changes added to commit`: you haven't told `git` to include any changes
   in the next commit. If you'd already adding files, they'd be listed here.

## investigating the `diff`

Let's also see what the changes are. Run the following command:

```bash
git diff README.md
```

The output is a little cryptic, but essentially it shows you the changes you've
made to the file. At the beginning of the output, you'll see the `a` and `b` versions
of the file, which are the original and modified versions of the file, respectively.
Then there's a summary of the number of lines added and removed, followed by the
actual changes. Lines that have been removed are prefixed with a `-` (and often
displayed in red), and lines that have been added are prefixed with a `+` (and
often displayed in green).

```diff
diff --git a/README.md b/README.md
index 8c3a2b6..35530ef 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,3 @@
-# pygame-starter
\ No newline at end of file
+# Pong! (Northridge Remix)
+
+The classic arcade game, Pong, created with `pygame`.
```

We'll come back to `diff`-ing later.

## staging (adding) files to commit

When we asked `git` for the `status`, it also gave us a hint: `use "git add"
<file>..." to update what will be committed`. Let's do it:

```bash
git add README.md
```

If you run `git status` again, you'll see that `README.md` is now listed under
the "Changes to be committed" section. Yatzee!

But all we've done so far is tell git which changes to include in the next
commit. We still have to create the commit itself. Let's do that:

## creating a commit

```bash
git commit -m "Update README with a more appropriate title and description"
```

The `-m` flag is short for `--message`, and it allows you to provide a message
describing the changes you're committing. Make it short but specific and
descriptive. If the command succeeds, you'll see the commit message echoed along
with a summary of the changes.

## pushing the commit to GitHub

If you again run `git status`, you'll see that your branch has no changes. But
your commit is still stuck on your virtual machine. The last step is to `push`
it to its "upstream" repository on GitHub:

```bash
git push
```

(`git` knows where your repo is because your Codespace was created from it
configured `git` to know about it.)

Want to see your commit on GitHub? Open your browser and navigate to your
repository. You should see you commit in this commit history.

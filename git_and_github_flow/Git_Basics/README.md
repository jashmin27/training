# Git Basics Practice

This is my practice repo for going through the basic Git commands - clone, status, add, commit, log, diff, restore, branch and merge. I did everything from the command line, no GUI.

## What I did

1. **Initialized a repo** with `git init` and set up my username/email with `git config`.

2. **Made my first commit**
   - Created `notes.txt`
   - `git add notes.txt`
   - `git commit -m "Add notes.txt with initial content"`

3. **Checked status and diff before committing again**
   - Added a second line to `notes.txt`
   - Ran `git status` to see it listed under "Changes not staged for commit"
   - Ran `git diff` to see exactly what line was added before staging it
   - Then `git add` + `git commit` to save it

4. **Checked the history**
   - `git log --oneline` to see the two commits so far

5. **Practiced recovering from a mistake**
   - Added a junk line to `notes.txt` (typed something wrong on purpose)
   - Ran `git status`, saw it was an unstaged change
   - Used `git restore notes.txt` to throw away the bad edit and get back to the last commit
   - Checked the file again to confirm it was back to normal

6. **Branching and merging**
   - Created a new branch: `git branch add-feature`
   - Switched to it: `git checkout add-feature`
   - Added a line to `notes.txt` and committed it on that branch
   - Switched back to `master`
   - Ran `git merge add-feature` to bring that change into master
   - Confirmed with `git log --oneline --graph` that the history looks right

7. **Cloning**
   - Cloned this repo into a separate folder with `git clone` to check that the full history (all 3 commits) comes along with it

## What I took away from this

- `git status` and `git diff` are basically your safety check before you commit anything - always worth running.
- `git restore` is what saves you when you've made a change you didn't mean to and haven't committed it yet.
- Branches are cheap to make, and merging is painless as long as you're not touching the same lines as someone else.
- `git log --oneline --graph` is a nice quick way to see how commits and branches connect.

## Files here

- `notes.txt` - the file I used to test everything on
- `README.md` - this file

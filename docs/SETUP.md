The goal of this guide is so that we all can pretty much use the same environment when it comes the the Campus-Hub project. Even though we tried to make the setup as easy as possible, there are several things we need to install and configure so we can have the functions we need. That makes things a little tricky so we have the instructions all in one place.

The idea is we have a bunch of steps that sets up the same type of development environment for all the team members. We eventually get to an environment that does everything we need it to do for the project.

Note the instructions assume Windows. Need to change to the Mac steps if you are using a Mac.

## Step 0 – Install the tools - Python 3.14, Git, VS Code, and markdown editor/renderer

**Goal** get all the basic tools installted.
Note this only has to be done once on your computer.

**1. Install Python 3.14** (NOT 3.15: Django doesn't officially support 3.15 yet).

- Download the 64-bit installer from python.org → Run the installer and be sure to use admin priviledges is checked and add python.exe to PATH is checked.


**2. Install Git**

- git-scm.com → Download, install, and accept the defaults.

**3. Install VS Code** from code.visualstudio.com, then open the **Extensions** panel
(the four-squares icon on the left) and install:
- **Python** (by Microsoft)
- **Python Debugger** (by Microsoft)
- **Django** (by Baptiste Darthenay), which colors Django template code
- **Markdown all in One*** (by Yu Zhang) which lets us edit markdown and see what it looks like (for our readme files, UML classes, Sequence Diagrams, etc)

**4. Close and reopen** your VS Code.
Double check Python version using a VS Code Terminal.  Should come back with some version of 3.14.x

 ```
 python --version
 ```

**5. Tell Git your name and email** 
In either a command prompt or VS Code terminal:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.edu"
# Make new projects use "main" as the name of the main branch
git config --global init.defaultBranch main
```

## Step 1 – Hello, Campus Hub!

**Goal:** create the project folder and add one basic Python file.

**1. Create the project folder.**

- This might be just a practie copy. Use file explorer of command line to make a folder like this:
```
C:\dev\practice\Campus-Hub
```


-  **clone** the GitHub repo into Campus-Hub folder. In command window:
```
  cd C:\dev
  git clone https://github.com/jjdelite/Campus-Hub.git
  cd Campus-Hub
  ```

**2. Open it in VS Code:** **File → Open Folder…** → pick the `Campus-Hub` folder.
Click **Yes, I trust the authors**.

**3. Create a file named `hello.py`** File | New File:

```python
# hello.py - basic test in Campus-Hub.

print("Hello, Campus Hub!")
```

**4. Run it.**

 `py -3.14 hello.py` 

or in **VS Code:** open `hello.py` and click the **▶** button at the top right.

The terminal shows: `Hello, Campus Hub!`

## Step 2 – Virtual environment, requirements.txt and Git

**Goal:** give the project its own private Python virtual environment (so we don't trash anything else and no other configurations in our Python / VS Code environment can trash this), a list of the packages it needs, and its first Git commit.

### Steps

**1. Create the virtual environment** inside the `Campus-Hub` folder:

`py -3.14 -m venv .venv` 

This creates a new `.venv` folder appears.

**2. Activate the virtual environment** 

`.venv\Scripts\activate` 

Your prompt now starts with **`(.venv)`**, but you need to do this for each terminal window.

or easier - in **VS Code:** press **Ctrl+Shift+P**  → **Python: Select Interpreter** →
pick the one marked **`.venv`**.
Once you do this once, new VS Code terminals then activate it automatically, and
the status bar (bottom right, with a `.py` file open) shows `3.14.x ('.venv': venv)`.

**3. Create `requirements.txt`** in the project root:

** [NOTE YOU SHOULD ALREADY HAVE THIS IF YOU DID A GIT REPO CLONE]
**
```
# requirements.txt -- the Python packages Campus Hub needs 
# Note this is not our use cases, user stories, UML, etc. It is a list of everything VS Code needs to run our project and we can install it with one command:
#      pip install -r requirements.txt
#
# Django 5.2 is a "long-term support" (LTS) version.
# 5.2.8 or newer is needed for Python 3.14.
# >=5.2.8  means "version 5.2.8 or newer"
# <6.0     means "but not 6.0 or later" (a big new version could break our code)

Django>=5.2.8,<6.0
```
**4. Create `.gitignore`** in the project root:

**[NOTE YOU SHOULD ALREADY HAVE THIS IF YOU DID A GIT REPO CLONE]**

```
# .gitignore -- files Git should NOT track.
# These are files that are unique to our own computers and do not make sense to track

# Virtual envirnment, cache, local database
.venv/
__pycache__/
*.pyc
db.sqlite3
.DS_Store
Thumbs.db
```

**5. Create `README.md`** in the project root. This is the first page people see on GitHub:

**[NOTE YOU SHOULD ALREADY HAVE THIS IF YOU DID A GIT REPO CLONE]**

```markdown
# Campus Hub

A student planning web app for assignments, tests, meetings, job shifts and more.
CS-312 Software Engineering, Team 5.

- Setup instructions: see docs/SETUP.md
- Problems and fixes: see docs/TIPS-TROUBLESHOOTING.md
```

The goal of this guide is so that we all can pretty much use the same environment when it comes the the Campus-Hub project. Even though we tried to make the setup as easy as possible, there are several things we need to install and configure so here are the functions we need. That makes things a little tricky so we have the instructions all in one place.

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

- Use file explorer of command line to make a folder like this:
```
C:\dev\Campus-Hub
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

## Step 3 – Install Django and create the project

**Goal:** install Django and see Django's welcome page in your browser.

- **Django** – DJango Python web framework with ready-made code for building websites. It has
  pages, forms, logins, databases so we don't start from scratch.
- **`manage.py`** – the project's remote control which is created by Django creates it. You run commands on it like `python manage.py runserver`. It tells Django where our settings are, then runs the command you asked for. **THIS IS A BASIC DEFAULT FILE WE WILL PROBABLY NOT NEED TO EDIT TOO MUCH IF AT ALL**
- **`config/`** – the folder holding the settings for the whole site which are in `settings.py` and the main list of web addresses which are in `urls.py`.
- **Development server** – a small web server that runs on our own local computers so we can test. It uses the IP address `127.0.0.1` means "this computer", and port `8000`. We will need to figure out later how to deploy this to a web server on a cloud service so the professor can access it when it is running.

**[NOTE YOU SHOULD ALREADY HAVE THESE CONFIG AND PYSTHON FILES IF YOU DID A GIT REPO CLONE]**

### Steps

Make sure the prompt shows **`(.venv)`** first.

**1. Install the packages will need**

```
pip install -r requirements.txt
```

**2. Check that Django is installed:**

```
python -m django --version
```

**3. Create the Django project.**

```
django-admin startproject config .
```

You now have:

```
Campus-Hub/
├── config/          ← site-wide settings and URLs (created by Django)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py        ← the project's remote control (created by Django)
├── hello.py
├── requirements.txt
├── .gitignore
├── README.md
└── docs/
```

**4. Start the development server:**

```
python manage.py runserver
```

**5. Open http://127.0.0.1:8000/** in the browser.
Stop the server any time with **Ctrl + C** in the terminal.

- When it is running `python -m django --version` should print `5.2.x`.
- When you open browser page it shows Django's rocket page: **"The install worked successfully! Congratulations!"**
- There might be warnings about migrations which will be taken care of later


## Step 4 – This is where we make the first page for Campus Hub

**Goal:** make Campus Hub show show a page "Hello from Campus Hub!"

**New concepts.**

- **App** – a Django **app** is a *section* of our one website, grouping related code like for example where we manage accounts or another app might be where we edit our planner items
- **View** – a Python **function** that runs when someone visits a web address and returns what to show.
- **URL pattern** – the thing that connects the URL web address to a view.

How a request flows:

```
Browser asks for  /
        │
        ▼
config/urls.py   →  "" (the home page) → hand it to planner/urls.py
        │
        ▼
planner/urls.py  →  "" → views.home
        │
        ▼
planner/views.py →  home(request) returns "Hello from Campus Hub!"
        │
        ▼
Browser shows the text
```

### Steps

**1. Create the app:**

**[NOTE YOU SHOULD ALREADY HAVE THESE FILES IF YOU DID A GIT REPO CLONE SO YOU DON'T NEED TO DO THIS STEP]**

```
python manage.py startapp planner
```

A new `planner/` folder appears with `models.py`, `views.py` and other files.

**2. Tell Django the app exists.** Open `config/settings.py`, find `INSTALLED_APPS`, and
add `"planner",` as the **last line inside the brackets**:

**[NOTE YOU SHOULD ALREADY HAVE THESE FILES IF YOU DID A GIT REPO CLONE SO YOU DON'T NEED TO DO THIS STEP]**

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # ----- Our own apps go below Django's built-in ones -----
    "planner",
]
```

**3. Write the view.** Replace **everything** in `planner/views.py` with:

```python
# planner/views.py -- WHAT HAPPENS when someone visits a page.
#
# A "view" is just a Python function. Django calls it when a browser
# asks for a web address, and gives it one argument: "request"
# The view must RETURN a "response" which is what to send back to the browser which is what needs to be displayed on the page.
# HttpResponse is Django's simplest response: plain text.
from django.http import HttpResponse


def home(request):
    """The Campus Hub home page."""
    return HttpResponse("Welcome to Campus Hub!")
```

**4. Create a new file `planner/urls.py`** (it does not exist yet) with:

**[NOTE YOU SHOULD ALREADY HAVE THIS FILE IF YOU DID A GIT REPO CLONE SO YOU DON'T NEED TO DO THIS STEP]**

```python
# planner/urls.py -- WHICH web address runs WHICH view (for the planner app).
#
# Think of this list as mapping which maps the web address to a Python view.

from django.urls import path   # path() creates one phone-book entry
from . import views            # "." means "this app's folder": planner/views.py

urlpatterns = [
    # ""        This is the home page (nothing after the site address)
    # views.home = the function to run
    # name="home" = a nickname, so other code can say "home"
    #  instead of typing the address
    path("", views.home, name="home"),
]
```

**5. Connect the app's URLs to the main list.** Replace **everything** in `config/urls.py` with:

**[NOTE YOU SHOULD ALREADY HAVE THIS FILE IF YOU DID A GIT REPO CLONE SO YOU DON'T NEED TO DO THIS STEP]**

```python
# config/urls.py -- the MAIN list of web addresses for the whole site.
# Django checks these from top to bottom for every request.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django's built-in admin website lives at /admin/
    path("admin/", admin.site.urls),

    # Everything else is handed to the planner app's own urls.py.
    # include() lets each app keep its own list of web addresses / url patterns which keeps things neat and organized.
    path("", include("planner.urls")),
]
```

**6. Run it:** `python manage.py runserver`, then open http://127.0.0.1:8000/

The browser should show in regular unformated plain text: **Hello from Campus Hub!**

We replaced the rocket default page with our page for our app.


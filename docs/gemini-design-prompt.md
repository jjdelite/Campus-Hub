# Gemini Design Prompt — Campus Hub UI/UX Design

> **How to use this file:** Copy the whole prompt in Section 1 below and paste it into Google Gemini. It is written so Gemini can generate a complete, buildable UI/UX design for Campus Hub without inventing a different app. Everything in Section 2 is the ground truth from this repository — use it to check Gemini's answer against the real app.

---

## 1. The prompt to paste into Gemini

```text
You are a senior product/UI/UX designer. Design a complete, coherent UI/UX system for Campus Hub, a student planning web app, so that a small student team can build it in Django templates with plain CSS. Do not redesign it as a different app, a mobile-only app, a social network, a chat app, or a paid SaaS product. Stay grounded in the app described below.

### What Campus Hub is
Campus Hub is a student planning web app for assignments, tests, meetings, and job shifts. It is a CS-312 Software Engineering course project (Team 5). One student uses one account to plan their own week: see what is due soon, plan by course, and keep assignments, tests, meetings, and job shifts in one place. The tone should be calm, clear, and encouraging — it should reduce stress, not add to it.

### Current state of the app (do not assume more exists)
- Stack: Python 3.14, Django 5.2.x, Django templates, SQLite for local development. Run with `python manage.py runserver` at http://127.0.0.1:8000/. The only dependency is Django (>= 5.2.8, < 6.0) in `requirements.txt`.
- Project structure: Django project `config/` (settings.py, urls.py, wsgi.py, asgi.py), Django app `planner/` (models.py, views.py, urls.py, admin.py, apps.py, tests.py, migrations/), plus `manage.py`, `hello.py`, `.gitignore`, `README.md`, and `docs/`.
- The only route today is the home page at `/`, served by `planner/views.py: home()`, which returns the plain text "Welcome to Campus Hub!" There are NO templates, NO static/CSS files, NO models, NO forms, and NO login/signup views yet. Design for Django templates and plain CSS in a future `planner/templates/` and `planner/static/` (or project-level static) folder — do not assume React, Tailwind, a component framework, or a design system already exists.
- Default Django settings: LANGUAGE_CODE en-us, TIME_ZONE UTC, DEBUG True in development. The user should be able to choose their own time zone in Settings.
- README: "A student planning web app for assignments, tests, meetings, job shifts and more. CS-312 Software Engineering, Team 5." Setup is documented in `docs/SETUP.md`; troubleshooting in `docs/TIPS-TROUBLESHOOTING.md`.
- Requirements in this repo: `docs/requirements/User Stories/US-01 - Create User Account.md` and `docs/requirements/User Stories/Student-Planner-20-Additional-User-Stories.md` (user stories US-41 to US-64). Use those stories as the feature list below — they are the source of truth, not a wish list.

### Features you must design for (grounded in the user stories)
1. Accounts and profile: sign up with name, email, and password; clear, reasonable error messages when a field is wrong or the email/account already exists; log in; log out; update profile (change name and email); change password; recover account access (forgot-password flow); view recent account activity and sign out of other sessions.
2. Planner items: four item types — Assignment, Test, Meeting, Job Shift. Each item has a title, course, due date or start/end date and time, priority (Low / Medium / High), and completion state (complete/incomplete). Items can have subtasks (checklist items the user checks off), an attachment link (a URL, for example to readings or assignment files), and can be duplicated. Deleting an item must offer Undo.
3. Organising items: sort items by date, priority, or type; filter the list by priority; see priority clearly on both the list and the calendar; agenda view = a chronological list of upcoming incomplete items.
4. Calendar: a weekly calendar view with Previous / Next week and a Today button; all-day items; recurring items (the user can edit one occurrence, or skip one occurrence, without changing the whole series); a warning when two timed items overlap (a scheduling conflict); the user's chosen time zone is respected.
5. Courses: a course list the user can reorder (drag, or Move up / Move down), and archive a course so it no longer clutters the active list.
6. Dashboard / home: at a glance — today, what is due soon, what is overdue, and upcoming incomplete items; a prominent way to add a new item.
7. Reminders: the user configures when reminders arrive (for example how far before a due date); they can preview a reminder email before it is sent; if a reminder fails to deliver, the user is told.
8. Data and admin: export the user's data (courses, items, recurrence rules, and completion status); an admin view that shows an audit trail of changes.

### What I need from you — deliver all of it, in this order

#### A. Design direction and style guide
- Propose ONE primary design direction (name it, explain in 2-3 sentences why it fits a busy student), plus one short alternative direction only if it is genuinely different.
- Colour palette with exact HEX values for: primary, primary-hover/active, secondary, accent, success, warning, danger/error, info, background, surface/card, border, and text (primary, secondary, muted). Give a light mode as the default and a dark-mode palette as an option. Give a distinct, colour-blind-friendly colour for each item type (Assignment, Test, Meeting, Job Shift) and for each priority (Low, Medium, High), and state the text/background contrast ratio for the main text and button combinations (aim for WCAG 2.1 AA).
- Typography: recommend a font pairing (prefer free, web-safe / Google Fonts), with a type scale table (font, size in px/rem, weight, line-height, and where it is used) for display/page title, section heading, card title, body, small/helper text, labels, and buttons.
- Spacing and layout: an 8-point spacing scale, page max-width, content padding, card corner radius, shadows, and border widths. State the grid/layout system (sidebar + content on desktop; what collapses on mobile).
- Component styling rules: buttons (primary, secondary, danger, ghost, disabled), text inputs, selects, date/time pickers, textareas, checkboxes and subtask rows, badges/chips, cards, modals/dialogs, toasts, and the navigation bar. For each, give default, hover, focus (visible keyboard focus), active, disabled, and error states.
- Give the whole style guide as a CSS-variables snippet the team can paste into a Django static CSS file (for example `:root { --color-primary: #...; --radius-md: 8px; ... }`).

#### B. Screen-by-screen design (design every screen below)
For EACH screen, give: purpose (one sentence), desktop layout (describe the regions top-to-bottom / left-to-right), mobile layout (what stacks, what moves to a bottom bar or menu), the exact sections and content shown, the primary and secondary actions, example data (use realistic student examples — e.g. "CS-312 Assignment 3", "Biology 101 Test", "Team meeting", "Library job shift"), and what the empty, loading, and error states look like.
1. Landing / public home page — the first page a new visitor sees; explain the app, show how to sign up/log in.
2. Sign up — name, email, password (per US-01); show the validation errors and the "account already exists" case.
3. Log in — email, password, link to password recovery and to sign up.
4. Password recovery / reset — request a reset link, then set a new password.
5. Dashboard / home (logged in) — today at a glance, due soon, overdue, upcoming incomplete items, quick Add button, and a course summary.
6. Planner list / All items — full item list with sort (by date, priority, type) and priority filter, item rows/cards showing type, course, due date/time, priority, subtasks progress, and completion checkbox.
7. Weekly calendar — week grid, Previous / Next / Today, all-day row, timed items, recurring-item marker, and the conflict warning for overlapping items.
8. Agenda view — chronological list of upcoming incomplete items, grouped by day.
9. Item detail — one item with its course, dates, priority, subtasks, attachment link, recurrence, reminder, and Edit / Duplicate / Delete (with Undo) actions.
10. Add item — form for all four item types, with fields for title, type, course, due/start/end date and time, all-day toggle, priority, subtasks, attachment link (URL), recurrence, and reminder timing.
11. Edit item — same form pre-filled, plus recurrence choice ("This occurrence only", "This and following", or "All occurrences" where it makes sense) and a "Skip this occurrence" option.
12. Courses — list of courses the user can reorder and archive, plus adding a course; show an archived-courses section.
13. Profile & Settings — profile (name/email), change password, time-zone selection, reminder settings, sessions/activity with "sign out of other sessions", and Export my data.
14. Reminder email preview — what the reminder email looks like, and the delivery-failure notice shown in the app.
15. Admin audit view — a simple table of who changed what and when (admin only; keep it clearly separate from student screens).
16. Error / not-found states — a 404-style page and a generic error page that fit the same design.

#### C. Key components and their states
Design and specify: item card/row (all four types, three priorities, overdue, due-soon, completed), calendar event block, priority badge, type chip, subtask checklist row, Add-item modal or page, confirmation dialog for delete, Undo toast after delete, conflict banner, filter chips and sort control, empty states (no items yet, no courses yet, nothing due today — include the exact copy you suggest), loading skeletons, and form-validation errors (inline, next to the field). Show each component in its normal, hover, focus, disabled, and error states where relevant.

#### D. Responsive behaviour
Give breakpoints (for example 360px phone, 768px tablet, 1024px laptop, 1280px+ desktop) and for each say exactly what changes: navigation (top bar vs. sidebar vs. bottom navigation), calendar (week grid vs. day/agenda list), item list (table/cards), Add/Edit forms (one column vs. two columns), minimum touch-target size (at least 44x44px), and what is hidden, collapsed, or moved. The design must work on a phone, a PC, and a Mac (US-01 acceptance criterion).

#### E. Accessibility and implementation notes for Django
- WCAG 2.1 AA checklist for this app: contrast, keyboard navigation and focus order, labels for every form field, ARIA where a component needs it, and reduced-motion support.
- Django implementation notes: how the screens map to Django templates (for example a shared `base.html`, one template per screen, partials for item cards), where the CSS variables and static files live, and how the list/calendar/agenda views reuse the same item-card component. Do not require any JavaScript framework; say where a small amount of plain JavaScript is genuinely needed (for example the Undo toast, the calendar Previous/Next navigation, or drag-to-reorder courses) and where plain Django forms/links are enough.
- Prioritised build order: what the team should build first (MVP) and what can come later.

### Output format
Return your answer as structured Markdown with: a one-paragraph summary; the style guide (with tables for colours, type, and spacing, and the CSS-variables code block); one section per screen (numbered as above, with a simple text/ASCII layout sketch for the desktop and mobile versions of the Dashboard, Weekly Calendar, and Add Item screens); a component library section; a responsive-behaviour table; an accessibility checklist; Django implementation notes; and a short list of open questions/assumptions you had to make, with your recommended answer for each. Do not add features that are not in the feature list above (no payments, no social feed, no chat, no grading). If a detail is not specified in the repository, say so and recommend a sensible default instead of silently inventing a different app.
```

---

## 2. Ground truth from this repository (for reviewers)

Checked 2026-11-11, on `main` of `jjdelite/Campus-Hub`.

- **Project:** Campus Hub — "A student planning web app for assignments, tests, meetings, job shifts and more. CS-312 Software Engineering, Team 5." (README.md)
- **Stack:** Python 3.14, Django 5.2.x (`Django>=5.2.8,<6.0` in `requirements.txt`), Django templates, SQLite for local development, `python manage.py runserver` on http://127.0.0.1:8000/ (`docs/SETUP.md`).
- **Structure:** `config/` (Django project: `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`), `planner/` (app: `models.py`, `views.py`, `urls.py`, `admin.py`, `apps.py`, `tests.py`, `migrations/`), `manage.py`, `hello.py`, `.gitignore`, `README.md`, `docs/`.
- **Current UI:** none. The only route is `""` in `planner/urls.py`, served by `planner/views.py: home()`, returning the plain text `Welcome to Campus Hub!`. `planner/models.py` is an empty placeholder comment. There are no `templates/` or `static/` folders anywhere in the repo, and no forms or auth views yet.
- **Docs:** `docs/SETUP.md` (setup/run instructions), `docs/TIPS-TROUBLESHOOTING.md`, `docs/design/` (placeholder README only), `docs/requirements/User Stories/US-01 - Create User Account.md`, `docs/requirements/User Stories/Student-Planner-20-Additional-User-Stories.md` (US-41–US-64: priorities, subtasks, duplicate, undo delete, sorting/filtering, recurring items, conflicts, weekly calendar, agenda, courses archive/reorder, reminders, export, admin audit, profile/password/recovery/sessions), `docs/requirements/CS-312-Project-Use Cases-10-26-2026.docx`, `docs/sprint/` and `docs/uml/` (mostly placeholders).
- **Default settings:** `LANGUAGE_CODE = "en-us"`, `TIME_ZONE = "UTC"`, `DEBUG = True`, `TEMPLATES` with `APP_DIRS = True` and no extra `DIRS` (`config/settings.py`).

## 3. Notes for the team

- Keep this file as the prompt source of truth. If Gemini suggests a feature or screen that is not in Section 1, check it against the user stories above before building it.
- The design in Section 1 is deliberately implementable in Django templates + plain CSS, so the Team 5 developers can apply it without adding a front-end framework.

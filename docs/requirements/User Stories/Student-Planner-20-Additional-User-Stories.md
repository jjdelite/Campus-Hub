# Student Planner — 24 Additional User Stories

These stories extend the original Student Planner backlog covering accounts, planner items, recurring events, courses, filters, weekly calendar views, reminders, and account administration.

## Account and profile

### US-41 — Update profile details
**As a** student, **I want** to update my name and email address, **so that** my planner account remains current.

**Acceptance criteria**
- The student can edit their name and email from account settings.
- The system validates required fields and email format.
- The system rejects an email already assigned to another account.
- The updated details appear the next time the student views their profile.

### US-42 — Change password
**As a** student, **I want** to change my password, **so that** I can keep my account secure.

**Acceptance criteria**
- The student must provide the current password.
- The new password must satisfy the system's password rules.
- The new password is stored securely and can be used on the next login.
- An incorrect current password does not change the account.

### US-43 — Recover account access
**As a** student, **I want** to request a password-reset link, **so that** I can regain access if I forget my password.

**Acceptance criteria**
- The student can submit the email associated with the account.
- The system sends a time-limited reset link when the account exists.
- The reset link cannot be reused after the password is changed.
- The response does not reveal whether an email is registered.

### US-44 — View account activity
**As a** student, **I want** to see my recent account activity, **so that** I can recognize unexpected access.

**Acceptance criteria**
- The system shows recent successful logins and password changes.
- Each entry includes a date and time.
- The student can sign out of other active sessions.

## Planner item management

### US-45 — Set item priority
**As a** student, **I want** to assign a priority to an item, **so that** I can focus on the work that matters most.

**Acceptance criteria**
- An item can be marked low, medium, or high priority.
- Priority is visible in list and calendar views.
- The student can filter items by priority.

### US-46 — Add subtasks
**As a** student, **I want** to break an item into subtasks, **so that** large assignments are easier to manage.

**Acceptance criteria**
- A planner item can contain zero or more subtasks.
- Each subtask can be marked complete independently.
- The parent item displays completion progress.
- Completing every subtask does not automatically complete the parent unless the student confirms it.

### US-47 — Duplicate an item
**As a** student, **I want** to duplicate an existing item, **so that** I can quickly create a similar task.

**Acceptance criteria**
- The duplicate receives a new identifier.
- The student can edit the title, dates, course, and notes before saving.
- The original item remains unchanged.

### US-48 — Undo a recent deletion
**As a** student, **I want** to undo a recent item deletion, **so that** I can recover from an accidental action.

**Acceptance criteria**
- A confirmation message offers an undo action after deletion.
- Undo restores the item's fields and completion status.
- The undo option expires after a reasonable short period or after navigation.

### US-49 — Sort planner items
**As a** student, **I want** to sort my items by date, priority, or type, **so that** I can review them in the most useful order.

**Acceptance criteria**
- The student can choose a sort option from the planner view.
- The selected sort applies without changing stored item data.
- The system preserves the selected sort during the current session.

### US-50 — Add an attachment link
**As a** student, **I want** to attach a web link to an item, **so that** I can quickly open related course material.

**Acceptance criteria**
- The student can add, edit, or remove a valid URL.
- The link is visible from the item details view.
- Opening the link does not expose other private planner data.

## Dates and recurring events

### US-51 — Edit one recurring occurrence
**As a** student, **I want** to edit one occurrence of a recurring event, **so that** an exception does not change every occurrence.

**Acceptance criteria**
- The system asks whether the change applies to one occurrence or all occurrences.
- A one-occurrence change is visible only on the selected date.
- The remaining recurrence pattern is unchanged.

### US-52 — Skip one recurring occurrence
**As a** student, **I want** to skip one occurrence of a recurring event, **so that** holidays or canceled sessions do not clutter my planner.

**Acceptance criteria**
- The student can remove one occurrence without deleting the series.
- The skipped occurrence is not shown as an outstanding item.
- Future occurrences remain scheduled.

### US-53 — Detect scheduling conflicts
**As a** student, **I want** the planner to warn me about overlapping timed items, **so that** I can resolve conflicts before they cause problems.

**Acceptance criteria**
- The system checks new and edited items against existing timed items.
- Overlapping items are clearly identified.
- The student may save the item after reviewing the warning.

### US-54 — Use all-day items
**As a** student, **I want** to create an all-day item, **so that** deadlines without a specific time appear correctly.

**Acceptance criteria**
- The student can choose all-day instead of entering a time.
- All-day items appear at the top or designated all-day area of the calendar.
- Reminders do not invent a time that the student did not provide.

### US-55 — Support time zones
**As a** student, **I want** my timed items to use my selected time zone, **so that** events remain accurate when I travel.

**Acceptance criteria**
- The student can select a time zone in account settings.
- Existing timed items display consistently after the time zone changes.
- Reminder times use the selected time zone.

## Calendar and course organization

### US-56 — Navigate calendar weeks
**As a** student, **I want** next-week, previous-week, and today controls, **so that** I can move through my schedule quickly.

**Acceptance criteria**
- The weekly calendar supports previous and next week navigation.
- A Today action returns to the week containing the current date.
- The displayed date range updates correctly.

### US-57 — View an agenda list
**As a** student, **I want** an agenda view of upcoming items, **so that** I can read my schedule without scanning calendar columns.

**Acceptance criteria**
- The agenda lists upcoming incomplete items in chronological order.
- Items include title, date, time when available, and course.
- The student can open an item from the agenda.

### US-58 — Archive a course
**As a** student, **I want** to archive a finished course, **so that** it no longer appears in active course filters while its history remains available.

**Acceptance criteria**
- Archiving a course does not delete its planner items.
- Archived courses are hidden from active course selectors by default.
- The student can view and restore archived courses.

### US-59 — Reorder courses
**As a** student, **I want** to choose the display order of my courses, **so that** my most-used courses are easy to find.

**Acceptance criteria**
- The student can reorder active courses.
- The order is saved to the student's account.
- Course order is reflected in selectors and filters.

## Reminders and administration

### US-60 — Configure reminder timing
**As a** student, **I want** to choose how far in advance reminders arrive, **so that** notifications fit my planning habits.

**Acceptance criteria**
- The student can choose from supported reminder lead times.
- The selected lead time is shown in reminder settings.
- Daily reminders use the saved preference.

### US-61 — Preview reminder email
**As a** student, **I want** to preview my reminder email, **so that** I know what information will be sent.

**Acceptance criteria**
- The preview uses the student's current upcoming items.
- The preview clearly identifies the date range covered.
- Previewing an email does not send it.

### US-62 — Handle reminder delivery failure
**As a** student, **I want** to know when a reminder cannot be delivered, **so that** I can correct my email settings.

**Acceptance criteria**
- A delivery failure is recorded without exposing sensitive content.
- The student sees a clear account notification at the next login.
- The system avoids repeatedly sending to an address that has permanently failed.

### US-63 — Review system audit actions
**As a** system administrator, **I want** an audit record of account deletions and administrative actions, **so that** sensitive changes can be reviewed.

**Acceptance criteria**
- The system records the action, administrator, and timestamp.
- Audit records do not contain plaintext passwords.
- Regular students cannot view administrative audit records.

### US-64 — Export account data
**As a** student, **I want** to export my planner data, **so that** I can keep a personal copy or move it to another tool.

**Acceptance criteria**
- The export includes courses, planner items, recurrence information, and completion status.
- The export is limited to the requesting student's data.
- The system clearly indicates when the export is ready.


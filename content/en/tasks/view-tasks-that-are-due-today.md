---
{
 "id": "tasks/view-tasks-that-are-due-today",
 "title": "View tasks that are due today",
 "section": [],
 "order": 284,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/40062",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/com.palm.app.tasks/source/views/ListsView.js:80",
  "adb: /usr/palm/applications/com.palm.app.tasks/source/views/ListsView.js:54",
  "adb: /usr/palm/applications/com.palm.app.tasks/source/views/ListsView.js:128",
  "adb: /usr/palm/applications/com.palm.app.tasks/source/views/TaskRow.js:107",
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates '{}'"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Tasks**.

   The number to the right of **List all tasks** shows the total number of tasks that are due today or are overdue. The number to the right of each task list name shows the number of tasks in that list that are due today or overdue.
2. Tap a task list name. The due date appears to the right of each task, and overdue dates appear in red.

See Also [**Get notified about tasks that are due**](/tasks/get-notified-about-tasks-that-are-due)

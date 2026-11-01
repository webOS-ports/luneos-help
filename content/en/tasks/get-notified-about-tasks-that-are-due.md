---
{
 "id": "tasks/get-notified-about-tasks-that-are-due",
 "title": "Get notified about tasks that are due",
 "section": [],
 "order": 284.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.tasks/source/Launcher.js:20-30 (when the due tasks are checked)",
  "/usr/palm/applications/com.palm.app.tasks/source/Launcher.js:221-256 (one item per task, tap actions, swipe away)",
  "/usr/palm/applications/com.palm.app.tasks/source/TasksDb.js:601 (due tasks)"
 ],
 "review": []
}
---

Tasks lets you know when tasks are due today or overdue. A notification appears for each one, showing the task name and the name of its list. Tasks checks when your device starts, at midnight, and whenever a due date changes. It doesn't remind you at a set time.

- To open the task: Tap the notification text.
- To open the task's list: Tap the notification icon.
- To clear the notification: Throw it off the side of the screen. It comes back only when the tasks that are due change.

The notification goes away when no tasks are due any more.

See Also [**View tasks that are due today**](/tasks/view-tasks-that-are-due-today)

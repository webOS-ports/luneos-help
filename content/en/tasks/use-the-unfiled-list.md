---
{
 "id": "tasks/use-the-unfiled-list",
 "title": "Use the Unfiled list",
 "section": [],
 "order": 281.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.tasks/source/TasksDb.js:28,344-358 (Unfiled, only while it holds tasks)",
  "/usr/palm/applications/com.palm.app.tasks/source/views/TasksView.js:324,350",
  "/usr/palm/applications/com.palm.app.tasks/source/views/MainView.js:137-139 (Just Type)",
  "/usr/palm/applications/com.palm.app.tasks/source/views/TaskDetails.js:60-63,139 (List selector)",
  "/usr/palm/applications/com.palm.app.tasks/source/Tasks.js:225 (Unfiled is not a local list, so it can't be swiped away)"
 ],
 "review": []
}
---

**Unfiled** holds tasks that aren't in any of your lists. A task goes there when you add it while viewing **List all tasks**, or when you create it with Just Type.

**Unfiled** appears in your lists only while it holds at least one task. You can't rename or delete it.

To move a task out of **Unfiled**:

1. **[Open](/basics/open-an-application-in-the-launcher) Tasks** > **Unfiled**.
2. Tap the arrow or due date to the right of the task name.
3. Next to **List**, tap the current setting > tap the list you want.

To move a task into **Unfiled**, select **Unfiled** in the same way.

See Also [**Create a task**](/tasks/create-a-task)

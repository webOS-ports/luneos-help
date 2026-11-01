---
{
 "id": "backup/manage-your-backups",
 "title": "Manage your backups",
 "section": [],
 "order": 439.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.backup/source/BackupInfo.js:86-90 (Manage backups row)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupListPage.js:25-46,133-145 (rows)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupListPage.js:55-78 (dialogs)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupListPage.js:38 (swipe, SwipeableItem)",
  "adb: luna-send com.palm.app.backup.service/listBackups"
 ],
 "review": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Backup**.
2. Tap **Manage backups**. The folder is shown at the top, then one row per backup with its date, its size, and **Full** or **Incremental**.
3. Do one of the following:
   - To restore a backup: Tap it > **Restore** ([learn more](/backup/restore-a-backup)).
   - To delete a backup: Tap it > **Delete This Backup** > **Delete**. Or swipe it sideways and tap **Delete**.
4. Tap **Done**.

A deleted backup cannot be brought back. Deleting one frees up storage.

If a row says something was skipped, that part could not be backed up. The rest of the backup is fine.

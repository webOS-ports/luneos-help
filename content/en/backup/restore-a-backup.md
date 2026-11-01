---
{
 "id": "backup/restore-a-backup",
 "title": "Restore a backup",
 "section": [],
 "order": 439.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.backup/source/BackupApp.js:95 (Restore a backup...)",
  "/usr/palm/applications/com.palm.app.backup/source/restore/ChooseBackupPage.js:54-56,70,106-115 (list, confirm)",
  "/usr/palm/applications/com.palm.app.backup/source/restore/RestoringPage.js:30-32,84-92 (progress, Try Again)",
  "/usr/palm/applications/com.palm.app.backup/source/restore/RestoringPage.js:100-107 (passphrase, Skip)",
  "/usr/palm/applications/com.palm.app.backup/source/restore/RestoringPage.js:270-302 (Restore complete, Restart)",
  "adb: luna-send com.palm.app.backup.service/listBackups (restoredCount 5: restore has run on the MindPhone)",
  "adb: com.palm.app.backup/source/BackupInfo.js on the TouchPad (Reinstall apps when restoring)"
 ],
 "review": []
}
---

Restoring replaces the accounts, contacts and settings on your device with those in the backup. What you added since that backup is overwritten.

1. **[Open](/basics/open-an-application-in-the-launcher) Backup**.
2. **[Menu](/basics/open-the-application-menu)** (upper left) > **Restore a backup...**.
3. Tap the backup you want > **Restore**. Each row shows the device that made the backup, its date and its size.
4. If the backup holds saved passwords, enter your passphrase > **Restore**. To restore everything else without them, tap **Skip**.
5. Wait for **Restore complete.**, then tap **Restart**. If there is only a **Done** button, tap it and restart your device yourself ([learn how](/device-info/restart-your-device)).

You can also start from **Manage backups**: Tap the backup > **Restore**.

If you see **Error Restoring Data**, tap **Try Again**.

On some devices, Backup has a **Reinstall apps when restoring** switch. It is off at first. Turn it on only if you trust where the backup came from. Apps that were not reinstalled are listed when the restore finishes; you can install them again with Preware 2 ([learn how](/software-manager/find-and-install-apps-with-preware-2)).

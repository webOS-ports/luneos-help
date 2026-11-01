---
{
 "id": "backup/erase-luneos-account-information-from-the-server",
 "title": "Turn Backup on or off",
 "section": [],
 "order": 439,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42503",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/com.palm.app.backup/source/BackupInfo.js:28-31 (dialog)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupInfo.js:170 (toggleChanged)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupListPage.js:64-76 (delete a backup)",
  "adb: luna-send com.palm.app.backup.service/listBackups"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Backup**.
2. Do one of the following:
   - To turn backup on: Tap **OFF**.
   - To turn backup off and erase your backups: Tap **ON** > **Turn Off and Erase**. This erases the backups stored on your device. It does not affect your other information. To leave Backup on, tap **Keep Backup On** instead.
   - To delete one backup: Tap **Manage backups** > tap the backup > **Delete This Backup** > **Delete**.

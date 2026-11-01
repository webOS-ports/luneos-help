---
{
 "id": "backup/manually-back-up-information-to-your-luneos-account",
 "title": "Back up your device manually",
 "section": [],
 "order": 438,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42500",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/com.palm.app.backup/source/BackupInfo.js:10 (info text)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupProgress.js:9 (Back Up Now)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupApp.js:96 (Back up everything now)",
  "/usr/palm/applications/com.palm.app.backup/source/UserDataPage.js:36-52",
  "adb: luna-send com.palm.app.backup.service/listTargets (/media/internal/webos-backups/)"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Backup**.
2. If **Backup** is **OFF**, tap it to turn it on.
3. Tap **Back Up Now**.

To make a full backup instead of adding only what changed: **[Menu](/basics/open-the-application-menu)** (upper left) > **Back up everything now**.

While Backup is on, your device also backs up once a day. Your accounts, contacts, calendar, settings, and application data are always included. To add media files or saved passwords, tap **What to back up** ([learn more](/backup/what-does-backup-save)).

Backups are stored on your device, in the **webos-backups** folder of the internal storage. They are not encrypted. You can copy them to your computer over USB ([learn how](/basics/copy-files-between-your-device-and-your-computer)).

To get your information back, see [Restore a backup](/backup/restore-a-backup).

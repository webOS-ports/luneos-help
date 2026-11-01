---
{
 "id": "basics/move-your-information-to-another-device",
 "title": "Move your information to another device",
 "section": [
  "Sync personal data and copy files between your device and computer"
 ],
 "order": 56.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: com.palm.app.backup source/BackupInfo.js:10 \"restored ... onto a different device\"",
  "adb: com.palm.app.backup source/BackupApp.js:95 Restore a backup...",
  "adb: com.palm.app.backup source/restore/ChooseBackupPage.js device rows, Restore this backup?, Cannot Restore, Replace the data on this device",
  "adb: com.palm.app.backup source/restore/RestoringPage.js:293-296 Restart",
  "adb: ls /media/internal/webos-backups on MindPhone",
  "copying the folder between two devices and restoring has not been tried"
 ]
}
---

Move your information with a backup, with your online accounts, or by copying files.

**Use a backup**

1. On the old device, [make a backup](/backup/manually-back-up-information-to-your-luneos-account).
2. [Connect the old device to your computer](/basics/copy-files-between-your-device-and-your-computer), and copy the **webos-backups** folder to your computer.
3. Connect the new device, and copy the **webos-backups** folder to it.
4. On the new device, [open](/basics/open-an-application-in-the-launcher) **Backup**.
5. Open the [application menu](/basics/open-the-application-menu) and tap **Restore a backup...**.
6. Tap the backup, and then tap **Restore**.
7. When the restore is done, restart your device if it asks you to.

**NOTE:** Restoring replaces the accounts, contacts and settings on the new device. You can't restore a backup that a newer version of LuneOS made.

**Use your online accounts**

Set up the same accounts on the new device. Your contacts and calendar events come back from the account ([learn how](/basics/sync-personal-data-using-third-party-software)).

**Copy your files**

Copy music, photos and videos over USB, using your computer ([learn how](/basics/copy-music-photos-and-videos-between-your-computer-and-your-device)).

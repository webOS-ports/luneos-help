---
{
 "id": "backup/what-does-backup-save",
 "title": "What does Backup save?",
 "section": [],
 "order": 437.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.backup/source/UserDataPage.js:36-48 (Always included)",
  "/usr/palm/applications/com.palm.app.backup/source/UserDataPage.js:51-52 (media off by default)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupInfo.js:10 (info text)",
  "/usr/palm/services/com.palm.app.backup.service/util/prefs.js:43 (manifestsToKeep 10)",
  "/usr/palm/services/com.palm.app.backup.service/handlers/backup.js:933 (purge)",
  "adb: luna-send com.palm.app.backup.service/listTargets (only target: This device, /media/internal/webos-backups/)",
  "adb: luna-send com.palm.app.backup.service/getUserDataCategories"
 ],
 "review": []
}
---

Backup keeps a copy of your information on your device. You do not need an online account for it, and it sends nothing over the Internet.

**Always saved**

- Accounts, contacts and calendar
- System settings and preferences
- Application data

**Saved if you choose** ([learn how](/backup/choose-what-to-back-up))

- Photos, videos, music, documents, downloads and ringtones
- Saved passwords ([learn how](/backup/back-up-your-saved-passwords))

**Where it goes**

Backups are stored in the **webos-backups** folder of your device's internal storage. **Back up to** in Backup shows the destination; **This device** is the only one.

While Backup is on, your device backs up once a day. Backup keeps your 10 most recent backups and removes older ones.

**Keep a copy somewhere else**

If you lose your device or reinstall LuneOS, backups stored on it can be lost too. Copy the **webos-backups** folder to your computer from time to time ([learn how](/basics/copy-files-between-your-device-and-your-computer)).

Backups are not encrypted, apart from saved passwords. Anyone who can reach your device's storage can read them.

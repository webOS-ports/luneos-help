---
{
 "id": "backup/what-does-limited-backup-mean",
 "title": "What does Limited backup mean?",
 "section": [],
 "order": 439.4,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "evidence": [
  "/usr/palm/applications/com.palm.app.backup/source/BackupInfo.js:21-22,69-73 (Limited backup box)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupApp.js:416-418 (shown when privileged is false)",
  "/usr/palm/services/com.palm.app.backup.service/util/privileged.js:485-500 (direct mode needs no helper)",
  "/usr/palm/applications/com.palm.app.backup/source/restore/RestoringPage.js:288-296 (no automatic restart)",
  "adb: luna-send com.palm.app.backup.service/getBackupStatus (privileged true on both devices)"
 ],
 "review": []
}
---

A **Limited backup** box in Backup means it could not get the access it needs to read some system files. Those files are left out of your backups. The rest is still backed up.

Backup comes with LuneOS and normally has this access, so you should not see this box. The advice in the box to install the app and restart does not apply to a Backup that came with LuneOS.

After you restore a limited backup, you have to restart your device yourself.

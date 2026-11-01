---
{
 "id": "backup/back-up-your-saved-passwords",
 "title": "Back up your saved passwords",
 "section": [],
 "order": 438.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.backup/source/UserDataPage.js:114-128 (Saved passwords, note)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupApp.js:138-150 (passphraseDialog caption, Back up)",
  "/usr/palm/applications/com.palm.app.backup/source/BackupApp.js:366-373 (saved passwords were not included)",
  "/usr/palm/services/com.palm.app.backup.service/handlers/backup.js:1028-1031 (scheduled run skips passwords)",
  "adb: luna-send com.palm.app.backup.service/getUserDataCategories (passwords: Saved passwords, Encrypted with a passphrase you choose)"
 ],
 "review": []
}
---

Backup can include the passwords of your accounts. They are encrypted with a passphrase you choose.

1. **[Open](/basics/open-an-application-in-the-launcher) Backup**.
2. Tap **What to back up**.
3. Under **Passwords**, turn on **Saved passwords** > **Done**.
4. Tap **Back Up Now**.
5. Enter a passphrase > **Back up**.

Good to know:

- You need the same passphrase to restore the passwords. If you forget it, the passwords do not restore, but everything else in the backup still does.
- You are asked for the passphrase only when you start a backup yourself. The daily backup has nobody to ask, so it leaves new passwords out.
- If the button shows **Backup complete - saved passwords were not included**, the backup worked but holds no passwords.

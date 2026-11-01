---
{
 "id": "backup/choose-what-to-back-up",
 "title": "Choose what to back up",
 "section": [],
 "order": 437.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.backup/source/UserDataPage.js:54-130,134-137 (rows, Done)",
  "/usr/palm/applications/com.palm.app.backup/source/UserDataPage.js:203-204 (empty categories hidden)",
  "adb: luna-send com.palm.app.backup.service/getUserDataCategories (labels, counts)"
 ],
 "review": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Backup**.
2. Tap **What to back up**.
3. Under **Media**, turn on what you want to include: **Photos**, **Videos**, **Music**, **Documents**, **Downloads** or **Ringtones**. Each row shows how many files there are and how much space they take. A kind of file you have none of is not listed.
4. Tap **Done**.

Media is off at first, because backups are written to your device: each file you include takes up storage twice. **Media selected** shows the total for what you turned on.

To include your saved passwords as well, see [Back up your saved passwords](/backup/back-up-your-saved-passwords).

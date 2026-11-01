---
{
 "id": "backup/do-i-need-a-luneos-account",
 "title": "Do I need a LuneOS account?",
 "section": [],
 "order": 439.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "adb: com.palm.accountservices: Service does not exist (both devices)",
  "docs/audit/system.md (deleted backup/what-is-a-luneos-account)",
  "adb: luna-send com.palm.app.backup.service/listTargets (local target only)",
  "/usr/palm/applications/com.palm.app.preware2/build/app.js (Preware 2)"
 ],
 "review": []
}
---

No. LuneOS has no account of its own, and nothing is stored on a LuneOS server.

- To keep a copy of your information, use [Backup](/backup/what-does-backup-save). It stores the copy on your device.
- To get new apps, use [Preware 2](/software-manager/find-and-install-apps-with-preware-2).
- To get mail, contacts and calendars, add your own online accounts in [Accounts](/accounts/accounts-overview).

There is no way to locate or erase your device from a distance. To protect your information, set a screen lock ([learn how](/screen-and-lock/set-options-for-unlocking-the-screen)).

---
{
 "id": "calendar/check-c-dav-sync",
 "title": "Check C+DAV sync",
 "section": [],
 "order": 235.7,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.cdav/source/CDavApp.js:77-92 (labels)",
  "/usr/palm/applications/org.webosports.app.cdav/appinfo.json (title)",
  "adb: luna-send listLaunchPoints on the MindPhone lists C+DAV Sync App"
 ],
 "review": []
}
---

If contacts or events from a C+DAV account aren't showing up, the C+DAV Sync App shows what the sync is doing and lets you start one.

1. **[Open](/basics/open-an-application-in-the-launcher) C+DAV Sync App**.
2. If you have more than one C+DAV account, select the account.
3. Under **Stats**, see how many contacts, calendars, and events are on your device. Under **Status**, see whether a sync is running and how many items were downloaded and uploaded.
4. Under **Trouble shooting**, tap one of these:
   - **Start Sync:** Sync the account now.
   - **Do Auto Discovery:** Look for the account's calendars and address books on the server again.
   - **Trigger Slow Sync:** Go through everything in the account again on the next sync.

To sync your calendars the usual way, see [**Manually synchronize Calendar**](/calendar/manually-synchronize-calendar-with-your-online-accounts).

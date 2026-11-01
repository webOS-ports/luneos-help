---
{
 "id": "messaging/customize-messaging-notifications",
 "title": "Customize messaging notifications",
 "section": [],
 "order": 225,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/20745",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "org.webosports.messaging/app/src/views/PreferencesView.js:69",
  "org.webosports.messaging/app/src/views/PreferencesView.js:102",
  "adb: grep in /usr/palm/applications/org.webosports.app.messaging/index.html: 'Show Notifications', 'Vibrate', 'System Sound', 'Tap to pick a ringtone'",
  "org.webosports.messaging: ringtone picker launches com.palm.app.musicplayer, not installed on MindPhone"
 ],
 "requires": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Messaging** > **[Menu](/basics/open-the-application-menu)** (upper left) > **Preferences & Accounts**.
2. Under **New Message**, set any of the following:

   **Show Notifications:** Turn message notifications on or off.

   **Alert:** Choose **Vibrate**, **System Sound**, **Ringtone**, or **Mute**. If you choose **Ringtone**, tap **Tap to pick a ringtone**.

   **Past messages notification period:** Choose how old a message can be for you to get a notification when your device receives it.
3. Tap **Done**.

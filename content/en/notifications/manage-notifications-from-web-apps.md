---
{
 "id": "notifications/manage-notifications-from-web-apps",
 "title": "Manage notifications from web applications",
 "section": [],
 "order": 100103,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/NotificationsPage.qml:329",
  "adb: settings-common/qml/General/NotificationsPage.qml:340",
  "adb: settings-common/qml/Common/AppPermissionList.qml:65",
  "adb: settings-common/qml/Common/AppPermissionList.qml:297"
 ]
}
---

A web application asks before it shows notifications.

1. **[Open](/basics/open-an-application-in-the-launcher) Notifications**.
2. Under **Web Applications**, tap the application's name > tap one of the following:

   - **Allowed**
   - **Denied**
   - **Ask Again:** Forgets your answer, so the application asks the next time.

An application that says **Allowed (system)** or **Allowed (by app)** can be changed only to **Denied**.

---
{
 "id": "notifications/turn-notifications-from-an-app-on-off",
 "title": "Turn notifications from an application on/off",
 "section": [],
 "order": 100101,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/NotificationsPage.qml:247",
  "adb: settings-common/qml/General/NotificationsPage.qml:314",
  "adb: settings-common/qml/General/NotificationsPage.qml:186",
  "adb: settings-common/qml/General/NotificationsPage.qml:359"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Notifications**.
2. Under **Applications**, turn the application's switch on or off.

An application that is off can't put a banner on the screen. It can still do everything else it does. System messages, such as a low battery or a missed call, arrive whatever you set here.

There's no switch for all notifications at once. If you see **Currently off**, something such as a call has paused notifications for everything, and they come back on by themselves.

To choose whether notifications show when the screen is locked, see [Get notifications when the screen is locked or off](/screen-and-lock/get-notifications-when-the-screen-is-locked-or-off).

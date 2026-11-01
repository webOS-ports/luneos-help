---
{
 "id": "notifications/choose-a-notification-light-color",
 "title": "Choose a notification light color",
 "section": [],
 "order": 100102,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/NotificationsPage.qml:114",
  "adb: settings-common/qml/General/NotificationsPage.qml:205",
  "adb: settings-common/qml/General/NotificationsPage.qml:233",
  "adb: settings-common/qml/General/NotificationsPage.qml:289",
  "luna-next-cardshell/qml/Notifications/NotificationLed.qml:170"
 ]
}
---

If your device has a notification light, you can choose the color it blinks. Only some devices have one.

1. **[Open](/basics/open-an-application-in-the-launcher) Notifications**.
2. Do any of the following:

   - To set the color for all applications: Under **Notification LED**, tap **Default colour** > tap a color.
   - To set the color for one application: Under **Applications**, make sure its switch is on, tap **LED colour** under it > tap a color. Tap **Default** to go back to the default color.

If you see a message that the notification LED is switched off, turn on **Blink Notifications** ([learn how](/screen-and-lock/turn-blink-notifications-on-off)).

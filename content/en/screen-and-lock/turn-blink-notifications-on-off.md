---
{
 "id": "screen-and-lock/turn-blink-notifications-on-off",
 "title": "Turn blink notifications on/off",
 "section": [],
 "order": 516,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/40068",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/ScreenLockPage.qml:424",
  "adb: /usr/lib/qml/WebOSCompositor/qml/Notifications/NotificationLed.qml:114",
  "adb: getPreferences BlinkNotifications true; /etc/palm/defaultPreferences.txt",
  "adb: settings-common/qml/General/NotificationsPage.qml:205"
 ]
}
---

**[Open](/basics/open-an-application-in-the-launcher) Screen & Lock** > under **Notifications**, turn **Blink Notifications** on or off.

If your device has a notification light, it blinks while the screen is off and a notification is waiting. Blink notifications are on by default.

To choose the color, see [Choose a notification light color](/notifications/choose-a-notification-light-color).

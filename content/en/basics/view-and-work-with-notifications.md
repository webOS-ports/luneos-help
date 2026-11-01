---
{
 "id": "basics/view-and-work-with-notifications",
 "title": "View and work with notifications",
 "section": [],
 "order": 53,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26837",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/Notifications/NotificationArea.qml:113-124",
  "qml/Notifications/NotificationAreaTablet.qml",
  "qml/Notifications/SwipeableNotification.qml",
  "qml/Notifications/NotificationLed.qml",
  "adb: screencaptures/20261030161731.png Music dashboard on phone, 20261007123138.png on tablet",
  "adb: settings-common ScreenLockPage.qml:424 Blink Notifications"
 ]
}
---

<!-- ui:phone -->

Notifications appear at the bottom of the screen, above the gesture area.

**Banners** appear briefly in a small strip. After a few seconds, a banner becomes an icon at the bottom of the screen.

**Dashboard items** are the expanded view. Tap the icons at the bottom of the screen to see them, and then tap an item to act on it.

**Pop-up notifications** are larger and need a response, such as incoming calls and alarms.

Some applications keep a dashboard item open while they work. For example, Music shows playback controls after you leave the application.

To remove a dashboard item, throw it off the side of the screen. To close the dashboard, tap the gesture area or tap outside it.

If you get a notification while the screen is off, the notification light blinks, if your device has one. You can turn this off ([learn how](/screen-and-lock/turn-blink-notifications-on-off)).

<!-- ui:tablet -->

Notifications appear at the top of the screen, in the status bar.

**Banners** appear briefly in a small strip. After a few seconds, a banner becomes an icon in the status bar.

**Dashboard items** are the expanded view. Tap the icons in the status bar to see them, and then tap an item to act on it.

**Pop-up notifications** are larger and need a response, such as alarms.

Some applications keep a dashboard item open while they work. For example, Music shows playback controls after you leave the application.

To remove a dashboard item, throw it off the side of the screen. To close the dashboard, tap the gesture area or tap outside it.

If you get a notification while the screen is off, the notification light blinks, if your device has one. You can turn this off ([learn how](/screen-and-lock/turn-blink-notifications-on-off)).

---
{
 "id": "basics/open-the-launcher",
 "title": "Open the Launcher",
 "section": [
  "Move around on your device"
 ],
 "order": 14,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27335",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/LaunchBar/Launcher.qml onSwipeUpGesture, onToggleLauncherDisplay",
  "qml/Connectors/HardwareKeys.qml:_defaultActions, navigationKeys"
 ]
}
---

Do one of the following:

- In Card view, tap the Launcher icon at the right end of Quick Launch.
- In Card view, flick up on the gesture area.
- {if:keyboard}Press the **Menu** or **Home** key, if your device has one. On some keyboards these keys do something else.

If an application fills the screen, [display Card view](/basics/display-card-view-minimize-an-application) first.

To close the Launcher, flick up on the gesture area again, or tap the Launcher icon.

---
{
 "id": "appearance/lock-the-screen-rotation",
 "title": "Lock the screen rotation",
 "section": [],
 "order": 100204,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/DisplayPage.qml:215",
  "adb: settings-common/qml/General/DisplayPage.qml:230",
  "adb: /usr/lib/qml/WebOSCompositor/qml/StatusBar/SystemMenu/RotationLockElement.qml",
  "luna-next-cardshell/qml/StatusBar/SystemMenu/SystemMenu.qml:363"
 ]
}
---

Rotation lock keeps the screen at the orientation it is in, instead of following the device.

Do one of the following:

- Open the [system menu](/basics/open-the-connection-menu) and tap **Turn on Rotation Lock** or **Turn off Rotation Lock**.
- **[Open](/basics/open-an-application-in-the-launcher) Display** > under **Screen**, turn **Rotation Lock** on or off.

Hold the device the way you want it before you turn rotation lock on.

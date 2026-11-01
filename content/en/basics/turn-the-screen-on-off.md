---
{
 "id": "basics/turn-the-screen-on-off",
 "title": "Turn the screen on/off",
 "section": [
  "Turn your device on/off"
 ],
 "order": 10,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27003",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "luna-displaymanager/Src/DisplayStates.cpp DisplayEventPowerKeyPress",
  "qml/LockScreen/PadLock.qml:130 Drag up to unlock",
  "adb: settings-common ScreenLockPage.qml:109 Off, Pattern, Simple PIN, Password"
 ]
}
---

{if:powerbutton}To turn the screen off, press the **power** button. Press it again to turn the screen on.

{if:!powerbutton}The screen turns off by itself after a period of inactivity.

When the screen turns on, you may need to unlock it. Drag the lock icon up, or enter your PIN, password or pattern.

To save power, the screen dims after a period of inactivity, and then turns off. Tap the screen to brighten it after it dims. This doesn't affect a call.

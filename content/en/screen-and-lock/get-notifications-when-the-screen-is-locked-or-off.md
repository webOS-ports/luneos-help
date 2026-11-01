---
{
 "id": "screen-and-lock/get-notifications-when-the-screen-is-locked-or-off",
 "title": "Get notifications when the screen is locked",
 "section": [],
 "order": 355,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/17787",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/ScreenLockPage.qml:406",
  "showAlertsWhenLocked read only by libLunaSysMgrCommon, no consumer in the shell QML"
 ]
}
---

**[Open](/basics/open-an-application-in-the-launcher) Screen & Lock** > under **Notifications**, turn **Show When Locked** on or off.

To have a light blink for notifications while the screen is off, see [Turn blink notifications on/off](/screen-and-lock/turn-blink-notifications-on-off).

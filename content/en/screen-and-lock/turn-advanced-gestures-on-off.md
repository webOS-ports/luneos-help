---
{
 "id": "screen-and-lock/turn-advanced-gestures-on-off",
 "title": "Turn advanced gestures on/off",
 "section": [],
 "order": 352,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/17773",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/ScreenLockPage.qml:168",
  "adb: settings-common/qml/General/ScreenLockPage.qml:182",
  "adb: /usr/lib/qml/WebOSCompositor/qml/CardsArea.qml:295",
  "sysUiEnableNextPrevGestures read only by libLunaSysMgrCommon, no consumer in the shell"
 ]
}
---

**[Open](/basics/open-an-application-in-the-launcher) Screen & Lock** > under **Advanced Gestures**, turn **Enable Gestures** on or off.

Swipe up from the bottom of the screen to turn an open app into a card. Swipe up again to see the Launcher.

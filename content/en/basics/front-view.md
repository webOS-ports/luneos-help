---
{
 "id": "basics/front-view",
 "title": "Buttons and gesture area",
 "section": [
  "Get to know your device"
 ],
 "order": 0,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42817",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/CardsArea.qml:285-300,712-760",
  "qml/WindowManager/LunaGestureArea.qml",
  "qml/StatusBar/SystemMenu/SystemMenu.qml visible rules",
  "adb: PowerdAlerts.js",
  "files/tweaks/luna-next-cardshell.json showGestureArea"
 ]
}
---

LuneOS runs on many different devices, so buttons and connectors are in different places. These parts work the same on all of them:

- **Touchscreen:** Tap, flick and make other gestures directly on the screen.
- **Gesture area:** The black strip along the bottom of the screen. It's part of the screen, not a button.
  - Tap it or flick up to go from an application to Card view.
  - Flick up from Card view to open the Launcher.
  - Flick left to go back one level.
  - Flick right to [take a screenshot](/basics/take-a-screenshot).
- {if:powerbutton}**Power button:** Press to turn the screen on or off. Press and hold to open the power menu.
- {if:!powerbutton}**Power:** Use **Power** in the [system menu](/basics/open-the-connection-menu).
- {if:volumebutton}**Volume buttons:** Press to change the volume.
- {if:!volumebutton}**Volume:** Use the slider in the system menu.
- {if:keyboard}**Physical keyboard:** See [Use the keyboard](/basics/use-the-keyboard).

To turn the gesture area off, use **Show virtual gesture area** in Tweaks. You then flick up from the bottom edge of the screen instead, but the other gestures aren't available.

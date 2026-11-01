---
{
 "id": "screen-and-lock/adjust-the-screen-brightness",
 "title": "Adjust the screen brightness",
 "section": [],
 "order": 514,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/40051",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/General/DisplayPage.qml:139",
  "adb: /usr/lib/qml/WebOSCompositor/qml/StatusBar/SystemMenu/SystemMenu.qml BrightnessElement visible: Settings.hasBrightnessControl"
 ],
 "requires": [
  "brightness"
 ]
}
---

Do one of the following:

- **[Open](/basics/open-an-application-in-the-launcher) Display** > drag the **Brightness** slider.
- From any screen: Open the [system menu](/basics/open-the-connection-menu) > drag the brightness slider.

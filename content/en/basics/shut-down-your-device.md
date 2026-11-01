---
{
 "id": "basics/shut-down-your-device",
 "title": "Shut down your device",
 "section": [
  "Turn your device on/off"
 ],
 "order": 12,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26971",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: com.palm.systemui PowerdAlerts.js:83-84",
  "qml/Notifications/PowerMenu.qml:69,93,111",
  "qml/StatusBar/SystemMenu/PowerElement.qml:35",
  "no Reset Options in adb: org.webosports.app.settings-common qml/General/DeviceInfoPage.qml"
 ]
}
---

1. {if:powerbutton}Press and hold the **power** button.
1. {if:!powerbutton}Open the [system menu](/basics/open-the-connection-menu) and tap **Power**.
2. Tap **Shut Down**.

Shutting down turns off the screen and all wireless services. Do this when you won't use your device for a long time.

To turn your device back on, press and hold the **power** button until the screen lights up.

To put away the menu without shutting down, tap **Cancel**.

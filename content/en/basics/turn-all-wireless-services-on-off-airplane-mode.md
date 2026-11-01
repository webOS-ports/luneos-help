---
{
 "id": "basics/turn-all-wireless-services-on-off-airplane-mode",
 "title": "Turn all wireless services on/off (airplane mode)",
 "section": [
  "Turn your device on/off"
 ],
 "order": 11,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27037",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/Connectors/AirplaneModeService.qml:26-50",
  "adb: PowerdAlerts.js:77,102",
  "qml/StatusBar/SystemMenu/SystemMenu.qml active: !airplaneModeInProgress"
 ]
}
---

Turn on airplane mode whenever you must turn off all wireless features. It turns off Wi-Fi, Bluetooth and, on a device with a modem, calls, text messages and mobile data. You can still use applications like Calendar and Memos.

Do one of the following:

- Open the [system menu](/basics/open-the-connection-menu) and tap **Turn on Airplane Mode** or **Turn off Airplane Mode**.
- {if:powerbutton}Press and hold the **power** button, and then tap **Airplane Mode** or **Turn off Airplane Mode**.

In airplane mode, you can still turn Wi-Fi or Bluetooth on by itself from the system menu.

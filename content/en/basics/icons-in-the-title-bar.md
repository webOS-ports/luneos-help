---
{
 "id": "basics/icons-in-the-title-bar",
 "title": "Icons in the status bar",
 "section": [
  "Get to know your device"
 ],
 "order": 4,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42819",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/StatusBar/SystemIndicators.qml",
  "qml/StatusBar/Indicators/",
  "adb: screencaptures on both devices",
  "adb: org.webosports.app.settings-common qml/General/AppearancePage.qml:141-173"
 ]
}
---

Icons in the upper-right corner of the screen show the state of your device. Each one appears only when it applies.

- **Battery:** The charge level, and whether the battery is charging.
- **Wi-Fi:** Wi-Fi is on. Filled-in waves show the signal strength.
- **Bluetooth:** Bluetooth is on, or a device is connected.
- **Airplane:** Airplane mode is on.
- **Rotation lock:** Rotation lock is on.
- **Mute:** Sound is muted.
- **Headset:** A headset is connected.
- {if:modem}**Signal bars:** Filled-in bars show the signal strength of your phone network.
- {if:modem}**Network type:** The kind of data connection, such as **3G** or **4G**.

To change what the status bar shows, [open](/basics/open-an-application-in-the-launcher) **Appearance** on the **Prefs** tab.

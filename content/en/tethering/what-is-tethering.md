---
{
 "id": "tethering/what-is-tethering",
 "title": "What is tethering?",
 "section": [],
 "order": 397,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/43538",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/TetheringPage.qml:138",
  "adb: settings-common/qml/Connectivity/TetheringPage.qml:208",
  "adb: settings-common/qml/Connectivity/TetheringPage.qml:218",
  "adb: settings-common/qml/Connectivity/TetheringPage.qml:249",
  "adb: dbus-send net.connman.Manager.GetTechnologies (both devices)"
 ]
}
---

Tethering shares your device's Internet connection with other devices, such as a laptop. The **Tethering** app offers these ways to share, depending on what your device supports:

- **Wi-Fi Hotspot:** Other devices join your device's Wi-Fi network ([learn how](/tethering/create-a-secure-hotspot)).
- **Bluetooth:** Other devices connect over Bluetooth.
- **USB:** A computer plugged into your device reaches the Internet through it.

Your device can't be a hotspot and be joined to a Wi-Fi network at the same time, so turning on the hotspot drops the Wi-Fi connection.

{if:modem}While the hotspot is on, your device goes online over mobile data. Your wireless service provider may charge for this data, especially when roaming.

To turn sharing on or off, see [Use tethering](/tethering/use-tethering).

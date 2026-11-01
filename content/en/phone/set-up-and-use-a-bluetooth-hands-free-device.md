---
{
 "id": "phone/set-up-and-use-a-bluetooth-hands-free-device",
 "title": "Set up and use a Bluetooth® hands-free device",
 "section": [
  "Use a phone headset"
 ],
 "order": 125,
 "devices": [
  "phone"
 ],
 "origin": "palm/d400-01/19129",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.phone/qml/services/AudioRouteManager.qml:62",
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/BluetoothPage.qml:599",
  "adb: /usr/palm/applications/org.webosports.app.settings.networksettings/qml/Connectivity/BluetoothPage.qml:617",
  "org.webosports.app.phone/TODO:87 Bluetooth handsfree: the audio route is detected, but AT command handling",
  "adb: ps: ofonod -n --noplugin=hfp_bluez5 on MindPhone"
 ],
 "requires": [
  "modem"
 ]
}
---

1. Turn Bluetooth on ([**learn how**](/bluetooth/turn-the-bluetooth-feature-on-off)) and pair the device ([**learn how**](/bluetooth/make-a-pairing-request-to-another-device)).
2. To use a Bluetooth device with your device, follow the instructions that came with the Bluetooth device.
3. To change the audio route while on a call: Tap **Audio**. Each tap moves to the next route: handset, speaker, Bluetooth.

**Headset takes calls** in the Bluetooth settings sets whether a connected headset takes your calls.

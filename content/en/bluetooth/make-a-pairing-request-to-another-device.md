---
{
 "id": "bluetooth/make-a-pairing-request-to-another-device",
 "title": "Make a pairing request to another device",
 "section": [],
 "order": 413,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26932",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/lib/qml/LuneOS/Bluetooth/BluetoothManager.qml:93",
  "adb: settings-common/qml/Connectivity/BluetoothPage.qml:367",
  "adb: settings-common/qml/Connectivity/BluetoothPage.qml:390",
  "adb: settings-common/qml/Connectivity/BluetoothConfirmPassKeyPopup.qml:51",
  "adb: settings-common/qml/Connectivity/BluetoothDisplayPassKeyPopup.qml:46",
  "adb: settings-common/qml/Connectivity/BluetoothProvidePinCodePopup.qml:46"
 ]
}
---

The other device must be discoverable to appear on your device. Check the documentation that came with it for how to do that.

1. **[Open](/basics/open-an-application-in-the-launcher) Bluetooth**.
2. Make sure Bluetooth is on ([learn how](/bluetooth/turn-the-bluetooth-feature-on-off)).
3. Under **Choose a device**, wait for the device to appear, then tap its name. If it doesn't appear and **Search again** is displayed, tap **Search again**.
4. If a PIN appears, do what the screen asks:
   - If you are asked to confirm that the PIN displayed on the other device matches: Check that it does and tap **Confirm**.
   - If you are asked to enter a PIN or code on the other device: Enter it there, then tap **Close**.
   - If you are asked for a PIN: Enter the PIN from the other device's documentation and tap **Ok**.

A padlock beside the name means the device is paired. A check mark means it is connected.

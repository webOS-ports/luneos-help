---
{
 "id": "bluetooth/accept-a-pairing-request-from-another-device",
 "title": "Accept a pairing request from another device",
 "section": [],
 "order": 414,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26361",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common/qml/Connectivity/BluetoothPage.qml:331",
  "adb: settings-common/qml/Connectivity/BluetoothPage.qml:39",
  "adb: settings-common/qml/Connectivity/BluetoothConfirmAuthorizePopup.qml:49",
  "adb: settings-common/qml/Connectivity/BluetoothConfirmPassKeyPopup.qml:51",
  "no Bluetooth agent in qml/StatusBar or qml/Connectors"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Bluetooth**.
2. Make sure Bluetooth is on ([learn how](/bluetooth/turn-the-bluetooth-feature-on-off)).
3. Turn on **Discoverable**.
4. Start pairing from the other device, and leave the Bluetooth app open on your device.
5. If you are asked to allow pairing, tap **Allow**.
6. If a PIN appears, do what the screen asks:
   - If you are asked to confirm that the PIN displayed on the other device matches: Check that it does and tap **Confirm**.
   - If you are asked to enter a PIN or code on the other device: Enter it there, then tap **Close**.
   - If you are asked for a PIN: Enter the PIN from the other device's documentation and tap **Ok**.

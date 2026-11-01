---
{
 "id": "bluetooth/delete-a-device",
 "title": "Delete a device",
 "section": [],
 "order": 420,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26391",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: settings-common/qml/Connectivity/BluetoothPage.qml:509",
  "adb MindPhone: settings-common/qml/Connectivity/BluetoothDeviceInfoPopup.qml:216",
  "absent from the image on TouchPad"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Bluetooth**.
2. Touch and hold the name of a paired device > **Forget device**.

Forgetting a device removes the pairing, so you need to pair again to connect to it ([learn how](/bluetooth/make-a-pairing-request-to-another-device)). Disconnecting only ends the connection ([learn how](/bluetooth/disconnect-from-a-device)).

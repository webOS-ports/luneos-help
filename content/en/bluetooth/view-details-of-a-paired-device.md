---
{
 "id": "bluetooth/view-details-of-a-paired-device",
 "title": "View details of a paired device",
 "section": [],
 "order": 420.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: settings-common/qml/Connectivity/BluetoothDeviceInfoPopup.qml:126",
  "adb MindPhone: settings-common/qml/Connectivity/BluetoothDeviceInfoPopup.qml:181",
  "adb TouchPad: BluetoothDeviceInfoPopup.qml absent"
 ]
}
---

Not every device shows these details yet.

1. **[Open](/basics/open-an-application-in-the-launcher) Bluetooth**.
2. Under **Choose a device**, touch and hold a paired device.
3. Under **Device Info**, see the device's **Address**. **Type**, **Profiles**, and **Battery** appear if they are known.
4. Tap **Cancel**.

To remove the device from here, see [Delete a device](/bluetooth/delete-a-device).

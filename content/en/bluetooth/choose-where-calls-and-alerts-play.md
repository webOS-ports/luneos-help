---
{
 "id": "bluetooth/choose-where-calls-and-alerts-play",
 "title": "Choose where calls and alerts play",
 "section": [],
 "order": 420.3,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb MindPhone: settings-common/qml/Connectivity/BluetoothPage.qml:593",
  "adb MindPhone: settings-common/qml/Connectivity/BluetoothPage.qml:632"
 ],
 "requires": [
  "modem"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Bluetooth**.
2. Under **Calls**, turn these on or off:

   - **Headset takes calls:** A headset that connects during a call takes the call over. When this is off, the call stays where it is, and you can still move it to the headset in the Phone app.
   - **Alerts on phone speaker:** Alerts and notifications play on the phone's speaker instead of in the headset.

Not every device has these options yet.

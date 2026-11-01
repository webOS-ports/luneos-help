---
{
 "id": "network/receive-emergency-broadcasts",
 "title": "Receive emergency broadcasts",
 "section": [
  "Emergency Broadcast"
 ],
 "order": 100009,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb MindPhone: settings-common/qml/Connectivity/CellBroadcastPage.qml:201",
  "adb MindPhone: settings-common/qml/Connectivity/CellBroadcastPage.qml:217",
  "adb MindPhone: settings-common/qml/Connectivity/CellBroadcastPage.qml:227",
  "adb MindPhone: settings-common/qml/Connectivity/CellBroadcastPage.qml:327",
  "adb MindPhone: settings-common/qml/Connectivity/CellBroadcastPage.qml:336",
  "grep CellBroadcast: only Settings' page and telephonyd's interface list, nothing in the shell"
 ],
 "requires": [
  "modem"
 ]
}
---

Your network can send emergency warnings to every phone in an area. They are not messages and don't cost anything.

1. **[Open](/basics/open-an-application-in-the-launcher) Emergency Broadcast**.
2. If your device has two SIMs, tap **SIM** and choose one.
3. Turn on **Receive Alerts**.
4. Under **Alerts**, turn each type on or off: **Extreme Threats**, **Severe Threats**, **AMBER Alerts**, **Public Safety**, and **Operator Tests**.

Presidential-level alerts and earthquake and tsunami warnings arrive whatever you set here.

The most recent alert appears under **Last Received** while the Emergency Broadcast app is open. Don't count on your device to show or sound an alert anywhere else.

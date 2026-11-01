---
{
 "id": "phone/receive-emergency-alerts",
 "title": "Receive emergency alerts",
 "section": [
  "Customize device settings"
 ],
 "order": 138.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /usr/palm/applications/org.webosports.app.settings.cellbroadcast/appinfo.json",
  "adb: /usr/palm/applications/org.webosports.app.settings.cellbroadcast/qml/Connectivity/CellBroadcastPage.qml:192-360",
  "adb: dbus-send org.ofono.Manager.GetModems lists org.ofono.CellBroadcast on /ril_0 and /ril_1",
  "grep CellBroadcast in luna-next-cardshell/qml, org.webosports.app.phone/qml, webos-telephonyd/src: no matches"
 ],
 "requires": [
  "modem"
 ]
}
---

Your network can send emergency warnings to every phone in an area. These alerts aren't text messages and they cost nothing.

1. **[Open](/basics/open-an-application-in-the-launcher) Emergency Broadcast**.
2. Turn **Receive Alerts** on. If your device has two SIM cards, first choose the **SIM**.
3. Under **Alerts**, turn on the types you want: **Extreme Threats**, **Severe Threats**, **AMBER Alerts**, **Public Safety**, and **Operator Tests**.

Presidential-level alerts and earthquake and tsunami warnings arrive whatever you set here.

**Important:** An alert appears only under **Last Received** on this screen, and only while the screen is open. Your device doesn't show a pop-up, and it doesn't keep past alerts. Don't rely on your device as your only source of emergency warnings.

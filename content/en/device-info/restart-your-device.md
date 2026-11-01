---
{
 "id": "device-info/restart-your-device",
 "title": "Restart your device",
 "section": [
  "Reset your device"
 ],
 "order": 428,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/23453",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "/usr/palm/applications/com.palm.systemui/app/PowerdAlerts/PowerdAlerts.js:81-84 (Restart, Luna Next restart, Shut Down, Cancel)",
  "/usr/palm/applications/com.palm.systemui/data/PowerdService.js:204 (powerKeyPressed showDialog)",
  "/usr/lib/qml/WebOSCompositor/qml/ShutdownScreen.qml:36 (hardware button reaches PowerdAlerts)",
  "/usr/lib/qml/WebOSCompositor/qml/StatusBar/SystemMenu/SystemMenu.qml:469-476 (Power only without a power button)",
  "/usr/lib/qml/WebOSCompositor/qml/Notifications/PowerMenu.qml:69 (Device Restart)"
 ]
}
---

{if:powerbutton}Press and hold the power button, and tap **Restart**.

{if:!powerbutton}Open the System menu and tap **Power** > **Device Restart**.

If an application freezes, first try restarting your device. No files or settings are changed when you restart.

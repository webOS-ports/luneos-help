---
{
 "id": "basics/3-trigger-a-restart",
 "title": "3. Trigger a restart",
 "section": [
  "If your device stops responding"
 ],
 "order": 62.4,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/40434",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: com.palm.systemui app/PowerdAlerts/PowerdAlerts.js:82 Luna Next restart",
  "qml/Notifications/PowerMenu.qml:75 Luna-Next Restart",
  "forced restart by holding power not established: firmware behaviour, per device"
 ]
}
---

If the status bar and gestures still respond but the screen looks wrong, restart only the shell. Your device stays on.

1. {if:powerbutton}Press and hold the **power** button.
1. {if:!powerbutton}Open the [system menu](/basics/open-the-connection-menu) and tap **Power**.
2. {if:powerbutton}Tap **Luna Next restart**.
2. {if:!powerbutton}Tap **Luna-Next Restart**.

If the screen doesn't respond at all, keep the **power** button held down. Many devices restart by themselves after a while. How long it takes, and whether it works, depends on the device.

**NOTE:** Applications are forced to close during this kind of restart, so unsaved data may be lost.

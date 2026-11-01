---
{
 "id": "basics/2-turn-your-device-completely-off-and-on",
 "title": "2. Turn your device completely off and on",
 "section": [
  "If your device stops responding"
 ],
 "order": 62.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/49721",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: com.palm.systemui app/PowerdAlerts/PowerdAlerts.js:81-84 Restart, Shut Down",
  "qml/Notifications/PowerMenu.qml:51 Device Restart",
  "qml/StatusBar/SystemMenu/PowerElement.qml:35, only without power button"
 ]
}
---

**NOTE:** If the screen stays off or gestures don't work, skip to [3. Trigger a restart](/basics/3-trigger-a-restart).

1. {if:powerbutton}Press and hold the **power** button.
1. {if:!powerbutton}Open the [system menu](/basics/open-the-connection-menu) and tap **Power**.
2. {if:powerbutton}Tap **Restart**.
2. {if:!powerbutton}Tap **Device Restart**.

To shut down instead, tap **Shut Down**, and then press and hold the **power** button to start the device again.

**Why this might help**

A restart closes all applications, frees all memory and starts wireless services again.

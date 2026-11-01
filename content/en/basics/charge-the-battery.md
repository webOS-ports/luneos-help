---
{
 "id": "basics/charge-the-battery",
 "title": "Charge the battery",
 "section": [],
 "order": 8,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42726",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /media/internal/screencaptures/20261007082944.png USB Connected popup on the TouchPad",
  "adb: com.palm.systemui StoragedAlerts.js:45-62, PowerdAlerts.js:203",
  "qml/StatusBar/SystemMenu/BatteryElement.qml:75",
  "qml/StatusBar/Indicators/BatteryIndicator.qml"
 ]
}
---

1. Connect the USB cable to your device.
2. Connect the other end to the charger, and plug the charger into a working outlet.

The battery icon in the upper-right corner of the screen shows that the device is charging. To see the charge level, open the [system menu](/basics/open-the-connection-menu) and look at **Battery**.

If you connect the device to a computer instead, **USB Connected** appears. Tap **Charge only** to charge without sharing your files.

If you see **Device May Not Charge**, the charger or cable doesn't supply enough power.

---
{
 "id": "basics/copy-files-between-your-device-and-your-computer",
 "title": "Copy files between your device and your computer",
 "section": [
  "Sync personal data and copy files between your device and computer"
 ],
 "order": 54,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/28343",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: /media/internal/screencaptures/20261007082944.png, 20261007123138.png",
  "adb: com.palm.systemui StoragedAlerts.js:22,45-62,160,208",
  "adb: org.webosports.app.settings-common qml/Connectivity/UsbPage.qml:123,132-142"
 ]
}
---

1. Connect your device to your computer with the USB cable.
2. On your device, tap **File Transfer** in **USB Connected**.
3. On your computer, open the device. It shows up as a media device.
4. Drag files in either direction.
5. When you're done, eject the device on your computer, and then unplug the cable.

If you tapped **Charge only**, you can still start a transfer. Open the notifications and tap **USB**, or [open](/basics/open-an-application-in-the-launcher) **USB** on the **Prefs** tab and tap **Connect as media device**.

You can copy any file to your device, but you can open it only if an application on the device can read it.

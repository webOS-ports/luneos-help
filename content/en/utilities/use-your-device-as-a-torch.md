---
{
 "id": "utilities/use-your-device-as-a-torch",
 "title": "Use your device as a torch",
 "section": [],
 "order": 100104,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.torch/qml/main.qml (Tap to turn on/off, Torch unavailable; closing the card turns it off)",
  "adb: appinfo.json: visible false on the MindPhone, visible on the TouchPad",
  "adb: listLaunchPoints (Torch on the TouchPad only)",
  "adb: luna-send org.webosports.service.torch/getStatus (available true on both)",
  "luna-next-cardshell/qml/StatusBar/SystemMenu/NewDeviceMenu.qml:122-221 (Flashlight)"
 ],
 "review": []
}
---

The Torch app isn't in the Launcher on every device.

1. **[Open](/basics/open-an-application-in-the-launcher) Torch**.
2. Tap the screen to turn the light on. Tap again to turn it off.

If you see **Torch unavailable**, your device cannot use its light this way.

The light stays on while the app is in the background. It turns off when you close the Torch card.

If you use the New Device Menu, it has a **Flashlight** button as well ([learn how](/tweaks/use-the-new-device-menu)).

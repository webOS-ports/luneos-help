---
{
 "id": "storage/turn-developer-mode-on-or-off",
 "title": "Turn Developer Mode on or off",
 "section": [],
 "order": 100002,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/DeveloperOptionsPage.qml (Developer Mode, Debugging, USB Debugging, explanation texts)",
  "adb: appinfo.json of org.webosports.app.settings.devmodeswitcher (Developer Mode, visible)",
  "adb: luna-send org.webosports.service.devmode/getStatus (both devices)"
 ],
 "review": []
}
---

Developer Mode is for people who build or test software for LuneOS. You do not need it for everyday use.

1. **[Open](/basics/open-an-application-in-the-launcher) Developer Mode**.
2. Tap the **Developer Mode** switch.
3. To let a computer connect with the Android adb tool, also turn on **USB Debugging** under **Debugging**. This only works on devices that have the Android tools.

Turning Developer Mode off also turns off USB Debugging.

---
{
 "id": "launcher/reorder-launcher-icons",
 "title": "Reorder Launcher icons",
 "section": [],
 "order": 149,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/21553",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/LaunchBar/FullLauncher.qml drop areas, turnLeftTimer, dragArea, DONE",
  "qml/LaunchBar/LauncherTabConfig.qml saved in db8"
 ]
}
---

1. [Open the Launcher](/basics/open-the-launcher).
2. Tap and hold an icon until it glows. All icons get a frame.
3. Drag the icon to another place on the tab.
4. To move it to another tab, drag it over the tab's name, or hold it at the left or right edge of the screen until the tab changes.
5. Lift your finger, and then tap **DONE**.

While the icons have frames, you can drag any icon without holding it first. Tapping an empty part of the Launcher also ends this.

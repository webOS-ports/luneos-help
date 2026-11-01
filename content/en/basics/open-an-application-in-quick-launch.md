---
{
 "id": "basics/open-an-application-in-quick-launch",
 "title": "Open an application in Quick Launch",
 "section": [
  "Open applications"
 ],
 "order": 30,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27119",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/LaunchBar/Launcher.qml states launchbar, fullLauncher keep launchBarInstance visible",
  "adb: screencaptures/20261031075422.png"
 ]
}
---

In Card view or the Launcher, tap an icon in Quick Launch at the bottom of the screen.

If an application fills the screen, [display Card view](/basics/display-card-view-minimize-an-application) first.

---
{
 "id": "basics/reorder-quick-launch-icons",
 "title": "Reorder Quick Launch icons",
 "section": [
  "Manage applications"
 ],
 "order": 40,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27679",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/LaunchBar/LaunchBar.qml:147-176",
  "does the order survive a restart: refreshConfig() rebuilds from /etc/palm/default-dock-positions.json, LaunchBar.qml:335-354"
 ]
}
---

1. [Display Card view](/basics/display-card-view-minimize-an-application).
2. Tap and hold a Quick Launch icon until it glows.
3. Drag it left or right to another position, and lift your finger.

The Launcher icon stays where it is.

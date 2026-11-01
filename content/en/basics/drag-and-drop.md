---
{
 "id": "basics/drag-and-drop",
 "title": "Drag and drop",
 "section": [
  "Move around on your device"
 ],
 "order": 26,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27223",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/LaunchBar/LaunchBar.qml:dragArea",
  "qml/LaunchBar/FullLauncher.qml:dragArea",
  "qml/CardView/CardWindowWrapper.qml:175"
 ]
}
---

Tap and hold an item, wait for it to change, drag it, and lift your finger to drop it.

You can use drag and drop to move icons in Quick Launch and the Launcher, and to move cards in Card view. Some applications use it to reorder lists.

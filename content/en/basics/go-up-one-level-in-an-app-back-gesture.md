---
{
 "id": "basics/go-up-one-level-in-an-app-back-gesture",
 "title": "Go up one level in an app (back gesture)",
 "section": [
  "Move around on your device"
 ],
 "order": 15,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27421",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/CardView/CardView.qml:327-333 swipe left sends Escape",
  "qml/Connectors/HardwareKeys.qml:_sendBack"
 ]
}
---

The back gesture is a quick flick from right to left in the gesture area. It takes you up one level in an application.

For example, make the back gesture while reading an email message to return to the list of messages.

Not every screen has a level to go back to.

{if:keyboard}If your device has a **Back** key, it does the same thing.

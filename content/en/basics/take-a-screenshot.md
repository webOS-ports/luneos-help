---
{
 "id": "basics/take-a-screenshot",
 "title": "Take a screenshot",
 "section": [],
 "order": 61,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26805",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/CardsArea.qml:285-290",
  "adb: ls /media/internal/screencaptures on both devices",
  "org.webosports.app.photos/qml/js/Library.js:43"
 ]
}
---

Flick from left to right in the gesture area. The screen flashes and you hear a camera shutter.

The picture is saved as a PNG file. It's in the **Screen captures** album in Photos & Videos, and in the **screencaptures** folder when you copy files to your computer ([learn how](/basics/copy-files-between-your-device-and-your-computer)).

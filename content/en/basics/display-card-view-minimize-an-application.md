---
{
 "id": "basics/display-card-view-minimize-an-application",
 "title": "Display Card view (minimize an application)",
 "section": [
  "Move around on your device"
 ],
 "order": 13,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/27247",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/CardView/CardView.qml:330-345",
  "qml/CardsArea.qml:295-300 onScreenEdgeFlickEdgeBottom, only while the gesture area is hidden",
  "qml/LaunchBar/Launcher.qml states"
 ]
}
---

When an application fills the screen, tap the gesture area to see Card view. You can also flick up on the gesture area.

Some applications cover the whole screen and hide the gesture area. Flick up from the bottom edge of the screen to get back to Card view.

Card view shows your open applications as cards, in front of your wallpaper. It's also where you find the Just Type field and Quick Launch.

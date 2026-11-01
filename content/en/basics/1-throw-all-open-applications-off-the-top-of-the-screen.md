---
{
 "id": "basics/1-throw-all-open-applications-off-the-top-of-the-screen",
 "title": "1. Throw all open applications off the top of the screen",
 "section": [
  "If your device stops responding"
 ],
 "order": 62,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/28399",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/CardView/CardView.qml:330-345 tap and swipe up",
  "qml/CardView/SwipeableCard.qml throw"
 ]
}
---

**NOTE:** If the screen stays off or gestures don't work, skip to [3. Trigger a restart](/basics/3-trigger-a-restart).

1. If an application fills the screen and isn't responding, tap the gesture area or flick up on it to go to Card view.
2. Throw the card off the top of the screen to close the application.
3. Throw any other open cards off the top of the screen.

**Why this might help**

An open application can hold on to so much memory that there isn't enough left for anything else. Closing applications frees it.

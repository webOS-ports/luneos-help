---
{
 "id": "basics/why-the-screen-goes-dark",
 "title": "Why the screen goes dark",
 "section": [],
 "order": 59,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26653",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: settings-common qml/General/DisplayPage.qml:104 1, 2, 5, 10 minutes",
  "luna-displaymanager/Src/DisplayManager.cpp proximity"
 ]
}
---

When your device is idle, the screen dims and then turns off. This is normal. You can set this interval to as long as 10 minutes ([learn how](/screen-and-lock/set-the-interval-for-turning-the-screen-off-automatically)).

Tap the screen to brighten it after it dims. After it turns off, press the **power** button.

{if:modem}The screen also goes dark while you're on a call and hold the device to your ear, so that you don't tap something by accident. It turns back on when you move the device away.

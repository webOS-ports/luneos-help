---
{
 "id": "exhibition/which-apps-work-in-exhibition",
 "title": "Which apps work in Exhibition?",
 "section": [],
 "order": 159.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "adb: luna-send com.palm.applicationManager/listDockModeLaunchPoints (Music, Photos & Videos on both)",
  "adb: grep exhibitionMode in appinfo.json of all apps",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/ExhibitionPage.qml:69-125 (list, Time fixed, No installed application...)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/ExhibitionPage.qml:128 (stale note)",
  "/usr/lib/qml/WebOSCompositor/qml/DockMode/ExhibitionCarousel.qml:23-37 (one page per app, started when its page opens)"
 ],
 "review": []
}
---

**Time** is always there. **Music** and **Photos & Videos** also have an Exhibition page.

Other apps can have one too. An app that supports Exhibition is added to the list in Exhibition settings as soon as you install it. If no app supports it, the list says **No installed application supports Exhibition mode.**

Each app you check gets its own full-screen page. An app starts when you first go to its page and does not show up as a card.

The note on the Exhibition settings screen says only clocks are shown so far. That note is out of date: checked apps do appear.

To choose your apps, see [Customize Exhibition settings](/exhibition/customize-exhibition-settings).

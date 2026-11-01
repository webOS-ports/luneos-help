---
{
 "id": "exhibition/view-a-picture-slideshow",
 "title": "View a picture slideshow",
 "section": [],
 "order": 161,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/35285",
 "status": "verified-source",
 "review": [],
 "evidence": [
  "adb: luna-send com.palm.applicationManager/listDockModeLaunchPoints (exhibitionModeTitle Photos, enabled false)",
  "/usr/palm/applications/org.webosports.app.photos/qml/SlideshowView.qml:35 (tap shows the bars), :226 (five seconds)",
  "/usr/palm/applications/org.webosports.app.photos/qml/SlideshowView.qml:200 (no pictures message)",
  "/usr/palm/applications/org.webosports.app.photos/qml/SlideshowView.qml:252-285 (Select Album, shuffle, play/pause, Show Each Photo For)",
  "/usr/palm/applications/org.webosports.app.photos/qml/SlideshowView.qml:294 (none ticked is all albums)"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Exhibition** and check **Photos & Videos** ([learn how](/exhibition/customize-exhibition-settings)).
2. In Exhibition, tap the page name in the upper-left corner of the screen > **Photos**. The slideshow starts automatically. It uses all your albums until you choose some.
3. To display the controls, tap the screen. They disappear after five seconds.
4. When the controls are displayed, do any of the following:
   - To choose albums for the slideshow: Tap **Select Album** > the albums you want. This button appears when more than one album has pictures.
   - To play the pictures in random order: Tap the shuffle button.
   - To pause or resume: Tap the pause or play button.
   - To change how long each picture stays on the screen: Tap the timer button > a time interval.
5. To move to the next or previous picture: Swipe left or right on the screen.

To end the slideshow, exit Exhibition ([learn how](/exhibition/exit-exhibition)).

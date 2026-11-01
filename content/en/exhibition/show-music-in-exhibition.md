---
{
 "id": "exhibition/show-music-in-exhibition",
 "title": "Show music in Exhibition",
 "section": [],
 "order": 159.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.music/appinfo.json (exhibitionMode)",
  "/usr/palm/applications/org.webosports.app.music/qml/ExhibitionView.qml:28-31 (cover, clock, track)",
  "/usr/palm/applications/org.webosports.app.music/qml/ExhibitionView.qml:160-210 (controls, Nothing playing, Shuffle All)",
  "adb: luna-send com.palm.applicationManager/listDockModeLaunchPoints (Music)"
 ],
 "review": []
}
---

The Music page shows the cover of the song that is playing, a large clock, the song and how far along it is, with big buttons you can reach from a distance.

1. In Exhibition settings, check **Music** ([learn how](/exhibition/customize-exhibition-settings)).
2. Start Exhibition ([learn how](/exhibition/start-exhibition)).
3. Tap the page name in the upper-left corner of the screen > **Music**.
4. Use the buttons to go to the previous song, play or pause, or go to the next song.

If you see **Nothing playing**, tap **Shuffle All** to play your whole library in random order.

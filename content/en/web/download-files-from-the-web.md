---
{
 "id": "web/download-files-from-the-web",
 "title": "Download files from the web",
 "section": [],
 "order": 373,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/5999",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.atlas/source/BrowserContextMenu.js:30",
  "/usr/palm/applications/org.webosports.app.atlas/source/DownloadList.js:49",
  "/usr/palm/applications/org.webosports.app.atlas/source/BrowserApp.js:719",
  "/usr/palm/applications/org.webosports.app.atlas/source/BrowserApp.js:162",
  "adb: grep -c media/internal/downloads /usr/sbin/LunaDownloadMgr (2); ls -d /media/internal/downloads on both devices"
 ]
}
---

1. In Atlas Web, go to the page with the file.
2. Tap the link to the file, or press and hold the link > **Download Link**.
3. The Downloads tab of the drawer opens and shows the progress. Tap **Open** when the file is done.

Files are saved in the downloads folder of your device's internal storage. A message tells you when a download finishes.

To remove an entry from the list, swipe it off the side of the screen. **Clear** empties the list. Neither deletes the file.

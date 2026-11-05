---
{
 "id": "videos/watch-owncast-live-streams",
 "title": "Watch Owncast live streams",
 "section": [],
 "order": 326.6,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/owncast/account/org.webosports.video.owncast/org.webosports.video.owncast.json (loc_name Owncast)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:83",
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:211 (STREAMS picker)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/owncast/provider/index.js:256 (search only for the directory)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/owncast/provider/index.js:263",
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/owncast/provider/index.js:268",
  "org.webosports.app.videoplayer/qml/BrowsePage.qml:108",
  "adb: ls /usr/palm/public/accounts on the MindPhone (no org.webosports.video.owncast)"
 ],
 "requires": [],
 "review": []
}
---

Owncast in Videos needs a newer LuneOS build than some devices have.

Owncast is live streaming that people run on their own servers. You can watch whatever is live in the Owncast Directory, or one server.

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account** > **Owncast**.
2. Under **STREAMS**, pick one:
   - **Owncast Directory:** The streams that are live now on the servers listed at directory.owncast.online.
   - **One Owncast server:** Enter the address you watch the stream at, for example live.example.org.
3. Tap **Add**.
4. **[Open](/basics/open-an-application-in-the-launcher) Videos** and tap the Owncast tab.
5. Tap a stream:
   - **Owncast Directory:** Under **Live Now**, or tap a category or **All Live Streams**.
   - **One server:** Its stream is under **Live Now**. If nothing is on, you see **Not Live Right Now**.

In the Owncast Directory you can also type in **Search** under the tabs and tap Enter.

A live stream shows **● LIVE** and has no seek bar.

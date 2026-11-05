---
{
 "id": "videos/watch-german-austrian-and-swiss-public-tv",
 "title": "Watch German, Austrian and Swiss public TV",
 "section": [],
 "order": 326.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "unreleased",
 "evidence": [
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/mediathek/account/org.webosports.video.mediathek/org.webosports.video.mediathek.json (loc_name Mediathek)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:76",
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/mediathek/provider/index.js:52 (channels)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/mediathek/provider/index.js:88 (New, Live TV, a section per channel)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) video/mediathek/provider/index.js:184 (Only in its own country)",
  "org.webosports.app.videoplayer/qml/PlayerView.qml:962",
  "org.webosports.app.videoplayer/qml/js/Online.js:112 (the subtitle under a tile)",
  "adb: ls /usr/palm/public/accounts on the MindPhone (no org.webosports.video.mediathek)"
 ],
 "requires": [],
 "review": []
}
---

Mediathek in Videos needs a newer LuneOS build than some devices have.

Mediathek brings the libraries of the German, Austrian and Swiss public broadcasters into Videos: ARD and its regional channels, ZDF, Arte, 3sat, KiKA, ORF, SRF and more. There is nothing to sign in to.

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account** > **Mediathek** > **Add**.
2. **[Open](/basics/open-an-application-in-the-launcher) Videos** and tap the **Mediathek** tab.
3. Tap a programme under **New**, a channel under **Live TV**, or tap a broadcaster to see its programmes.

To find a programme, type in **Search** under the tabs and tap Enter.

A programme marked **Only in its own country** plays only in that country. A live channel shows **● LIVE** and has no seek bar.

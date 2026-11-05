---
{
 "id": "videos/watch-tv-channels-from-an-m3u-list",
 "title": "Watch TV channels from an M3U list",
 "section": [],
 "order": 326.3,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "unreleased",
 "evidence": [
  "luneos-synergy-connectors/video/m3u/account/org.webosports.video.m3u/org.webosports.video.m3u.json (loc_name M3U Playlist)",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:68",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:123",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:128",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:132",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:249 (Free TV list of the device's region picked first)",
  "luneos-synergy-connectors/video/m3u/provider/index.js:152 (All countries)",
  "luneos-synergy-connectors/video/m3u/provider/index.js:361 (All Channels, a section per group)",
  "org.webosports.app.videoplayer/qml/PlayerView.qml:78",
  "org.webosports.app.videoplayer/qml/PlayerView.qml:962 (LIVE instead of the time)",
  "org.webosports.app.videoplayer/qml/PlayerView.qml:979",
  "org.webosports.app.videoplayer/qml/PlayerView.qml:1064 (no speed for a live channel)",
  "adb: ls /usr/palm/public/accounts on the MindPhone (no org.webosports.video.m3u)"
 ],
 "requires": [],
 "review": []
}
---

TV channels in Videos need a newer LuneOS build than some devices have.

You can watch the free channels of a country from the Free TV lists, or your own M3U playlist, such as the one an IPTV service gives you.

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account** > **M3U Playlist**.
2. Under **CHANNELS**, pick a list:
   - **Free TV –** and a country. Your device's country is picked to begin with. **All countries** has every list in one.
   - **My own playlist:** Enter the list's web address under **PLAYLIST ADDRESS**, exactly as the service gives it. Under **NAME (OPTIONAL)**, you can give it a name.
3. Tap **Add**.
4. **[Open](/basics/open-an-application-in-the-launcher) Videos** and tap the list's tab.
5. Tap a channel. If the list has groups, tap **All Channels** or a group first.

A channel plays live: Videos shows **● LIVE** instead of the time, and there's no seek bar, no jumping back or forward and no speed. Videos doesn't remember where you were in a channel.

Some Free TV channels play only in their own country.

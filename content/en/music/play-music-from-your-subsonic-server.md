---
{
 "id": "music/play-music-from-your-subsonic-server",
 "title": "Play music from your Subsonic server",
 "section": [],
 "order": 310.31,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "luneos-synergy-connectors/music/subsonic/account/org.webosports.app.music.subsonic/org.webosports.app.music.subsonic.json (loc_name Subsonic, capability Music)",
  "luneos-synergy-connectors/music/_core/apps/org.webosports.app.musicauth/source/musicAuth.js:75",
  "luneos-synergy-connectors/music/_core/apps/org.webosports.app.musicauth/source/musicAuth.js:79",
  "luneos-synergy-connectors/music/_core/apps/org.webosports.app.musicauth/source/musicAuth.js:182",
  "luneos-synergy-connectors/music/_core/service/subsonic.go:317 (playlists)",
  "luneos-synergy-connectors/music/_core/service/subsonic.go:539 (artists and albums to browse)",
  "org.webosports.app.music/qml/views/StreamingView.qml:44 (Artists, albums and search)",
  "org.webosports.app.music/qml/pages/StreamLibraryPage.qml:82 (Search <service>)",
  "org.webosports.app.music/qml/pages/StreamLibraryPage.qml:95 (NEWEST ALBUMS)",
  "org.webosports.app.music/qml/pages/StreamLibraryPage.qml:132 (ARTISTS)",
  "org.webosports.app.music/qml/main.qml:1188 (an album's menu: Go to Artist)",
  "meta-luneos/recipes-luneos/synergy/luneos-synergy-music_git.bb:69 (MUSIC_PROVIDERS has no subsonic)",
  "adb: ls /usr/palm/public/accounts and /usr/palm/applications/org.webosports.app.music/qml/pages on the MindPhone (no Subsonic template, no StreamLibraryPage.qml)"
 ],
 "requires": [],
 "review": []
}
---

Subsonic needs a newer LuneOS build than some devices have.

Subsonic works with your own music server: Navidrome, Airsonic, Gonic or any other server that speaks the Subsonic API.

**To add your server**

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account** > **Subsonic**.
2. Under **SERVER**, enter the address you open the server at in a browser, for example nas.local:4533.
3. Enter your **USERNAME** and **PASSWORD**, then tap **Sign In**.

**To play from it**

1. **[Open](/basics/open-an-application-in-the-launcher) Music** > tap **Streaming** > **Subsonic**.
2. Do one of the following:
   - Tap an album under **NEWEST ALBUMS**.
   - Tap an artist under **ARTISTS**. You see their albums, then their songs.
   - Tap **Search Subsonic** to look for a song.
3. Tap a song, or tap **Play** or **Shuffle**.

Tap and hold an album for what to do with its songs, and for **Go to Artist**.

Your server's playlists are in Music's **Playlists** ([learn how](/music/play-your-playlists-from-a-streaming-service)).

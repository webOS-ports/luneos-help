---
{
 "id": "music/add-your-own-radio-stations",
 "title": "Add your own radio stations",
 "section": [],
 "order": 310.33,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "unreleased",
 "evidence": [
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/apps/org.webosports.app.musicauth/source/musicAuth.js:92 (YOUR STATION LIST (OPTIONAL))",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/apps/org.webosports.app.musicauth/source/musicAuth.js:287",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/apps/org.webosports.app.musicauth/source/musicAuth.js:294",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/service/radio.go:863 (each list read before it is kept; at most 20)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/service/radio.go:700 (a playlist per group)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/service/radio.go:267 (M3U and PLS)",
  "no code removes a kept list (no writer of radio-lists but handleRadioAuthLists)"
 ],
 "requires": [],
 "review": []
}
---

Internet Radio needs a newer LuneOS build than some devices have.

You can add a list of your own stations: the web address of an M3U or PLS playlist. A station's own stream address works too.

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account** > **Internet Radio**.
2. Under **YOUR STATION LIST (OPTIONAL)**, enter the list's address, for example https://example.org/stations.m3u.
3. Tap **Add Internet Radio**. Music reads the list before it keeps it.
4. **[Open](/basics/open-an-application-in-the-launcher) Music** > tap **Playlists**. Your list is at the top under **INTERNET RADIO**. If the list has groups of stations, each group is a playlist of its own.

If the list can't be read, you see why, and the account isn't added yet. Check the address. It can't hold a user name or password before the server's name.

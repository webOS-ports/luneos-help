---
{
 "id": "music/listen-to-internet-radio",
 "title": "Listen to internet radio",
 "section": [],
 "order": 310.32,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "unreleased",
 "evidence": [
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/radio/account/org.webosports.app.music.radio/org.webosports.app.music.radio.json (loc_name Internet Radio, capability Music)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/apps/org.webosports.app.musicauth/source/musicAuth.js:190 (Add Internet Radio)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/service/radio.go:682 (Most played, Most liked)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/service/radio.go:686 (Popular in <country>)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/service/radio.go:70 (genres)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/service/radio.go:557 (search: own lists, then Radio Browser)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/service/radio.go:749 (owner Radio Browser)",
  "org.webosports.app.music/qml/views/PlaylistsView.qml:53 (a heading per service)",
  "org.webosports.app.music/qml/js/Streaming.js:117 (the account's templateId org.webosports.app.music.radio lets it show)",
  "adb: ls /usr/palm/public/accounts on the MindPhone (no org.webosports.app.music.radio)"
 ],
 "requires": [],
 "review": []
}
---

Internet Radio needs a newer LuneOS build than some devices have.

Internet Radio plays the stations of Radio Browser, a free directory of tens of thousands of stations. There is nothing to sign in to.

**To add it**

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account** > **Internet Radio**.
2. Tap **Add Internet Radio**. You can first add a station list of your own ([learn how](/music/add-your-own-radio-stations)).

**To listen**

1. **[Open](/basics/open-an-application-in-the-launcher) Music** > tap **Playlists**.
2. Scroll to **INTERNET RADIO**. You see **Most played**, **Most liked**, the stations popular in your country, and lists for Pop, Rock, News, Jazz, Classical, Dance, Electronic, Talk, Hits and Oldies.
3. Tap a list, then tap a station.

To look for a station by name, tap **Streaming** > **Internet Radio** and type its name. Your own station lists are searched first.

A station plays as long as you listen: it has no length and no end.

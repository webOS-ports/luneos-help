---
{
 "id": "videos/watch-videos-from-a-media-server",
 "title": "Watch videos from a media server",
 "section": [],
 "order": 326.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "org.webosports.app.videoplayer/qml/components/SourceBar.qml:63",
  "org.webosports.app.videoplayer/qml/components/SourceBar.qml:77",
  "org.webosports.app.videoplayer/qml/BrowsePage.qml:84 (back: search, up a level, This Device)",
  "org.webosports.app.videoplayer/qml/BrowsePage.qml:108 (one section opens on its list)",
  "org.webosports.app.videoplayer/qml/BrowsePage.qml:305 (Search <server>)",
  "org.webosports.app.videoplayer/qml/BrowsePage.qml:368",
  "org.webosports.app.videoplayer/qml/BrowsePage.qml:554 (seasons)",
  "org.webosports.app.videoplayer/qml/main.qml:177 (servers asked for again on coming back)",
  "org.webosports.app.videoplayer/qml/main.qml:384 (headset next/previous: next episode)",
  "org.webosports.app.videoplayer/README.md (Streams from servers: subtitles, where it was left)",
  "luneos-synergy-connectors/video/jellyfin/provider/index.js:257",
  "luneos-synergy-connectors/video/plex/provider/index.js:396",
  "luneos-synergy-connectors/video/peertube/provider/index.js:28",
  "MindPhone /usr/palm/applications/org.webosports.app.videoplayer/qml has no BrowsePage.qml or SourceBar.qml"
 ],
 "requires": [],
 "review": []
}
---

Media servers in Videos need a newer LuneOS build than some devices have. First add the server in Accounts ([learn how](/videos/add-a-media-server-account)).

1. **[Open](/basics/open-an-application-in-the-launcher) Videos**.
2. Tap the server's tab at the top. **This Device** goes back to the videos on your device.
3. Tap a video in one of the rows, such as **Continue Watching** or **Recently Added**, or tap a library to see all of it.
4. To watch a series, tap it, tap a season above the list of episodes, then tap an episode.

To find something on the server, type in **Search** under the tabs and tap Enter.

To go back up, use the back gesture. It clears the search first, then goes up one level, then back to **This Device**.

**What each server offers**

- **Jellyfin, Emby:** **Continue Watching**, **Next Up**, **Recently Added** and your libraries.
- **Plex:** **Continue Watching**, **Recently Added** and your libraries.
- **PeerTube:** **Trending**, **Recently Added**, **On This Instance** and **Most Viewed**.
- **Media Servers (UPnP/DLNA):** The server's own folders.

Jellyfin, Emby and Plex keep your place. If you stop a video there, you can carry on from the same place on the server or on another device. Subtitles the server has are in the subtitles button's list ([learn how](/videos/use-subtitles-and-audio-tracks)).

With a Bluetooth headset, the next and previous buttons go to the next or previous episode.

Videos shows the tabs it had last time at once, then brings them up to date. It looks for your servers again each time you come back to it. Finding the media servers on your network takes a few seconds.

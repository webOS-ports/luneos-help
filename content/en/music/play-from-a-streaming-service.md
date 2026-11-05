---
{
 "id": "music/play-from-a-streaming-service",
 "title": "Play from a streaming service",
 "section": [],
 "order": 310.3,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.music/qml/views/StreamingView.qml:43",
  "/usr/palm/applications/org.webosports.app.music/qml/pages/StreamSearchPage.qml:82",
  "/usr/palm/applications/org.webosports.app.music/qml/pages/StreamSearchPage.qml:121",
  "/usr/palm/applications/org.webosports.app.music/qml/pages/SearchPage.qml:51",
  "/usr/palm/applications/org.webosports.app.music/qml/main.qml:1021",
  "luneos-synergy-connectors/music/_core/service/youtube.go:29",
  "org.webosports.app.music/qml/main.qml:954 (a provider with browse opens StreamLibraryPage.qml)"
 ],
 "review": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Music** > tap **Streaming**.
{if:unreleased}2. Tap a service. A Subsonic server opens on its albums and artists instead: tap **Search Subsonic** there ([learn how](/music/play-music-from-your-subsonic-server)).
{if:!unreleased}2. Tap a service.
3. Type what you are looking for. Results appear after a moment.
4. Do one of the following:
   - To play a song: Tap it. The songs in the results after it play next.
   - To queue it or save it: Tap and hold it, then tap **Play Next**, **Add to Queue**, **Add to Playlist…** or **Add to Favorites**.

You can also tap the Search button in Music. Below the songs on your device, you see a few results from each service. To see more, tap **More from** and the service's name.

Streamed songs work with [Up Next](/music/work-with-up-next) and your own playlists, and with the Sleep Timer. If you want to go back to a service, tap **Streaming**.

If you see **The search did not work**, the service could not be reached or your sign-in has ended.

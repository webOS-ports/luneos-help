---
{
 "id": "music/play-your-playlists-from-a-streaming-service",
 "title": "Play your playlists from a streaming service",
 "section": [],
 "order": 310.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.music/qml/views/PlaylistsView.qml:52",
  "/usr/palm/applications/org.webosports.app.music/qml/main.qml:878",
  "luneos-synergy-connectors/music/_core/service/playlists.go:10",
  "luneos-synergy-connectors/music/_core/service/playlists.go:29",
  "luneos-synergy-connectors/music/_core/service/deezer.go:161",
  "TouchPad /media/cryptofs/apps/usr/palm/applications/org.webosports.app.music/qml/views/PlaylistsView.qml has no service playlists (Oct 18 copy)",
  "luneos-synergy-connectors/music/_core/service/subsonic.go:317",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/service/radio.go:723"
 ],
 "review": []
}
---

{if:unreleased}This isn't in every copy of Music. It works with Spotify, Tidal, Qobuz and Deezer, and on newer LuneOS builds with Subsonic and Internet Radio. From Deezer you see your public playlists and your favorite tracks. Internet Radio's playlists are lists of stations ([learn how](/music/listen-to-internet-radio)).
{if:!unreleased}This isn't in every copy of Music. It works with Spotify, Tidal, Qobuz and Deezer. From Deezer you see your public playlists and your favorite tracks.

1. **[Open](/basics/open-an-application-in-the-launcher) Music** > tap **Playlists**.
2. Scroll past **YOUR PLAYLISTS**. Each service has its own heading, with the playlists you have there.
3. Tap a playlist, then tap a song, **Play** or **Shuffle**.

You can't change these playlists in Music. Change them with the service itself.

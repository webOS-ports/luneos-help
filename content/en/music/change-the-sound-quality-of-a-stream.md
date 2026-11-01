---
{
 "id": "music/change-the-sound-quality-of-a-stream",
 "title": "Change the sound quality of a stream",
 "section": [],
 "order": 310.4,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.music/qml/NowPlaying.qml:416",
  "/usr/palm/applications/org.webosports.app.music/qml/main.qml:1155",
  "luneos-synergy-connectors/music/_core/service/youtube.go:210",
  "/usr/palm/applications/org.webosports.app.music/qml/main.qml:1159",
  "TouchPad /media/cryptofs/apps/usr/palm/applications/org.webosports.app.music/qml/NowPlaying.qml has no formatBadge (Oct 18 copy)"
 ],
 "review": []
}
---

This isn't in every copy of Music, and not every service offers a choice. SoundCloud and YouTube Music do.

1. Start a streamed song and open Now Playing.
2. Under the seek bar, Music shows the format of the song. If it shows a small arrow, tap it.
3. Tap a format.

The song switches to that format where you are, and Music keeps your choice for that service's next songs. If a song doesn't have that format, Music uses the best one it has.

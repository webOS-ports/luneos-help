---
{
 "id": "music/stream-music",
 "title": "Stream music",
 "section": [],
 "order": 310.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.music/qml/js/Streaming.js:34",
  "/usr/palm/applications/org.webosports.app.music/qml/views/StreamingView.qml:56",
  "/usr/palm/applications/org.webosports.app.music/qml/main.qml:100",
  "luneos-synergy-connectors/music/_core/service/main.go:142",
  "luneos-synergy-connectors/music/_core/service/deezer.go:209",
  "luneos-synergy-connectors/music/_core/service/qobuzprovider.go:11",
  "luneos-synergy-connectors/music/_core/service/tidaldl.go:250",
  "luneos-synergy-connectors/music/_core/service/applemusic.go:39",
  "luneos-synergy-connectors/music/_core/librespot/README.md:9 (Spotify Premium mandatory)",
  "adb: GET 127.0.0.1:8730/providers on both devices (archive, deezer, jamendo, soundcloud, youtube; the MindPhone also qobuz, spotify, tidal)",
  "adb: ls /usr/palm/public/accounts on both devices (apple, archive, deezer, jamendo, qobuz, soundcloud, spotify, tidal)",
  "adb: ls /etc/spotify-webos, /media/internal/device.wvd (TouchPad: no client id; neither device: no device.wvd)"
 ],
 "review": []
}
---

Music can play from online services as well as from your device. You need an internet connection. Each service has its own terms and its own plans.

If **Streaming** is not one of Music's categories, the music streaming service isn't installed or isn't running on your device.

| Service | What you need | Add it in Accounts? |
| --- | --- | --- |
| YouTube Music | Nothing | No, it is always there |
| SoundCloud | Nothing | Yes, no sign-in |
| Jamendo | Nothing | Yes, no sign-in |
| Internet Archive | Nothing | Yes, no sign-in |
| Deezer | A Deezer account. Lossless sound needs a plan that includes it | Yes, sign in |
| Spotify | Spotify Premium | Yes, sign in |
| Tidal | A Tidal plan with lossless sound | Yes, sign in |
| Qobuz | A Qobuz plan with lossless sound | Yes, sign in |
| Apple Music | An Apple Music subscription and an extra file on your device | Yes, sign in |

To start, see [Add a streaming service](/music/add-a-streaming-service), then [Play from a streaming service](/music/play-from-a-streaming-service).

**Limits**

- Spotify can't be signed in to on every device. Your device needs a Spotify client ID, which not every LuneOS build includes.
- Spotify songs have no crossfade and no change of speed.
- Apple Music works only with a file called device.wvd in your device's internal storage. LuneOS doesn't include this file.
- Streamed songs need the network the whole time. They aren't saved on your device.
- Streamed songs have no **Song Info**, **Go to Album** or **Go to Artist** in their menu.
- A streamed song you mark as a favorite isn't listed in the **Favorites** playlist. That list shows only songs on your device.

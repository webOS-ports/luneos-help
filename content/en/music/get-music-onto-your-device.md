---
{
 "id": "music/get-music-onto-your-device",
 "title": "Get music onto your device",
 "section": [],
 "order": 310,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42554",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.music/appinfo.json:56",
  "/usr/palm/applications/org.webosports.app.music/qml/pages/PreferencesPage.qml:188",
  "/usr/palm/applications/org.webosports.app.music/qml/main.qml:100",
  "adb: luna-send -n 1 -f luna://com.palm.service.accounts/listAccountTemplates {} (org.webosports.app.music.*)",
  "/usr/palm/applications/org.webosports.app.music/qml/js/Streaming.js:34 (noAccount youtube)",
  "adb: GET 127.0.0.1:8730/providers (youtube always listed)"
 ]
}
---

Copy music files from your computer to your device ([learn how](/basics/copy-files-between-your-device-and-your-computer)). Music finds them in the device's internal storage by itself. Songs on memory cards and USB sticks are under **Folders**.

Music plays MP3, M4A, M4B, AAC, FLAC, Ogg, Opus, WAV, WMA, AIFF, APE and WavPack files.

To put playlists on your device too, see [Import a playlist file](/music/import-a-playlist-file).

You can also stream instead of copying. YouTube Music works without an account. For SoundCloud, Jamendo, the Internet Archive, Deezer, Spotify, Tidal, Qobuz and Apple Music, add the service in Accounts. See [Stream music](/music/stream-music).

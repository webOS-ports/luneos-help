---
{
 "id": "music/add-a-streaming-service",
 "title": "Add a streaming service",
 "section": [],
 "order": 310.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.musicauth/source/musicAuth.js:159",
  "/usr/palm/applications/org.webosports.app.musicauth/source/musicAuth.js:164",
  "/usr/palm/applications/org.webosports.app.musicauth/source/musicAuth.js:437",
  "/usr/palm/applications/org.webosports.app.musicauth/source/musicAuth.js:247",
  "/usr/palm/applications/org.webosports.app.musicauth/source/musicAuth.js:311",
  "/usr/palm/applications/org.webosports.app.musicauth/source/musicAuth.js:186",
  "/usr/palm/applications/org.webosports.app.musicauth/source/musicAuth.js:365",
  "/usr/palm/applications/org.webosports.app.music/qml/main.qml:509",
  "/usr/palm/applications/org.webosports.app.music/qml/views/StreamingView.qml:58",
  "luneos-synergy-connectors/music/_core/apps/org.webosports.app.musicauth/source/musicAuth.js:182 (subsonic)",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/_core/apps/org.webosports.app.musicauth/source/musicAuth.js:190 (radio)"
 ],
 "review": []
}
---

YouTube Music needs no account. It is already in Music's **Streaming** category.

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account**.
2. Tap the service.
3. Do what the service asks for:
   - **SoundCloud, Jamendo, Internet Archive:** Tap **Add SoundCloud**, **Add Jamendo** or **Add Internet Archive**.
{if:unreleased}   - **Internet Radio:** Tap **Add Internet Radio**. You can first enter a station list of your own ([learn how](/music/add-your-own-radio-stations)).
{if:unreleased}   - **Subsonic:** Enter your server's address, your username and password, and tap **Sign In** ([learn how](/music/play-music-from-your-subsonic-server)).
   - **Qobuz, Deezer:** Enter your email and password and tap **Sign In**.
   - **Tidal:** Sign in on the page that opens. You come back by yourself.
   - **Spotify:** Tap **Connect Spotify** and sign in on the page that opens. It can take you through a second sign-in page. You come back by yourself.
   - **Apple Music:** Sign in on the page that opens.
4. Go back to Music. The service is now in the **Streaming** category.

{if:unreleased}Subsonic and Internet Radio need a newer LuneOS build than some devices have.

If the service is not listed, tap **Try Again** in **Streaming**.

**If it doesn't work**

- **Deezer** sometimes refuses this kind of sign-in. A field for an **ARL** cookie then appears. The cookie comes from deezer.com in a desktop browser. Paste it and tap **Save ARL**.
- **Spotify** says "Spotify can't be signed in to on this device yet" when your device has no Spotify client ID.
- **Apple Music** asks you to put device.wvd in your device's internal storage, then tap **Try again**. LuneOS doesn't include this file.

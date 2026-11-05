# Media servers, radio and PiGallery2: help update (2026-11-05)

Scope: what Synergy (luneos-synergy-connectors), Music (org.webosports.app.music) and Videos
(org.webosports.app.videoplayer) gained since 2026-11-01, plus the Accounts side. Topics edited:
music, videos, photos, accounts. Nothing in tools/, static/, toc.json or other topics was touched.
No build was run and nothing was committed.

Device checks were read-only and on the MindPhone (adb MST0000022) only. adb also listed the TouchPad
(05DAY1XC8P) as attached. I was told it was not connected, so I did not query it.

## Where the code is, and what the MindPhone has

| Piece | Repo state read | On the MindPhone (opkg / files) | In the layer (meta-webos-ports, branch herrie/20261104) |
|---|---|---|---|
| Video connectors: Jellyfin, Emby, Plex, PeerTube, UPnP/DLNA, M3U + Free TV, Continue Watching and search across sources | luneos-synergy-connectors main | none: no org.webosports.video.* template, no org.webosports.service.videos | **no recipe installs them** (only an iptables rule for SSDP, 191d319) |
| Video connectors: Internet Archive, Mediathek, Owncast | only on branch herrie/music-video-sources (pushed, not merged) | none | no recipe |
| Subsonic (service + template + sign-in) | main | luneos-synergy-music 5b7468e3e8: no subsonic template, musicAuth.js has no subsonic | LSC_SRCREV 2e41ae2 has the service code, but `MUSIC_PROVIDERS` (luneos-synergy-music_git.bb:69) has **no subsonic**, so its template is never installed |
| Internet Radio, Jellyfin/Emby/Plex music in the music service | only on herrie/music-video-sources | none | not in LSC_SRCREV |
| PiGallery2 | main | none | no recipe |
| Music app: Subsonic browsing, covers | main (1bd230f) | app 9014b0c17e: no StreamLibraryPage.qml | recipe SRCREV 1bd230f has it |
| Music app: dashboard stays up while paused | main | **installed** (DashboardRule.js, main.qml:530) | yes |
| Videos app: servers, tabs, live, Continue Watching and search on the servers | master (0e74d45) | app 2a00b53e81: no BrowsePage.qml, SourceBar.qml, VideoSources.qml | recipe SRCREV 0e74d45 has it |
| Photos app: sub-albums | origin/master 20fb03b | no AlbumCell.qml, no parentId handling | recipe SRCREV 20fb03b has it |
| Photos service: sub-albums (parentAid) | only app-services-ports branch herrie/photos-sub-albums (29c14f7) | no | app-services SRCREV 456e2a87 does not have it |

So every new server feature is "verified-source". Each new page's first line says it "needs a newer
LuneOS build than some devices have". The evidence for that is the MindPhone's installed versions
against the repos (rows above). Today no LuneOS build would have the video connectors, Subsonic's
account type, Internet Radio or PiGallery2, because the layer doesn't package them (see Bugs).

## Pages added (10)

| Page | Status | Evidence (main) |
|---|---|---|
| videos/add-a-media-server-account | verified-source | videoAuth.js:38,44,50,56,92 (each kind's fields and button), :154/:316 (Plex by address), :337 (Plex code), :442 (error text); add-account.js:71 (no Video heading, so OTHER); MindPhone has no templates |
| videos/watch-videos-from-a-media-server | verified-source | SourceBar.qml:63,77; BrowsePage.qml:84 (back), :108 (one section opens its list), :305 (Search), :554 (seasons); main.qml:177 (asked again on return), :384 (headset next episode); jellyfin/plex/peertube provider sections |
| videos/watch-tv-channels-from-an-m3u-list | verified-source | videoAuth.js:68,123,128,132,249; m3u provider :152 (All countries), :361 (All Channels/groups); PlayerView.qml:78,962,979,1064 (LIVE, no seek, no speed) |
| videos/watch-films-from-the-internet-archive | verified-source (code on herrie/music-video-sources only) | videoAuth.js:62; archive provider :47 (collections), :336 |
| videos/watch-german-austrian-and-swiss-public-tv | verified-source (branch only) | videoAuth.js:76; mediathek provider :52, :88, :184 ("Only in its own country"); Online.js:112 (subtitle under a tile) |
| videos/watch-owncast-live-streams | verified-source (branch only) | videoAuth.js:83, :211 (STREAMS); owncast provider :256, :263, :268 |
| music/play-music-from-your-subsonic-server | verified-source | musicAuth.js:75,79,182; subsonic.go:317,539; StreamingView.qml:44; StreamLibraryPage.qml:82,95,132; main.qml:1188 (origin/main) |
| music/listen-to-internet-radio | verified-source (branch only) | radio template; musicAuth.js:190; radio.go:70,557,682,686,749; PlaylistsView.qml:53; Streaming.js:117 |
| music/add-your-own-radio-stations | needs-device-test (branch only) | musicAuth.js:92,287,294; radio.go:267,700,863 |
| photos/look-at-photos-on-a-pigallery2-server | verified-source | pigallery2Auth.js:22,25,35,71; cloud/pigallery2/README.md; Photos AlbumView.qml:47 (origin/master); add-account.js:77 |

Order values: videos 326.1 to 326.6 (between watch-a-video 326 and the controls page 327); music
310.31 to 310.33 (between play-from 310.3 and quality 310.4); photos 502.1 (after set-up, 502).
No new topics.

## Pages changed (10)

| Page | Status now | What changed |
|---|---|---|
| music/stream-music | needs-device-test (unchanged) | Subsonic and Internet Radio rows in the service table; the newer-build line; links to the new pages |
| music/add-a-streaming-service | needs-device-test (unchanged) | Internet Radio and Subsonic sign-in steps; the newer-build line |
| music/play-from-a-streaming-service | needs-device-test (unchanged) | A Subsonic server opens on its library, not a search (main.qml:954 on origin/main) |
| music/play-your-playlists-from-a-streaming-service | needs-device-test (unchanged) | Subsonic and Internet Radio also give playlists |
| music/listen-to-music | verified-device (kept) | The dashboard stays while paused, a tap opens Now Playing, a swipe pauses, closing the card on paused music ends Music. All of it is in the MindPhone's installed files (DashboardRule.js:31, main.qml:530,539,562, Dashboard.qml:131) |
| videos/continue-watching-a-video | verified-device to **verified-source** | Server videos (Jellyfin, Emby, Plex) in the same list, last watched first, eight at most; their hold menu; not shown in the grid layout |
| videos/watch-a-video | verified-device to **verified-source** | The search also asks the servers ("On <server>"); link to media servers |
| photos/set-up-an-online-pictures-or-videos-account-on-your-device | verified-device to **verified-source** | One sentence and a link for PiGallery2 |
| accounts/what-kinds-of-accounts-can-i-add | verified-device to **verified-source** | "On newer LuneOS builds" list: Subsonic, Internet Radio (MUSIC); PiGallery2 (CLOUD & PHOTOS); the nine video kinds (OTHER) |
| accounts/how-your-accounts-work-together | verified-device to **verified-source** | A Videos bullet |

These pages went down to verified-source because they now hold sentences no device can show yet. Their
older claims and evidence are unchanged.

## Needs device test (once a build packages them)

1. **Accounts > Add an Account**: the video kinds are under **OTHER** with no subtitle line. Two
   "Internet Archive" entries appear (MUSIC and OTHER). Subsonic and Internet Radio are under MUSIC, PiGallery2
   under CLOUD & PHOTOS with "Photos".
2. **Jellyfin/Emby**: enter the address, user and password, then **Sign In**. Videos shows a tab with the account's
   icon and the server name. Then check **Continue Watching**, **Next Up**, **Recently Added** and the libraries;
   a series' season pills and episodes; a stop part way showing up in Continue Watching on the
   library page and on the server's web app.
3. **Plex**: tap **Get a Code**, enter it at plex.tv/link, and the screen should go on by itself. Check that a second
   server or a shared one gets its own tab. Check **Enter a server address instead** with a
   no-auth server.
4. **PeerTube**: pick an instance from the list and check the sections. **UPnP/DLNA**: tap **Add**; tabs
   should appear after a few seconds (SSDP; iptables rule 191d319).
5. **Search**: in a server's tab, type and press Enter. In the library's **Search**, results should show under
   "On <server>" after half a second.
6. **M3U**: the Free TV list of the device's country is picked first. Check **All countries**, an own IPTV
   address with a name, and a list with groups (All Channels + groups). A channel shows **● LIVE**,
   with no seek bar, the jump buttons off and speed off.
7. **Internet Archive / Mediathek / Owncast**: tap **Add**, then the tab and its rows. Check a Mediathek item
   marked "Only in its own country" from outside DE/AT/CH. Check an Owncast single server that is
   offline ("Not Live Right Now").
8. **Continue Watching on a tablet**: on the TouchPad (1024x768) the library is the wide grid and
   LibraryPage.qml:144 shows no Continue Watching. Confirm, then decide whether the app or the page
   is right.
9. **Subsonic**: **Streaming** > **Subsonic** opens on **Search Subsonic**, **NEWEST ALBUMS** and **ARTISTS**. Check an artist's
   albums then songs, an album's hold menu with **Go to Artist**, and the server's playlists under Playlists.
10. **Internet Radio**: tap **Add Internet Radio**. **Playlists** should show the INTERNET RADIO heading with Most played,
    Most liked, Popular in <CC> and the ten genres. A station should play with no length (check how Now
    Playing shows a zero-length track). Check search under **Streaming** > **Internet Radio**.
11. **Own station list**: enter an M3U/PLS address at sign-in. The list should be at the top of INTERNET RADIO,
    one playlist per group. Check that a bad address shows the service's error. Check whether the account
    can be opened again to add a second list, and what removing the account does to the kept
    lists.
12. **PiGallery2**: tap **Connect** with and without a user and password, then **Sync Now**. Check whether sub-albums show
    (they need the photos service from app-services-ports herrie/photos-sub-albums). A HEIC should come
    over as a thumbnail.
13. **Music dashboard** (already installed on the MindPhone): pause with the card closed; the
    dashboard stays with Play. Tap it to open Now Playing. Close the card while paused; Music ends.

## Features found but not documented, and why

- **Jellyfin, Emby and Plex music in Music** (the music service reads the Videos sign-in,
  fb2471a, branch only). On Music's main, `Streaming.signedIn()` (js/Streaming.js:117) keeps only
  providers with an account `org.webosports.app.music.<id>`, so these never show: see Bugs. The
  app fix (7949753) is only on local, unpushed branches herrie/music-media-servers and
  herrie/music-service-icons.
- **Music's Radio tab, Home, favourite stations, "More stations"** (edc9ee7, 234ea59, 74f0849,
  0d23095, 001443f): local unpushed branch herrie/music-service-icons, not main. When it lands, the
  two radio pages need rewriting (radio moves out of Playlists into its own tab).
- **Radio Browser lists a page at a time** (96e1edf): the Music app on main asks only for the first
  page (100 stations). No user step until the app side lands.
- **Spotify self-heal / held output / rate limit** (873e919, 83a15cc, 744b351, a15e31b): internal, with nothing
  for the user to do.
- **Videos tab-bar styling, flick speeds, captions on two lines**: look only, with no task to describe.
- **Server subtitles** (by the server's names, off unless the server marks a default) and **"this
  device's place wins"** over the server's: one line in watch-videos-from-a-media-server. I did not
  add them to use-subtitles-and-audio-tracks, because that page is device-verified and none of this is on a device.
- **Immich, PhotoPrism, SmugMug, WebDAV** connectors and recipes exist (before 11-01). They are not in
  packagegroup-luneos-extended and not on the MindPhone, and are out of this task's date range.

## Bugs and oddities

1. **Nothing packages the new connectors.** meta-webos-ports has no recipe for
   org.webosports.service.videos, org.webosports.app.videoauth or any org.webosports.video.*
   template, and none for PiGallery2. luneos-synergy-music_git.bb:69 `MUSIC_PROVIDERS` lacks
   `subsonic` (and `radio`), so their account types are never installed. The Music app pin
   (1bd230f), with Subsonic browsing, and the Videos app pin (0e74d45), with the server tabs, ship UI
   that no account can reach.
2. **Music on main hides Jellyfin/Emby/Plex** even once the service offers them (Streaming.js:117
   filter on `org.webosports.app.music.` templates). The fix exists only on unpushed local branches.
3. **Video accounts land under OTHER** in Add an Account: their capability is "Video", which is not in
   add-account.js `categoryOrder`/`capLabels` (enyo-1.0 and enyo-1.0-ports). The row has no
   subtitle. Two accounts are named "Internet Archive" (music and video).
4. **Continue Watching is not shown in the wide grid layout** (LibraryPage.qml:144 `!wide`, the same on
   the installed MindPhone copy at line 68). The old continue-watching page was marked verified-device
   on both devices and said otherwise. I have now worded it as "not shown in the grid".
5. **Radio station lists can't be removed**: no code writes `radio-lists` except
   handleRadioAuthLists (which only adds), and nothing clears it when the account is deleted. That
   is the same pattern as the kept music sign-ins on remove-a-streaming-service.
6. **Photos sub-albums are half-way**: the app pin has them, the photos service pin doesn't
   (parentAid only on app-services-ports herrie/photos-sub-albums). With PiGallery2, every folder is
   a top-level album until that lands.
7. Subsonic's sign-in needs a non-empty password (musicAuth.js validateInput). Jellyfin/Emby's
   allows an empty one ("Password (may be empty)").
8. Which tree the line numbers come from: connectors from the working checkout
   herrie/music-video-sources, which holds main plus the radio/media-server-music/Archive/Mediathek/
   Owncast commits. On main, videoAuth.js is 47 lines shorter, so its line numbers there are lower.
   Videos is from herrie/videos-continue-search, whose qml/ is identical to origin/master. Music
   numbers are re-checked against origin/main. During this session the Music clone
   (~/Documents/GitHub/org.webosports.app.music) was switched from herrie/subsonic-browse to
   herrie/music-service-icons. I did not make that switch, and I changed no repo other than luneos-help.

## Cross-group links

None outside music, videos, photos and accounts. Links into /basics/ are to pages that already
existed (open-an-application-in-the-launcher, open-the-application-menu,
copy-files-between-your-device-and-your-computer). All links were checked against content/en.

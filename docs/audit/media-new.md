# Audit: media group, replacements and new features

Date: 2026-11-01. Generator: ~/claude-scratch/help/audit/media-new/ (lib.py resolves every evidence line from a needle in the device copy or repo, and stops on a miss). Originals of changed pages: media-new/before/.

Devices were read only. Beyond file reads and luna-send queries, three read-only checks: GET 127.0.0.1:8730/providers on both devices, `luna-send -a com.palm.app.accounts .../listAccounts` (templateIds only printed), and listing the names of files in /media/cryptofs/spotify-webos (contents not read). No streaming track was searched or played.

## Streaming per device

| | MindPhone (MindPhone) | TouchPad (TouchPad) |
| --- | --- | --- |
| Live Music | /usr/palm/applications, current (matches repo but Player.qml, SpotifyEngine.qml) | /media/cryptofs copy of Oct 18, older than its own /usr copy (getAppInfo folderPath) |
| Streaming category, per-service search, search sections | yes | yes |
| Quality badge, service playlists, online lyrics, About the artist | yes | no |
| Daemon running | yes | yes |
| Daemon lists | archive, deezer, jamendo, qobuz, soundcloud, spotify, tidal, youtube | archive, deezer, jamendo, soundcloud, youtube |
| Music accounts | archive, deezer, jamendo, qobuz, soundcloud, spotify, tidal | none |
| Account templates | all eight, apple included | all eight, apple included |
| Spotify client id | /etc/spotify-webos has one | none found: sign-in gives the 412 message |
| librespot | /usr/bin/librespot | /usr/bin/librespot |
| device.wvd (Apple Music) | absent | absent |

The prior audit said lyrics lookup and artist lookup are missing on the tablet copy; true of the cryptofs copy only. Pages say "isn't in every copy of Music".

## New pages

| Page | Status | Evidence |
| --- | --- | --- |
| music/stream-music | needs-device-test | org.webosports.app.music/qml/js/Streaming.js:34; org.webosports.app.music/qml/views/StreamingView.qml:56; org.webosports.app.music/qml/main.qml:100; +9 more |
| music/add-a-streaming-service | needs-device-test | org.webosports.app.musicauth/source/musicAuth.js:159; org.webosports.app.musicauth/source/musicAuth.js:164; org.webosports.app.musicauth/source/musicAuth.js:437; +6 more |
| music/play-from-a-streaming-service | needs-device-test | org.webosports.app.music/qml/views/StreamingView.qml:43; org.webosports.app.music/qml/pages/StreamSearchPage.qml:82; org.webosports.app.music/qml/pages/StreamSearchPage.qml:121; +3 more |
| music/change-the-sound-quality-of-a-stream | needs-device-test | org.webosports.app.music/qml/NowPlaying.qml:416; org.webosports.app.music/qml/main.qml:1155; luneos-synergy-connectors/music/_core/service/youtube.go:210; +2 more |
| music/play-your-playlists-from-a-streaming-service | needs-device-test | org.webosports.app.music/qml/views/PlaylistsView.qml:52; org.webosports.app.music/qml/main.qml:878; luneos-synergy-connectors/music/_core/service/playlists.go:10; +3 more |
| music/remove-a-streaming-service | needs-device-test | org.webosports.app.music/qml/StreamingStore.qml:31; org.webosports.app.music/qml/js/Streaming.js:122; luneos-synergy-connectors/music/_core/service/secrets.go:118; +1 more |
| music/use-the-sleep-timer | verified-device | org.webosports.app.music/qml/main.qml:697; org.webosports.app.music/qml/main.qml:1135; org.webosports.app.music/qml/main.qml:1141; +4 more |
| music/change-the-playback-speed | verified-device | org.webosports.app.music/qml/main.qml:1169; org.webosports.app.music/qml/NowPlaying.qml:586; org.webosports.app.music/qml/SpotifyEngine.qml:59 |
| music/mark-songs-as-favorites | verified-device | org.webosports.app.music/qml/NowPlaying.qml:397; org.webosports.app.music/qml/main.qml:1028; org.webosports.app.music/qml/js/Library.js:451; +1 more |
| music/read-the-lyrics-of-a-song | verified-device | org.webosports.app.music/qml/NowPlaying.qml:560; org.webosports.app.music/qml/LyricsView.qml:26; org.webosports.app.music/qml/pages/PreferencesPage.qml:122; +2 more |
| music/read-about-the-artist | verified-device | org.webosports.app.music/qml/NowPlaying.qml:571; org.webosports.app.music/qml/ArtistView.qml:195; org.webosports.app.music/qml/pages/PreferencesPage.qml:139; +2 more |
| music/work-with-up-next | verified-device | org.webosports.app.music/qml/main.qml:693; org.webosports.app.music/qml/NowPlaying.qml:607; org.webosports.app.music/qml/pages/QueuePage.qml:91; +2 more |
| music/change-music-preferences | verified-device | org.webosports.app.music/qml/pages/PreferencesPage.qml:56; org.webosports.app.music/qml/pages/PreferencesPage.qml:63; org.webosports.app.music/qml/pages/PreferencesPage.qml:70; +5 more |
| music/see-song-information | verified-device | org.webosports.app.music/qml/main.qml:1036; org.webosports.app.music/qml/pages/SongInfoPage.qml:31; org.webosports.app.music/qml/pages/SongInfoPage.qml:101 |
| music/use-automatic-playlists | verified-device | org.webosports.app.music/qml/views/PlaylistsView.qml:38; org.webosports.app.music/qml/js/Library.js:441; org.webosports.app.music/qml/js/Library.js:472; +1 more |
| music/import-a-playlist-file | verified-device | org.webosports.app.music/qml/main.qml:1069; org.webosports.app.music/qml/main.qml:1075; org.webosports.app.music/qml/views/FoldersView.qml:120; +2 more |
| music/export-a-playlist | verified-device | org.webosports.app.music/qml/main.qml:1090; org.webosports.app.music/qml/main.qml:1091; org.webosports.app.music/qml/main.qml:64; +1 more |
| videos/use-subtitles-and-audio-tracks | verified-device | org.webosports.app.videoplayer/qml/PlayerView.qml:605; org.webosports.app.videoplayer/qml/PlayerView.qml:595; org.webosports.app.videoplayer/qml/PlayerView.qml:601; +3 more |
| videos/lock-the-screen-while-watching-a-video | verified-device | org.webosports.app.videoplayer/qml/PlayerView.qml:817; org.webosports.app.videoplayer/qml/PlayerView.qml:1076; org.webosports.app.videoplayer/qml/PlayerView.qml:79; +1 more |
| videos/continue-watching-a-video | verified-device | org.webosports.app.videoplayer/qml/LibraryPage.qml:354; org.webosports.app.videoplayer/qml/LibraryPage.qml:350; org.webosports.app.videoplayer/qml/PlayerView.qml:851; +1 more |
| videos/change-how-videos-are-listed-and-shown | verified-device | org.webosports.app.videoplayer/qml/main.qml:330; org.webosports.app.videoplayer/qml/main.qml:348; org.webosports.app.videoplayer/qml/main.qml:354; +2 more |
| pdf/find-text-in-a-file | verified-device | org.webosports.app.pdf/qml/ViewerPage.qml:254; org.webosports.app.pdf/qml/components/SearchBar.qml:76; TouchPad /media/cryptofs/appsorg.webosports.app.pdf/qml/ViewerPage.qml:237 |
| pdf/copy-text-from-a-file | verified-device | org.webosports.app.pdf/qml/ViewerPage.qml:308; org.webosports.app.pdf/qml/ViewerPage.qml:499; org.webosports.app.pdf/qml/ViewerPage.qml:561; +1 more |
| pdf/open-a-protected-file | verified-device | org.webosports.app.pdf/qml/components/PasswordDialog.qml:57; org.webosports.app.pdf/qml/components/PasswordDialog.qml:56; org.webosports.app.pdf/qml/components/PasswordDialog.qml:94; +1 more |
| pdf/see-document-info | verified-device | org.webosports.app.pdf/qml/ViewerPage.qml:261; org.webosports.app.pdf/qml/DocumentInfoPage.qml:53; org.webosports.app.pdf/qml/DocumentInfoPage.qml:90 |
| pdf/use-night-mode-and-rotate-pages | verified-device | org.webosports.app.pdf/qml/ViewerPage.qml:257; org.webosports.app.pdf/qml/ViewerPage.qml:255; org.webosports.app.pdf/qml/ViewerPage.qml:256; +1 more |
| maps/use-voice-guidance | needs-device-test | org.webosports.app.maps/source/data/Pullout.js:699; org.webosports.app.maps/source/views/main.js:1601; org.webosports.app.maps/source/data/Guidance.js:176; +3 more |
| maps/add-stops-to-a-route | verified-device | org.webosports.app.maps/source/views/main.js:1524; org.webosports.app.maps/source/data/Pullout.js:683; org.webosports.app.maps/source/data/Pullout.js:684; +1 more |
| maps/change-maps-settings | verified-device | org.webosports.app.maps/source/data/Pullout.js:157; org.webosports.app.maps/source/data/Pullout.js:169; org.webosports.app.maps/source/data/Pullout.js:182; +4 more |
| maps/drop-a-pin-on-the-map | verified-device | org.webosports.app.maps/source/views/main.js:1009; org.webosports.app.maps/source/views/main.js:1015; org.webosports.app.maps/build/app.js contains 'Dropped pin #' |
| location-services/see-your-gps-status | verified-device | TouchPad org.webosports.app.settings.location/qml/General/LocationPage.qml:187; TouchPad org.webosports.app.settings.location/qml/General/LocationPage.qml:194; TouchPad org.webosports.app.settings.location/qml/General/LocationPage.qml:238; +1 more |
| location-services/see-which-applications-asked-for-your-location | verified-device | TouchPad org.webosports.app.settings.location/qml/General/LocationPage.qml:332; TouchPad org.webosports.app.settings.location/qml/General/LocationPage.qml:339; TouchPad org.webosports.app.settings.location/qml/General/LocationPage.qml:347; +1 more |
| web/save-and-manage-passwords | needs-device-test | org.webosports.app.atlas/source/Browser.js:390; org.webosports.app.atlas/source/Browser.js:363; org.webosports.app.atlas/source/LoginPicker.js:18; +3 more |
| web/import-or-export-passwords | needs-device-test | org.webosports.app.atlas/source/LoginExporter.js:11; org.webosports.app.atlas/source/LoginImporter.js:14; org.webosports.app.atlas/source/LoginImporter.js:3; +4 more |
| web/use-reading-mode | verified-device | org.webosports.app.atlas/source/BrowserApp.js:170; org.webosports.app.atlas/source/ReaderView.js:34; org.webosports.app.atlas/source/ReaderView.js:42; +1 more |
| web/translate-a-web-page | needs-device-test | org.webosports.app.atlas/source/Preferences.js:49; org.webosports.app.atlas/source/ActionBar.js:63; org.webosports.app.atlas/source/phone/PhoneActionBar.js:56; +1 more |
| web/browse-in-a-private-card | needs-device-test | org.webosports.app.atlas/source/BrowserApp.js:171; org.webosports.app.atlas/source/BrowserApp.js:767; org.webosports.app.atlas/source/BrowserApp.js:884 |
| web/restart-the-browser-engine | needs-device-test | org.webosports.app.atlas/source/BrowserApp.js:176; org.webosports.app.atlas/source/BrowserApp.js:799; org.webosports.app.atlas/source/Browser.js:1070 |
| web/find-text-on-a-page | verified-device | org.webosports.app.atlas/source/BrowserApp.js:169; org.webosports.app.atlas/source/FindBar.js:31; org.webosports.app.atlas/source/FindBar.js:58 |
| camera/use-the-camera | verified-device | TouchPad org.webosports.app.camera/qml/CaptureOverlay.qml:294; TouchPad org.webosports.app.camera/qml/CaptureOverlay.qml:272; TouchPad org.webosports.app.camera/qml/main.qml:74; +1 more |
| camera/switch-cameras | verified-device | TouchPad org.webosports.app.camera/qml/CaptureOverlay.qml:375; TouchPad org.webosports.app.camera/qml/CaptureOverlay.qml:398; TouchPad org.webosports.app.camera/qml/prefs/PreferencesPage.qml:58 |
| camera/change-camera-preferences | verified-device | TouchPad org.webosports.app.camera/qml/prefs/PreferencesPage.qml:41; TouchPad org.webosports.app.camera/qml/prefs/PreferencesPage.qml:65; TouchPad org.webosports.app.camera/qml/prefs/PreferencesPage.qml:73; +6 more |
| camera/read-a-qr-code-or-barcode | verified-device | TouchPad org.webosports.app.camera/qml/prefs/PreferencesPage.qml:97; TouchPad org.webosports.app.camera/qml/PreferencesModel.qml:55; TouchPad org.webosports.app.camera/qml/components/CodeBanner.qml:97; +2 more |
| camera/tag-your-photos-with-a-location | verified-device | TouchPad org.webosports.app.camera/qml/prefs/PreferencesPage.qml:87; TouchPad org.webosports.app.camera/qml/CaptureOverlay.qml:447; TouchPad org.webosports.app.settings.location/qml/General/LocationPage.qml:361 |
| documents/open-a-document | verified-device | org.webosports.app.documents/source/views/LibraryView.js:33; org.webosports.app.documents/source/views/LibraryView.js:118; org.webosports.app.documents/source/App.js:26; +3 more |
| documents/read-a-document | verified-device | org.webosports.app.documents/source/views/ViewerView.js:35; org.webosports.app.documents/source/views/ViewerView.js:57; org.webosports.app.documents/source/App.js:21; +5 more |
| documents/edit-a-workbook | verified-device | org.webosports.app.documents/source/views/SheetView.js:32; org.webosports.app.documents/source/views/ViewerView.js:31; org.webosports.app.documents/source/views/SheetView.js:342; +2 more |
| documents/edit-a-document | verified-device | org.webosports.app.documents/source/views/ViewerView.js:63; org.webosports.app.documents/source/views/ViewerView.js:46; org.webosports.app.documents/source/views/ViewerView.js:31; +1 more |
| documents/open-a-document-from-an-online-account | needs-device-test | org.webosports.app.documents/source/views/LibraryView.js:37; org.webosports.app.documents/source/views/CloudView.js:230; org.webosports.app.documents/source/views/CloudView.js:271; +3 more |
| files/browse-your-files | verified-device | com.palm.stark.files/source/App.js:46; com.palm.stark.files/source/App.js:424; com.palm.stark.files/source/App.js:27; +5 more |
| files/copy-move-rename-or-delete-files | verified-device | com.palm.stark.files/source/App.js:50; com.palm.stark.files/source/App.js:56; com.palm.stark.files/source/App.js:57; +6 more |
| files/extract-or-compress-an-archive | verified-device | com.palm.stark.files/source/App.js:91; com.palm.stark.files/source/App.js:92; com.palm.stark.files/source/App.js:83; +2 more |
| files/open-a-network-folder | needs-device-test | com.palm.stark.files/source/App.js:23; com.palm.stark.files/source/App.js:25; com.palm.stark.files/source/Dialogs.js:68; +2 more |
| files/share-your-files-over-ftp | needs-device-test | com.palm.stark.files/source/App.js:102; com.palm.stark.files/source/Dialogs.js:325; com.palm.stark.files/source/Dialogs.js:345; +1 more |
| files/change-system-files | verified-device | com.palm.stark.files/source/App.js:104; com.palm.stark.files/source/App.js:1215 |
| sound-recorder/record-sound | verified-device | org.webosports.app.soundrecorder/qml/RecordingsPage.qml:302; org.webosports.app.soundrecorder/qml/RecordingsPage.qml:321; org.webosports.app.soundrecorder/qml/RecordingDashboard.qml:111; +4 more |
| sound-recorder/play-a-recording | verified-device | org.webosports.app.soundrecorder/qml/RecordingsPage.qml:43; org.webosports.app.soundrecorder/qml/components/RecordingRow.qml:249; org.webosports.app.soundrecorder/qml/components/RecordingRow.qml:260; +1 more |
| sound-recorder/rename-send-or-delete-a-recording | verified-device | org.webosports.app.soundrecorder/qml/RecordingsPage.qml:334; org.webosports.app.soundrecorder/qml/RecordingsPage.qml:354; org.webosports.app.soundrecorder/qml/RecordingsPage.qml:365; +2 more |
| sound-recorder/change-recording-preferences | verified-device | org.webosports.app.soundrecorder/qml/PreferencesPage.qml:65; org.webosports.app.soundrecorder/qml/PreferencesPage.qml:73; org.webosports.app.soundrecorder/qml/PreferencesPage.qml:84; +4 more |

## Pages changed for replacements

| Page | Change |
| --- | --- |
| music/get-music-onto-your-device | HP Play replacement: USB/MTP copy plus streaming. Corrected: Streaming does not "appear" after adding an account (YouTube Music is there with none); added YouTube Music and Apple Music, which were missing. Link to playlist import. |
| music/listen-to-music | Adds the Streaming category. |
| music/switch-the-now-playing-display | Adds About the artist and how to go back. |
| music/search-songs-artists-albums-genres-or-playlists | Adds streaming results. |
| videos/use-video-playback-controls | Links to the new subtitle and lock pages. |
| pdf/open-a-file | "Files" corrected to LuneOS Explorer, the app's real title. |
| photos/take-a-picture | Links into the new camera topic. Camera steps stay in photos/ and videos/: nothing moved, camera/use-the-camera links to them. |

Replacements confirmed: HP Play -> USB/MTP and streaming. Adobe Reader -> PDF Viewer (already done). Quickoffice -> Documents: no imported Quickoffice page exists, the new documents topic fills the gap. music/search-for-related-songs-or-content -> partly, music/read-about-the-artist.

## Replacements confirmed absent (left deleted)

| Article | Why |
| --- | --- |
| pdf/print-a-pdf-file, web/print-a-web-page | No printing in either app. |
| pdf/save-a-file-with-a-new-name | PDF Viewer is read-only. LuneOS Explorer can rename a file, but that is not the old task. |
| videos/edit-videos-you-recorded | No trim anywhere. |
| maps/work-with-locations-you-viewed-recently | Recent still commented out. |
| web/add-a-web-search-engine, web/use-flash-content | Nothing replaces them. |
| photos/add-a-picture-to-a-contact, photos/use-photos-and-videos-for-the-first-time | No change in Photos & Videos. Contacts belongs to another group. |

## Found but not documented

- Web, Autofill: the menu item and list store values in org.webosports.autofill:1, but no code in Atlas, webos-keyboard or luneos-components reads them, so nothing fills a form. Preferences' Clear Autofill Information has an empty handler. A page would promise something that does not happen.
- Web, camera and microphone prompts from sites: ChromiumWebView.js:384-388 says the stock webruntime never emits the request and denies without a prompt. Location for sites is covered by location-services.
- Web, Help menu item: launches http://help.palm.com/web/index.html (BrowserApp.js helpClick). Dead link, an app bug.
- Music daemon /download (lossless download) and /provider/*/resolveVideo: no UI in Music.
- Music, Spotify's and others' sign-in data, backup through keymanager: Backup group's area.
- Documents, Edit with LibreOffice and .doc/.ppt/.rtf: need org.webosports.service.office, on neither device. One line in documents/open-a-document.
- LuneOS Explorer, Google Drive and Nextcloud in the folder tree: code exists, not confirmed on LuneOS without a signed-in account. Its system-changes warning names webOS and webOS Doctor; left out of the page.
- Maps, Offline map tiles and High DPI tiles: rows are hidden or engine-specific.
- Exhibition Now Playing: group system.

## Possible app bugs for the owner

1. Streamed favorites never show in Favorites: smartPlaylist runs over library.lib.songs only (main.qml:829). Documented as a limit.
2. Removing a streaming account does not sign out: removeSecret runs only after a failed sign-in, so tokens stay in /media/cryptofs/spotify-webos and keymanager. StreamingStore's comment says so too. Documented in music/remove-a-streaming-service.
3. Streaming's empty-state text is unreachable while the daemon runs: YouTube Music is always listed.
4. Streaming's text offers Apple Music, which cannot sign in without a user-supplied device.wvd. The page states the need and does not say how to get one.
5. TouchPad runs a Music, PDF Viewer and Videos copy older than the image's own.

## Needs device test

Accounts exist on the MindPhone, so 1 to 6 can be tried there.

1. music/stream-music: is a free Deezer account enough for full tracks? (Code comment says yes.) Does Deezer give FLAC or MP3 on free? Confirm Tidal and Qobuz refuse a plan without lossless.
2. music/add-a-streaming-service: add each service, on a device without the account. Confirm button labels, that Spotify's second page appears, Tidal's return, and the Deezer ARL fallback.
3. music/play-from-a-streaming-service: search each service, play, seek; hold a result for its menu; More from <service> in Search. Check that The search did not work shows when offline.
4. music/change-the-sound-quality-of-a-stream: SoundCloud and YouTube Music: does the badge show the arrow, does the switch keep the position?
5. music/play-your-playlists-from-a-streaming-service: check Spotify, Tidal, Qobuz, Deezer. The installed daemon's strings were checked for the route only. README says Spotify only, connectors main says all four.
6. music/remove-a-streaming-service: remove an account, check that it leaves Streaming and Search at once, re-add, see whether sign-in is skipped. Streamed tracks in your playlists after removal were not traced.
7. music/stream-music, TouchPad: add Spotify, expect the client id message.
8. maps/use-voice-guidance: drive a route with a fix; does a voice speak on LuneOS (speechSynthesis)?
9. web/save-and-manage-passwords: sign in to a site, Save, return, fill; phone drawer route (see web items in media.md).
10. web/import-or-export-passwords: which button is which: both are icons with no labels. Round trip a CSV.
11. web/translate-a-web-page: the button appears in the address bar on both layouts.
12. web/browse-in-a-private-card: cookies and cache really gone after closing.
13. web/restart-the-browser-engine: tap it, see the engine return.
14. documents/open-a-document-from-an-online-account: open and Save a Copy on a cloud account.
15. files/open-a-network-folder and files/share-your-files-over-ftp: connect to a server; check that the address is shown when sharing.

## New topics for toc.json

| id | title | Home group | Icon |
| --- | --- | --- | --- |
| camera | Camera | Media | ~/Documents/GitHub/org.webosports.app.camera/icon.png |
| documents | Documents | Documents | ~/Documents/GitHub/org.webosports.app.documents/icon.png |
| files | LuneOS Explorer | Documents | ~/Documents/GitHub/topaz-explorer-webos/app/images/icon.png |
| sound-recorder | Sound Recorder | Media | ~/Documents/GitHub/org.webosports.app.soundrecorder/icon.png |

All of these match the apps installed (com.palm.stark.files is titled LuneOS Explorer in its appinfo.json on both devices). Camera pages carry requires ["camera"]; camera/use-the-camera is the topic's entry page.

## Links into other groups

- /accounts/use-the-accounts-application-to-set-up-an-online-account: documents/open-a-document-from-an-online-account
- /accounts/use-the-accounts-application-to-edit-or-delete-an-online-account: music/remove-a-streaming-service
- /basics/copy-files-between-your-device-and-your-computer: music/import-a-playlist-file, documents/open-a-document, web/import-or-export-passwords
- /basics/open-an-application-in-the-launcher and /basics/open-the-application-menu: most new pages

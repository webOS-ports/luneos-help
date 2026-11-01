# Audit: media group

Topics: photos, music, videos, pdf, maps, web, location-services. Date: 2026-11-01.

Devices read over adb: TouchPad (TouchPad), MindPhone (MindPhone). App copies pulled to device-media/ and every evidence needle was checked by media_apply.py in both devices' live copies (camera: TouchPad only, MindPhone has none).
On the TouchPad the live Music, PDF Viewer and Videos are the /media/cryptofs copies (getAppInfo folderPath), which differ from the /usr copies. Evidence lines are for the /usr path on the MindPhone. The tablet copy of Music lacks the lyrics and artist lookups, so those are not documented.
Legacy icon images were removed from every rewritten page: buttons are named in words because the apps are new and the old art was not compared one by one.

| Article | Status | What changed | Evidence |
| --- | --- | --- | --- |
| photos/add-a-comment-to-a-picture-or-video-in-an-online-account | needs-device-test | Comment send is Enter, no send icon. No account with comments was on the devices. | org.webosports.app.photos/qml/PictureView.qml:283; org.webosports.app.photos/qml/PictureView.qml:371 |
| photos/copy-pictures-or-videos-to-an-album | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/AlbumView.qml:246; org.webosports.app.photos/qml/AlbumView.qml:297; org.webosports.app.photos/qml/main.qml:216; +3 more |
| photos/create-an-album | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/LibraryPanel.qml:173; org.webosports.app.photos/qml/main.qml:342; org.webosports.app.photos/qml/main.qml:231; +1 more |
| photos/delete-pictures-or-videos | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/PictureView.qml:297; org.webosports.app.photos/qml/AlbumView.qml:304; org.webosports.app.photos/qml/main.qml:257; +1 more |
| photos/delete-an-album | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/AlbumView.qml:221; org.webosports.app.photos/qml/main.qml:243 |
| photos/delete-an-online-pictures-or-videos-account | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/main.qml:352; org.webosports.app.photos/qml/main.qml:353; adb: grep 'Remove Account' /usr/palm/frameworks/enyo/0.10/framework/lib/accounts |
| photos/look-at-pictures-in-a-slideshow | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/AlbumView.qml:280; org.webosports.app.photos/qml/PictureView.qml:266; org.webosports.app.photos/qml/LibraryGrid.qml:174; +3 more |
| photos/look-at-pictures | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/js/Library.js:118; org.webosports.app.photos/qml/PictureView.qml:190; org.webosports.app.photos/qml/PictureView.qml:235; +1 more |
| photos/organize-your-pictures-and-videos-into-albums | verified-device | The device library's name comes from deviceName, default My Device; a device may report its own name. | org.webosports.app.photos/qml/LibraryPanel.qml:102; org.webosports.app.photos/qml/LibraryPanel.qml:112; org.webosports.app.photos/qml/main.qml:116; +2 more |
| photos/print-pictures | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/PictureView.qml:290; org.webosports.app.photos/qml/Printer.qml:50; org.webosports.app.photos/qml/Printer.qml:68; +1 more |
| photos/review-the-pictures-you-took | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.camera/qml/main.qml:273; org.webosports.app.camera/qml/main.qml:87; org.webosports.app.camera/qml/main.qml:74; +1 more |
| photos/save-a-picture-as-wallpaper | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/PictureView.qml:312; org.webosports.app.photos/qml/main.qml:286; org.webosports.app.photos/qml/main.qml:276 |
| photos/set-up-an-online-pictures-or-videos-account-on-your-device | verified-device | Sign-in screens differ per account type, so they are not spelled out here. | org.webosports.app.photos/qml/main.qml:352; org.webosports.app.photos/qml/main.qml:347; adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates {"capability":"PHOTO.UPLOAD"}; +1 more |
| photos/share-a-picture | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/PictureView.qml:276; org.webosports.app.photos/qml/main.qml:269 |
| photos/take-a-picture | verified-device | Space key shortcut removed: the camera has no key handling. Tap to focus needs a camera with focus control (droid cameras). | org.webosports.app.camera/qml/CaptureOverlay.qml:294; org.webosports.app.camera/qml/CaptureOverlay.qml:201; org.webosports.app.camera/qml/CaptureOverlay.qml:211; +3 more |
| photos/upload-a-picture-to-the-web | needs-device-test | Upload depends on an account; no cloud account was on the devices. | org.webosports.app.photos/qml/PictureView.qml:309; org.webosports.app.photos/qml/js/Library.js:430 |
| photos/use-video-playback-controls | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/VideoPane.qml:148; org.webosports.app.photos/qml/VideoPane.qml:162; org.webosports.app.photos/qml/VideoPane.qml:181; +1 more |
| photos/watch-a-video | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/AlbumView.qml:184; org.webosports.app.videoplayer/qml/PlayerView.qml:964 |
| photos/work-with-panels-in-photos-and-videos | verified-device | Old link to /basics/resize-panels removed: this panel does not resize. | org.webosports.app.photos/qml/main.qml:62; org.webosports.app.photos/qml/main.qml:465; org.webosports.app.photos/qml/LibraryPanel.qml:104 |
| videos/delete-a-video | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.videoplayer/qml/LibraryPage.qml:350; org.webosports.app.videoplayer/qml/LibraryPage.qml:354; org.webosports.app.photos/qml/PictureView.qml:297 |
| videos/record-a-video | verified-device | Removed stabilization, keyboard Space, and landscape step: none in the app. | org.webosports.app.camera/qml/CaptureOverlay.qml:294; org.webosports.app.camera/qml/CaptureOverlay.qml:325; org.webosports.app.camera/qml/CaptureOverlay.qml:212 |
| videos/upload-or-share-videos-you-recorded | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.photos/qml/PictureView.qml:276; org.webosports.app.photos/qml/main.qml:269; org.webosports.app.photos/qml/js/Library.js:430 |
| videos/use-video-playback-controls | verified-device | Removed the swipe to skip 30/10 seconds: PlayerView has no swipe handling. | org.webosports.app.videoplayer/qml/PlayerView.qml:971; org.webosports.app.videoplayer/qml/PlayerView.qml:993; org.webosports.app.videoplayer/qml/PlayerView.qml:957; +5 more |
| videos/watch-a-video | verified-device | Search field shows only with six or more videos (README). Not stated in the steps beyond the field's name. | org.webosports.app.videoplayer/qml/LibraryPage.qml:75; org.webosports.app.videoplayer/qml/LibraryPage.qml:220; org.webosports.app.videoplayer/qml/main.qml:330; +1 more |
| music/add-music-to-a-playlist | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/components/SongRow.qml:59; org.webosports.app.music/qml/components/AlbumTile.qml:81; org.webosports.app.music/qml/main.qml:1009; +2 more |
| music/change-order-of-items-in-the-playlist-view | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/components/SongRow.qml:42; org.webosports.app.music/qml/main.qml:862; org.webosports.app.music/qml/pages/QueuePage.qml:35 |
| music/create-a-playlist | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/views/PlaylistsView.qml:104; org.webosports.app.music/qml/views/PlaylistsView.qml:44; org.webosports.app.music/qml/main.qml:1109 |
| music/delete-a-playlist | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/main.qml:1095; org.webosports.app.music/qml/main.qml:1096; org.webosports.app.music/qml/views/PlaylistsView.qml:111 |
| music/delete-a-song-from-your-device | verified-device | USB Drive wording replaced: the device is an MTP media device. Music's song menu has no delete. | org.webosports.app.settings.location/qml/Connectivity/UsbPage.qml:123; org.webosports.app.settings.location/qml/Connectivity/UsbPage.qml:138 |
| music/delete-songs-from-a-playlist | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/main.qml:1038 |
| music/edit-a-playlist-name | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/main.qml:1084 |
| music/get-music-onto-your-device | verified-device | Streaming not tried: no streaming account on the devices. | org.webosports.app.music/appinfo.json:56; org.webosports.app.music/qml/pages/PreferencesPage.qml:188; org.webosports.app.music/qml/main.qml:100; +1 more |
| music/listen-to-music | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/main.qml:94; org.webosports.app.music/qml/components/CollectionHeader.qml:115; org.webosports.app.music/qml/components/ViewBar.qml:69; +3 more |
| music/remove-a-song-from-playlist-view | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/main.qml:693; org.webosports.app.music/qml/pages/QueuePage.qml:176; org.webosports.app.music/qml/pages/QueuePage.qml:73 |
| music/return-to-album-art-view-for-the-currently-playing-song-from-anywhere- | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/components/MiniPlayer.qml:24; org.webosports.app.music/qml/main.qml:688; org.webosports.app.music/qml/NowPlaying.qml:208 |
| music/search-songs-artists-albums-genres-or-playlists | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/components/MusicHeader.qml:40; org.webosports.app.music/qml/pages/SearchPage.qml:109 |
| music/sort-all-songs-or-a-playlist | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/components/ViewBar.qml:62; org.webosports.app.music/qml/pages/LibraryPage.qml:104; org.webosports.app.music/qml/views/SongsView.qml:55; +1 more |
| music/switch-the-now-playing-display | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/NowPlaying.qml:607; org.webosports.app.music/qml/NowPlaying.qml:560 |
| music/use-music-playback-controls | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.music/qml/NowPlaying.qml:467; org.webosports.app.music/qml/NowPlaying.qml:509; org.webosports.app.music/qml/NowPlaying.qml:519; +3 more |
| pdf/change-the-display-size | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.pdf/qml/components/CommandBar.qml:88; org.webosports.app.pdf/qml/ViewerPage.qml:35 |
| pdf/move-around-in-a-file | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.pdf/qml/components/CommandBar.qml:78; org.webosports.app.pdf/qml/components/CommandBar.qml:69; org.webosports.app.pdf/qml/components/GoToPageDialog.qml:120; +3 more |
| pdf/open-a-file | verified-device | App's label is PDF Viewer. Opening from Files/Email rests on the mime registration and README; other groups own those apps. | org.webosports.app.pdf/qml/LibraryPage.qml:56; org.webosports.app.pdf/qml/LibraryPage.qml:185; org.webosports.app.pdf/qml/LibraryPage.qml:102; +2 more |
| pdf/send-a-file-as-an-attachment-to-an-email-message | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.pdf/qml/ViewerPage.qml:259; org.webosports.app.pdf/qml/LibraryPage.qml:275 |
| pdf/view-bookmarks | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.pdf/qml/components/CommandBar.qml:53; org.webosports.app.pdf/qml/components/ContentsPanel.qml:74 |
| maps/customize-the-map-view | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.maps/build/app.js contains 'Humanitarian'; org.webosports.app.maps/build/app.js contains 'OpenTopoMap'; org.webosports.app.maps/build/app.js contains 'CyclOSM'; +3 more |
| maps/get-directions | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.maps/build/app.js contains 'Starting Location'; org.webosports.app.maps/build/app.js contains 'Ending Location'; org.webosports.app.maps/build/app.js contains 'Start voice guidance'; +3 more |
| maps/move-around-and-zoom-in-out-on-a-map | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.maps/build/app.js contains 'mapZoomIn'; org.webosports.app.maps/source/views/main.js:122 (mapZoomButtons) |
| maps/search-for-a-business | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.maps/build/app.js contains 'Save place'; org.webosports.app.maps/build/app.js contains 'nominatim.openstreetmap.org'; org.webosports.app.maps/source/views/main.js:1082 (markerPopupTap), source/data/Pullout.js:57 (Current) |
| maps/search-for-an-address | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.maps/build/app.js contains 'Save place'; org.webosports.app.maps/build/app.js contains 'Route to here'; org.webosports.app.maps/source/views/main.js:13 (searchLocation) |
| maps/view-your-current-location | verified-device | No Allow Once prompt: Maps asks the location service directly (requiredPermissions location.query). | org.webosports.app.maps/build/app.js contains 'Current location found'; org.webosports.app.maps/build/app.js contains 'Location error: '; org.webosports.app.maps/source/views/main.js:44,595,637 (myLocation button); +1 more |
| maps/work-with-saved-locations | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.maps/build/app.js contains 'Save place'; org.webosports.app.maps/build/app.js contains 'Remove from saved'; org.webosports.app.maps/build/app.js contains 'No saved places yet'; +1 more |
| location-services/manage-location-information-passed-to-applications | verified-device | Auto Locate/Always Ask and Background Data Collection are gone. | org.webosports.app.settings.location/qml/General/LocationPage.qml:293; org.webosports.app.settings.location/qml/General/LocationPage.qml:318; org.webosports.app.settings.location/qml/General/LocationPage.qml:332; +2 more |
| location-services/manage-location-information-passed-to-websites | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.settings.location/qml/General/LocationPage.qml:249; org.webosports.app.settings.location/qml/General/LocationPage.qml:257; org.webosports.app.settings.location/qml/General/LocationPage.qml:276; +1 more |
| location-services/turn-location-service-providers-on-off | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.settings.location/qml/General/LocationPage.qml:400; org.webosports.app.settings.location/qml/General/LocationPage.qml:425; org.webosports.app.settings.location/qml/General/LocationPage.qml:447; +2 more |
| web/add-a-web-page-to-the-launcher | verified-device | Tablet layout only: the phone layout hides the Share button, so nothing reaches Add to Launcher there. | org.webosports.app.atlas/source/ActionBar.js:69; org.webosports.app.atlas/source/BrowserApp.js:821; org.webosports.app.atlas/source/phone/PhoneActionBar.js:53 |
| web/create-a-bookmark | needs-device-test | Phone route inferred from PhoneActionBar edit mode using the same AddressInput; not tried. | org.webosports.app.atlas/source/AddressInput.js:51; org.webosports.app.atlas/source/ActionBar.js:67; org.webosports.app.atlas/source/BookmarkList.js:51 |
| web/customize-web-browser-settings | verified-device | Autoplay media with sound left out: the Chromium engine ignores it. Flash rows do not exist. | org.webosports.app.atlas/source/BrowserApp.js:172; org.webosports.app.atlas/source/Preferences.js:36; org.webosports.app.atlas/source/Preferences.js:40; +4 more |
| web/download-files-from-the-web | needs-device-test | /media/internal/downloads held no files on either device; the flow was not exercised. | org.webosports.app.atlas/source/BrowserContextMenu.js:30; org.webosports.app.atlas/source/DownloadList.js:49; org.webosports.app.atlas/source/BrowserApp.js:719; +2 more |
| web/edit-reorder-or-delete-a-bookmark | needs-device-test | No direct way to the drawer in the phone layout: the Bookmarks button is hidden. Password Manager is the only menu item that opens it. Not tried. | org.webosports.app.atlas/source/BookmarkList.js:45; org.webosports.app.atlas/source/BookmarkList.js:36; org.webosports.app.atlas/source/BrowserApp.js:838; +2 more |
| web/go-to-a-website | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.atlas/source/URLSearch.js:51; org.webosports.app.atlas/source/AddressInput.js:47; adb: com.palm.launcher/app/LaunchItems.js:30 (Go to website); +1 more |
| web/navigate-a-web-page | needs-device-test | Scrolling and pinch come from the Chromium engine; no Atlas code to confirm. Gesture-area swipes removed. | org.webosports.app.atlas/source/phone/PhoneBottomBar.js:33; org.webosports.app.atlas/source/phone/PhoneActionBar.js:36; org.webosports.app.atlas/source/ActionBar.js:57; +3 more |
| web/open-a-bookmarked-page | needs-device-test | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.atlas/source/StartPage.js:37; org.webosports.app.atlas/source/URLSearch.js:48; org.webosports.app.atlas/appinfo.json:67; +1 more |
| web/open-another-browser-window | verified-device | browser_shell gives one window, so cards are in-app tabs. Removed Card view text. | org.webosports.app.atlas/source/phone/PhoneTabSwitcher.js:55; org.webosports.app.atlas/source/phone/PhoneTabSwitcher.js:56; org.webosports.app.atlas/source/ActionBar.js:61; +2 more |
| web/return-to-previously-viewed-web-pages | needs-device-test | Phone drawer route as in web/edit-reorder-or-delete-a-bookmark. Clear History's engine case is a no-op, the db8 side was not traced. | org.webosports.app.atlas/source/BrowserApp.js:114; org.webosports.app.atlas/source/HistoryList.js:35; org.webosports.app.atlas/source/Preferences.js:57; +1 more |
| web/search-for-a-website | verified-device | Rewritten to the installed app: labels, paths and merged phone/tablet text. | org.webosports.app.atlas/source/URLSearch.js:82; org.webosports.app.atlas/source/URLSearch.js:86; adb: luna-send -n 1 luna://com.palm.universalsearch/getAllSearchPreference {} (defaultSearchEngine google) |
| web/use-links-on-a-web-page | verified-device | Option key steps removed. | org.webosports.app.atlas/source/BrowserContextMenu.js:26; org.webosports.app.atlas/source/BrowserContextMenu.js:27; org.webosports.app.atlas/source/BrowserContextMenu.js:28; +3 more |
| web/work-with-images-on-a-web-page | verified-device | saveImageAtPoint has no method or case in ChromiumWebView.js, so it falls to unsupported() and is ignored. | org.webosports.app.atlas/source/BrowserContextMenu.js:36; org.webosports.app.atlas/source/BrowserContextMenu.js:33; org.webosports.app.atlas/source/Browser.js:892; +1 more |

## Deleted articles

| Article | Reason |
| --- | --- |
| photos/add-a-picture-to-a-contact | Photos & Videos has no Assign to contact. Its More menu holds only Add to Album and Set As Wallpaper (PictureView.qml moreButton). |
| photos/delete-a-picture | Merged into photos/delete-pictures-or-videos: phone and tablet use the same app now. |
| photos/delete-an-online-pictures-account | Merged into photos/delete-an-online-pictures-or-videos-account. |
| photos/look-at-photos-in-a-slideshow | Merged into photos/look-at-pictures-in-a-slideshow. |
| photos/organize-your-pictures-into-albums | Merged into photos/organize-your-pictures-and-videos-into-albums. Its USB Drive mode steps no longer apply: the device connects as an MTP media device. |
| photos/set-up-an-online-pictures-account-on-your-device | Merged into photos/set-up-an-online-pictures-or-videos-account-on-your-device. |
| photos/use-photos-and-videos-for-the-first-time | The app has no first-run screen, account prompt or Go button: it opens straight at the library (main.qml Component.onCompleted). |
| videos/edit-videos-you-recorded | Neither Videos nor Photos & Videos can trim, rename or describe a video; no such code in either app. |
| music/install-hp-play | HP Play does not exist on LuneOS. |
| music/manually-sync-music-from-hp-play-to-your-device | HP Play does not exist on LuneOS. |
| music/set-up-hp-play-to-sync-with-your-device | HP Play does not exist on LuneOS. |
| music/use-hp-play-to-sync-music-from-your-computer-to-your-device | HP Play does not exist on LuneOS. |
| music/search-for-related-songs-or-content | Music has no menu entry that searches websites. Go to Album and Go to Artist cover related songs (song menu in main.qml). |
| music/show-hide-the-library-or-playlist-lists | The categories can no longer be collapsed: a fixed rail on a tablet, tabs on a phone (LibraryPage.qml). Described in music/listen-to-music. |
| pdf/change-the-text-display-size | Merged into pdf/change-the-display-size. |
| pdf/edit-or-delete-an-online-account-in-adobe-reader | Adobe Reader does not exist on LuneOS, and PDF Viewer has no online accounts. |
| pdf/set-up-adobe-reader-to-access-files-from-an-online-account | Adobe Reader does not exist on LuneOS, and PDF Viewer has no online accounts. |
| pdf/print-a-pdf-file | PDF Viewer has no Print: no print code in the app, and requiredPermissions has no print.operation. |
| pdf/save-a-file-with-a-new-name | PDF Viewer is read-only: no Save As in the app. |
| pdf/share-a-file | Merged into pdf/send-a-file-as-an-attachment-to-an-email-message. |
| maps/work-with-locations-you-viewed-recently | Maps has no recent locations: the Recent tab is commented out in source/data/Pullout.js:58. |
| web/add-a-web-search-engine | Atlas Web cannot add search engines: no OpenSearch handling or add call in its source. Only clearOptionalSearchList remains. |
| web/edit-or-delete-a-bookmark | Merged into web/edit-reorder-or-delete-a-bookmark. |
| web/print-a-web-page | Printing does not work in Atlas Web on LuneOS. The Print menu item is still there, but ChromiumWebView.js ignores printFrame ('print needs a whole printing stack that neva does not build'). |
| web/use-flash-content | There is no Flash in Atlas Web: Chromium 120 engine, no Flash rows in Preferences. |

## Cross-group links

Targets exist today. If another group deletes one, fix these pages.

- /basics/copy-files-between-your-device-and-your-computer: 5 page(s), e.g. music/delete-a-song-from-your-device
- /basics/open-an-application-in-the-launcher: 38 page(s), e.g. location-services/manage-location-information-passed-to-applications
- /basics/open-the-application-menu: 11 page(s), e.g. music/remove-a-song-from-playlist-view
- /exhibition/view-a-picture-slideshow: 1 page(s), e.g. photos/look-at-pictures-in-a-slideshow
- /print-manager/add-a-printer: 1 page(s), e.g. photos/print-pictures
- /print-manager/cancel-printing: 1 page(s), e.g. photos/print-pictures
- Deleted pages that had incoming links from other groups: none found.
- The accounts topic owns the Add an Account and Remove Account flow; photos pages name those labels.

## Missing articles

- Music: streaming services and the Streaming category; Sleep Timer; lyrics; Favorites and automatic playlists; Up Next (Play Next, Add to Queue); import and export of playlists; Exhibition view; Preferences (volume levelling, crossfade).
- Videos: subtitles and audio tracks in depth; Screen lock; Read Video Lengths; Turn Wide Videos on Tall Screens.
- PDF Viewer: find in document; copy text (hold a word); protected files; Document Info; Night Mode.
- Maps: voice guidance; route stops; choosing the map engine; dropped pins; settings (language, GPS update interval).
- Web: Password Manager and import/export; Autofill; Reading Mode; Translate; private cards; Restart Browser Engine; camera, microphone and notification prompts from sites.
- Camera: front/back and lens switching; Camera Preferences (self-timer, HDR, grid, scene, white balance); QR and barcode reading; Tag photos with location.
- Location: GPS Status panel; Application Access list.
- Other apps nearby with no page in these topics: Documents, Sound Recorder, LuneOS Explorer.

## Needs device test

1. web/create-a-bookmark, phone: open a page, tap the address at the top. Is the star shown, and does it save a bookmark?
2. web/edit-reorder-or-delete-a-bookmark and web/return-to-previously-viewed-web-pages, phone: Menu button > Password Manager. Do the drawer tabs let you reach Bookmarks and History? The Bookmarks button is hidden in this layout, so this is the only route found. Swipe an entry and confirm.
3. web/edit-reorder-or-delete-a-bookmark: drag a start page thumbnail; hold it and tap Remove Bookmark.
4. web/navigate-a-web-page: drag to scroll, pinch to zoom on both devices. Hold an empty part of a page and check Share Link. Hold the back arrow on the tablet.
5. web/open-a-bookmarked-page: type part of a bookmark name in the address bar; in Just Type check Bookmarks & History.
6. web/download-files-from-the-web: tap a file link. Does the Downloads tab open on both layouts, does the file land in /media/internal/downloads, does Open work?
7. web/return-to-previously-viewed-web-pages: Preferences > Clear History, then check the History tab. The engine case is a no-op, the db8 delete was not traced.
8. Web, Print menu item: tap it on a loaded page and confirm that nothing prints (article deleted on source evidence).
9. web/work-with-images-on-a-web-page: hold an image, try Save Image, Set Wallpaper, Share Image, Drag. Source says all four are ignored; if a later Atlas fixes them, update the page.
10. photos/add-a-comment-to-a-picture-or-video-in-an-online-account: with a cloud account whose photos allow comments, check that the Comments button appears, and that Enter posts.
11. photos/upload-a-picture-to-the-web: with a cloud account, More > Add to Album > a cloud album. Check that the picture reaches the account.
12. maps/customize-the-map-view: switch Map engine to Google Maps. Does it load with the built-in key? Do Traffic and public transport appear? The page says they do.
13. Maps on a device with a fix: turn on GPS in Location Services, then tap My Location. Both devices had gps and network off.
14. photos/take-a-picture on a phone with a droid camera: tap to focus and the flash button cycle.

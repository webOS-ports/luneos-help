---
{
 "id": "videos/continue-watching-a-video",
 "title": "Continue watching a video",
 "section": [],
 "order": 100003,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.videoplayer/qml/LibraryPage.qml:354",
  "/usr/palm/applications/org.webosports.app.videoplayer/qml/LibraryPage.qml:350",
  "/usr/palm/applications/org.webosports.app.videoplayer/qml/PlayerView.qml:851",
  "/usr/palm/applications/org.webosports.app.videoplayer/qml/PlayerView.qml:844",
  "org.webosports.app.videoplayer/qml/LibraryPage.qml:144 (only in the list layout, not the wide grid)",
  "org.webosports.app.videoplayer/qml/LibraryPage.qml:163 (the servers' items, merged, last watched first)",
  "org.webosports.app.videoplayer/qml/VideoSources.qml:83 (eight at most)",
  "org.webosports.app.videoplayer/qml/LibraryPage.qml:495 (Show on Its Server)",
  "org.webosports.app.videoplayer/qml/LibraryPage.qml:501 (Remove only for the device's videos)",
  "luneos-synergy-connectors/video/{jellyfin,plex}/provider/index.js features() continueWatching: true (Emby shares Jellyfin's)"
 ],
 "review": []
}
---

Videos you stopped part way are at the top of the list, under **Continue Watching**, the last one you watched first.

1. **[Open](/basics/open-an-application-in-the-launcher) Videos**.
2. Tap a video under **Continue Watching**. It starts where you stopped.

For a few seconds you can tap **Start over** to go back to the beginning.

Tap and hold a video for **Play from the Start** or **Remove from Continue Watching**.

{if:unreleased}**Videos from your media servers**

{if:unreleased}On a newer LuneOS build, **Continue Watching** also lists what you stopped on your Jellyfin, Emby and Plex servers ([learn how](/videos/add-a-media-server-account)), next to your device's videos. It shows eight videos at most.

{if:unreleased}Tap and hold a server's video for **Play**, **Play from the Start** or **Show on Its Server**. You can't remove a server's video from the list in Videos: the server keeps its own list.

{if:unreleased}Continue Watching isn't shown when Videos lists your videos as a grid of pictures, as it does on a wide screen.

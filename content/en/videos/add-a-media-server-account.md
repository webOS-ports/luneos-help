---
{
 "id": "videos/add-a-media-server-account",
 "title": "Add a media server account",
 "section": [],
 "order": 326.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "unreleased",
 "evidence": [
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:38",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:44",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:50",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:56",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:92",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:154",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:337",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:316",
  "luneos-synergy-connectors/video/_core/apps/org.webosports.app.videoauth/source/videoAuth.js:442",
  "luneos-synergy-connectors/video/{jellyfin,emby,plex,peertube,upnp}/account/*/*.json (loc_name, capability Video)",
  "enyo-1.0-ports/framework/lib/accounts/source/add-account.js:71 (no heading for capability Video: OTHER)",
  "adb: ls /usr/palm/public/accounts on the MindPhone (no org.webosports.video.* templates); opkg list-installed (videoplayer 2a00b53e81)"
 ],
 "requires": [],
 "review": []
}
---

Media servers in Videos need a newer LuneOS build than some devices have.

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account**.
2. Tap the kind of server. The video accounts are under **OTHER**, or type the name in **Search accounts**.
3. Do what the server asks for:
   - **Jellyfin, Emby:** Under **SERVER**, enter the address you open the server at, for example 192.168.1.10:8096. Enter your **USER NAME** and **PASSWORD**, then tap **Sign In**.
   - **Plex:** Tap **Get a Code**. On a computer or another phone, go to plex.tv/link, sign in to Plex and enter the code. The screen goes on by itself. If the code runs out, tap **Get a New Code**.
   - **PeerTube:** Tap an instance in the list, or search for one. You can also type an instance's address and tap **Add**.
   - **Media Servers (UPnP/DLNA):** Tap **Add**. There is nothing to sign in to. Videos finds the media servers on your network by itself.
4. **[Open](/basics/open-an-application-in-the-launcher) Videos**. Each server has a tab at the top, beside **This Device**. See [Watch videos from a media server](/videos/watch-videos-from-a-media-server).

**Plex without plex.tv:** For a Plex server that lets your network in without signing in, tap **Enter a server address instead**. Enter its address, and a **TOKEN** only if the server asks for one, then tap **Add**.

A Plex account shows every server it can reach, including servers shared with you. Each one gets its own tab.

If you see **Could not connect. Check the address and the network.**, check the server's address and that your device is on a network that reaches it.

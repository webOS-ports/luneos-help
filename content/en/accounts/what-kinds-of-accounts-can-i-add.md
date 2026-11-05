---
{
 "id": "accounts/what-kinds-of-accounts-can-i-add",
 "title": "What kinds of accounts can I add?",
 "section": [],
 "order": 154.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "evidence": [
  "luneos-synergy-connectors/cloud/{immich,photoprism,smugmug}/account (PHOTO.UPLOAD), cloud/webdav/account/com.palm.webdav.json (DOCUMENTS, PHOTO.UPLOAD), im/signal/account/com.palm.signal",
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates '{}' (both devices, 37 templates, same ids)",
  "productivity-apps/mindphone/accounts-lib/source/add-account.js:71-88 (groups, order)",
  "productivity-apps/mindphone/accounts-lib/source/util.js:25 (hidden and validator-less templates left out)",
  "adb: ls /usr/share/luna-service2/services.d: com.palm.imap, pop and smtp only, no EAS service",
  "/usr/palm/applications/com.palm.app.email/accounts/source/ManualConfig.js:57 (EAS commented out)",
  "/usr/palm/applications/com.palm.app.email/accounts/source/AccountWizard.js:1720 (Gmail in the Email Account table)",
  "luneos-synergy-connectors/music/subsonic/account/org.webosports.app.music.subsonic/org.webosports.app.music.subsonic.json",
  "luneos-synergy-connectors (branch herrie/music-video-sources) music/radio/account/org.webosports.app.music.radio/org.webosports.app.music.radio.json",
  "luneos-synergy-connectors/cloud/pigallery2/account/com.palm.pigallery2/com.palm.pigallery2.json",
  "luneos-synergy-connectors video/*/account/*/*.json (jellyfin, emby, plex, peertube, upnp, m3u on main; archive, mediathek, owncast on herrie/music-video-sources)",
  "enyo-1.0-ports/framework/lib/accounts/source/add-account.js:71 (capability Video has no heading: OTHER)",
  "adb: ls /usr/palm/public/accounts on the MindPhone (none of these templates)"
 ],
 "review": []
}
---

**[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account** lists every kind of account your device can use. The list depends on what's installed on your device.

| Heading | Accounts | What they add |
| --- | --- | --- |
| **EMAIL** | Email Account | Email from IMAP and POP services |
| **CONTACTS & CALENDAR** | C+DAV Connector, Google C+DAV, iCloud C+DAV, Yahoo C+DAV | Contacts and calendars ([**learn how**](/calendar/set-up-a-c-dav-account)) |
| **MESSAGING & CHAT** | Discord, Facebook (E2EE), Google Chat | Messaging and contacts |
| | Signal, Teams, Telegram, WhatsApp | Messaging, contacts, and voice and video calls |
| | Jabber, Matrix | Messaging |
| **CLOUD & PHOTOS** | Box, Dropbox, HiDrive, kDrive, Koofr, MEGA, OneDrive, pCloud, S3 Storage, Yandex Disk | Files and photos |
| | Google Drive | Files |
| | Flickr, Immich, PhotoPrism, SmugMug | Photos |
| | WebDAV / Nextcloud | Files and photos |
| **MUSIC** | Apple Music, Deezer, Internet Archive, Jamendo, Qobuz, SoundCloud, Spotify, Tidal | Music |

**On newer LuneOS builds** you can also add these. Some devices don't have them yet.

- Under **MUSIC**: Subsonic, for your own music server, and Internet Radio ([**learn how**](/music/stream-music)).
- Under **CLOUD & PHOTOS**: PiGallery2, for the photos on your own gallery server ([**learn how**](/photos/look-at-photos-on-a-pigallery2-server)).
- Under **OTHER**: Jellyfin, Emby, Plex, PeerTube, Media Servers (UPnP/DLNA), M3U Playlist, Internet Archive, Mediathek and Owncast, for Videos ([**learn how**](/videos/add-a-media-server-account)).

**Google:** Each Google service is a separate account. Use **Email Account** for Gmail, **Google C+DAV** for contacts and calendars, **Google Drive** for files, and **Google Chat** for messaging.

**Microsoft:** Use **OneDrive** for files and photos, and **Teams** for messaging. There's no Microsoft Exchange or Microsoft 365 account type, so you can't add Exchange email, contacts, calendars, or tasks.

See Also [**Use the Accounts application to set up an online account**](/accounts/use-the-accounts-application-to-set-up-an-online-account)

---
{
 "id": "photos/look-at-photos-on-a-pigallery2-server",
 "title": "Look at photos on a PiGallery2 server",
 "section": [],
 "order": 502.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "unreleased",
 "evidence": [
  "luneos-synergy-connectors/cloud/pigallery2/account/com.palm.pigallery2/com.palm.pigallery2.json (loc_name PiGallery2, PHOTO.UPLOAD only)",
  "luneos-synergy-connectors/cloud/pigallery2/apps/com.palm.app.pigallery2-auth/source/pigallery2Auth.js:22",
  "luneos-synergy-connectors/cloud/pigallery2/apps/com.palm.app.pigallery2-auth/source/pigallery2Auth.js:25",
  "luneos-synergy-connectors/cloud/pigallery2/apps/com.palm.app.pigallery2-auth/source/pigallery2Auth.js:35 (Connect)",
  "luneos-synergy-connectors/cloud/pigallery2/apps/com.palm.app.pigallery2-auth/source/pigallery2Auth.js:71",
  "luneos-synergy-connectors/cloud/pigallery2/README.md (read-only, no videos, HEIC and the like as thumbnails, self-signed certificates refused, sub-albums need a newer photos service)",
  "org.webosports.app.photos origin/master qml/AlbumView.qml:47 (sub-albums)",
  "enyo-1.0-ports/framework/lib/accounts/source/add-account.js:77 (PHOTO.UPLOAD: CLOUD & PHOTOS)",
  "adb: ls /usr/palm/public/accounts on the MindPhone (no com.palm.pigallery2); its Photos app has no sub-albums (no AlbumCell.qml)"
 ],
 "requires": [],
 "review": []
}
---

PiGallery2 needs a newer LuneOS build than some devices have.

PiGallery2 is a photo gallery you run on your own server. Its folders show up in Photos & Videos as albums.

1. **[Open](/basics/open-an-application-in-the-launcher) Accounts** > **Add an Account** > **PiGallery2**, under **CLOUD & PHOTOS**.
2. Enter the server's address, for example gallery.example.org or http://192.168.1.5.
3. Enter your user name and password. For a gallery that needs no sign-in, leave both empty.
4. Tap **Connect**.
5. **[Open](/basics/open-an-application-in-the-launcher) Photos & Videos**. The account is under **LIBRARIES**. To fetch its albums right away, open the **[Menu](/basics/open-the-application-menu)** and tap **Sync Now**.

On newer builds, the folders inside a folder are shown as albums inside that album. Otherwise every folder is an album of its own.

You can only look at the photos. Nothing is uploaded to the server, and the gallery's videos are left out. Pictures in formats such as HEIC or TIFF come over as smaller copies.

If your server uses a certificate it made itself, your device refuses it. Use an address with plain http only on your home network: over the internet, your password would be sent unprotected.

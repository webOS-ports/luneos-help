---
{
 "id": "photos/set-up-an-online-pictures-or-videos-account-on-your-device",
 "title": "Set up an online pictures or videos account on your device",
 "section": [],
 "order": 502,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d500-01/41204",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.photos/qml/main.qml:352",
  "/usr/palm/applications/org.webosports.app.photos/qml/main.qml:347",
  "adb: luna-send -n 1 luna://com.palm.service.accounts/listAccountTemplates {\"capability\":\"PHOTO.UPLOAD\"}",
  "core-apps-ports/com.palm.app.accounts/source/AccountManager.js:65"
 ]
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Photos & Videos** > **[Menu](/basics/open-the-application-menu)** > **Preferences & Accounts**. This opens Accounts.
2. Tap **Add an Account** > tap the type of account.
3. Sign in and follow the instructions on the screen.
4. Go back to Photos & Videos. The account appears under **LIBRARIES**. To fetch its albums right away, open the **[Menu](/basics/open-the-application-menu)** and tap **Sync Now**.

These accounts can hold pictures: Box, Dropbox, Flickr, HiDrive, kDrive, Koofr, MEGA, OneDrive, pCloud, S3 Storage and Yandex Disk.

---
{
 "id": "documents/open-a-document-from-an-online-account",
 "title": "Open a document from an online account",
 "section": [],
 "order": 100005,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.documents/source/views/LibraryView.js:37",
  "/usr/palm/applications/org.webosports.app.documents/source/views/CloudView.js:230",
  "/usr/palm/applications/org.webosports.app.documents/source/views/CloudView.js:271",
  "/usr/palm/applications/org.webosports.app.documents/source/services/CloudService.js:212",
  "adb: luna-send listAccountTemplates {\"capability\":\"DOCUMENTS\"} (Box, Dropbox, Google Drive, HiDrive, Koofr, MEGA, OneDrive, S3 Storage, Yandex Disk, kDrive, pCloud)",
  "TouchPad /media/cryptofs/apps/usr/palm/applications/org.webosports.app.documents/source/views has no CloudView.js (older copy)"
 ],
 "review": []
}
---

This isn't in every copy of Documents. You need an online storage account, such as Dropbox, Google Drive or OneDrive, added in [Accounts](/accounts/use-the-accounts-application-to-set-up-an-online-account).

1. **[Open](/basics/open-an-application-in-the-launcher) Documents** and tap the cloud button in the toolbar.
2. Tap an account, then tap folders until you find the document.
3. Tap the document. Documents downloads it and opens it.

When you use **Save a Copy** on such a document, the copy is also uploaded to the same folder online, as a new file. To go up a folder, use the back gesture.

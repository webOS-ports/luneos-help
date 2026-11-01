---
{
 "id": "web/import-or-export-passwords",
 "title": "Import or export passwords",
 "section": [],
 "order": 100002,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.atlas/source/LoginExporter.js:11",
  "/usr/palm/applications/org.webosports.app.atlas/source/LoginImporter.js:14",
  "/usr/palm/applications/org.webosports.app.atlas/source/LoginImporter.js:3",
  "/usr/palm/applications/org.webosports.app.atlas/source/PasswordList.js:41",
  "/usr/palm/applications/org.webosports.app.atlas/source/PasswordList.js:42",
  "/usr/palm/applications/org.webosports.app.atlas/source/BrowserApp.js:992",
  "/usr/palm/applications/org.webosports.app.atlas/source/BrowserApp.js:1003"
 ],
 "review": []
}
---

Atlas Web reads and writes the CSV file that Chrome and Google Password Manager use. The file is always called atlas-logins.csv, in the top folder of your internal storage.

This file holds your passwords as plain text. Anyone who gets it can read them. Delete it when you are done.

**To import:**

1. Export your passwords from Chrome.
2. Rename the file atlas-logins.csv and copy it to the top folder of your device ([learn how](/basics/copy-files-between-your-device-and-your-computer)).
3. In Atlas Web, open the [Menu](/basics/open-the-application-menu) and tap **Password Manager**.
4. Tap the import button at the bottom of the panel.

Atlas Web tells you how many it imported and how many it skipped as duplicates.

**To export:** Do steps 3 and 4 with the export button beside it. Atlas Web tells you how many it saved. An export overwrites any atlas-logins.csv that is there.

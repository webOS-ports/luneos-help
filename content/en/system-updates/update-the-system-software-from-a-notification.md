---
{
 "id": "system-updates/update-the-system-software-from-a-notification",
 "title": "System update notifications",
 "section": [],
 "order": 444,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/17583",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "/usr/palm/services/org.webosports.service.update/lib/update.js:30 and :263-272 (toast, opens org.webosports.app.settings)",
  "adb: /etc/palm/activities/org.webosports.service.update (24h check)",
  "adb: appinfo.json of org.webosports.app.settings.updates (visible false)",
  "adb: org.webosports.app.settings is not in /usr/palm/applications on either device",
  "org.webosports.app.settings/src/qml/General/UpdatePage.qml:27-32 (placeholder example page)",
  "org.webosports.update/README.md B12"
 ]
}
---

When your device is connected to the Internet, it checks for a new LuneOS version once a day. If there is one, you get a **System update available** notification that shows the new version.

You cannot download or install the update from your device yet: LuneOS has no screen for this. To get the new version, install it from a computer ([learn how](/system-updates/update-luneos-to-a-newer-version)).

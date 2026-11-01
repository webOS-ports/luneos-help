---
{
 "id": "storage/check-how-much-storage-is-in-use",
 "title": "Check how much storage is in use",
 "section": [],
 "order": 100001,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/StoragePage.qml:158 (box per volume), :208-240 (Used, Free, Filesystem, Device), :260 (note), :272 (Encryption)",
  "adb: appinfo.json of org.webosports.app.settings.storage (Storage, visible, both devices)",
  "adb: luna-send com.palm.storage/volumes/getSpaceInfo (both devices)"
 ],
 "review": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Storage**.
2. Each part of your device's storage has its own box, with a bar that shows how full it is. The bar turns amber when space runs low and red when it is nearly full.

For each part you see:

- **Used**: How much is used, out of the total
- **Free**: How much you can still use
- **Filesystem** and **Device**: Technical details

A memory card or USB stick that is connected gets its own box.

To make room, you can remove apps ([learn how](/software-manager/manage-downloaded-applications)) or delete backups ([learn how](/backup/manage-your-backups)).

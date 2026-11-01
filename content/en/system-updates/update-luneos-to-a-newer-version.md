---
{
 "id": "system-updates/update-luneos-to-a-newer-version",
 "title": "Update LuneOS to a newer version",
 "section": [],
 "order": 443.9,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-source",
 "evidence": [
  "~/webos/LuneOS/OTA/NOTES.md (no working updater; status update 2026-10-14: updater stack unchanged, no feeds, no update page)",
  "https://webos-ports.org/ (test images in luneos-testing releases; flashing replaces the operating system)",
  "https://github.com/webOS-ports/luneos-testing/releases (checked 2026-11-01)",
  "adb: appinfo.json of org.webosports.app.settings.updates (visible false)"
 ],
 "review": []
}
---

LuneOS cannot update itself yet. To get a newer version, you install LuneOS again from a computer.

1. Check which version you have ([learn how](/device-info/view-system-information)).
2. Follow the steps in [Reinstall LuneOS](/basics/reinstall-luneos). They start with making a backup, because reinstalling can erase your information.
3. If your information is gone afterwards, [restore your backup](/backup/restore-a-backup).

Apps from Preware 2 are updated separately ([learn how](/software-manager/manually-check-for-application-updates)).

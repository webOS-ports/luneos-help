---
{
 "id": "software-manager/use-luna-manager",
 "title": "Use Luna Manager",
 "section": [],
 "order": 443.4,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/com.palm.app.preware2/build/app.js (Luna Manager, Rescan, Restart Luna, Restart Java)",
  "preware/source/LunaManagerDialog.js:19-45",
  "preware/source/App.js:73",
  "adb: strings /usr/sbin/org.webosports.service.ipkg (systemctl restart surface-manager; killall java)",
  "adb: systemctl show surface-manager (loaded)",
  "adb: which java (none on either device)"
 ],
 "review": []
}
---

Luna Manager helps when a newly installed app does not behave.

1. **[Open](/basics/open-an-application-in-the-launcher) Preware 2**.
2. **[Menu](/basics/open-the-application-menu)** (upper left) > **Luna Manager**.
3. Do one of the following:
   - If a new app is not in the Launcher: Tap **Rescan**.
   - To restart the interface: Tap **Restart Luna**. This closes all your open apps.
4. Tap **Close**.

**Restart Java** does nothing useful on LuneOS, which does not use Java.

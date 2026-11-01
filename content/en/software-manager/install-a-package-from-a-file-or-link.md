---
{
 "id": "software-manager/install-a-package-from-a-file-or-link",
 "title": "Install a package from a file or link",
 "section": [],
 "order": 443.2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/com.palm.app.preware2/build/app.js (Package Location, Browse, Get Info, Install)",
  "preware/source/InstallPackageDialog.js:34-54 (dialog, Note)",
  "preware/source/App.js:71",
  "preware/source/InstallPackageDialog.js:266-272 (Get Info)",
  "~/webos/LuneOS/exhibition/TESTING.md (appinstalld failure on the MindPhone: to be retested)"
 ],
 "review": []
}
---

Use this for an app package (a file ending in .ipk) that is not in a feed. Install packages only from people you trust.

1. **[Open](/basics/open-an-application-in-the-launcher) Preware 2**.
2. **[Menu](/basics/open-the-application-menu)** (upper left) > **Install Package**.
3. Under **Package Location**, do one of the following:
   - Enter the web address of the package.
   - Tap **Browse** and tap the package on your device.
4. To read about the package first, tap **Get Info**.
5. Tap **Install**.
6. Tap **Close**.

If the package needs a restart, Preware 2 does not do it for you here. Use [Luna Manager](/software-manager/use-luna-manager) or restart your device ([learn how](/device-info/restart-your-device)).

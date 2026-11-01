---
{
 "id": "software-manager/find-and-install-apps-with-preware-2",
 "title": "Find and install apps with Preware 2",
 "section": [],
 "order": 441.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/com.palm.app.preware2/build/app.js (strings below confirmed)",
  "preware/source/PackagesMenu.js:44-47 (menu rows)",
  "preware/source/SearchHeader.js:27 (Search)",
  "preware/source/PackageDisplay.js:185-188 (Install, Update, Remove, Launch)",
  "preware/source/model/luneosFeeds.js:23-33 (default feeds, first start)",
  "preware/source/App.js:59 (Restart Required)",
  "adb: md5 of app.js equal on both devices"
 ],
 "review": []
}
---

Preware 2 is where you get apps on LuneOS. It lists packages from community feeds. Most of them were made for older devices, so not all of them work.

The first time you open Preware 2 it sets up its feeds and downloads their lists. This needs an Internet connection and can take a while.

1. **[Open](/basics/open-an-application-in-the-launcher) Preware 2**.
2. Do one of the following:
   - To browse: Tap **Available Packages**, then a type, then a category.
   - To find something by name: Type in the **Search** box.
3. Tap the package.
4. Tap **Install**.

If you see **Restart Required**, choose to restart now or later. The package may not work until you do.

To open the app, tap **Launch**, or find it in the Launcher. To remove it, tap **Remove**.

Other lists on the first screen: **Package Updates** shows what can be updated, **Installed Packages** shows what you have, and **List of Everything** shows all packages.

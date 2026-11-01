---
{
 "id": "software-manager/set-preware-2-preferences",
 "title": "Set Preware 2 preferences",
 "section": [],
 "order": 443.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.preware2/build/app.js (all labels)",
  "preware/source/SettingsDialog.js:67-143,262-290 (settings)",
  "preware/source/App.js:68,180-192",
  "preware/source/model/cookie.js:18-26 (defaults)",
  "preware/source/model/packagesModel.js:221,327,377 (fixUnknown, ignoreDevices)",
  "preware/source/UpdateFeeds.js:119-158",
  "preware/source/AppPanels.js:483 (searchDesc)"
 ],
 "review": []
}
---

1. **[Open](/basics/open-an-application-in-the-launcher) Preware 2**.
2. **[Menu](/basics/open-the-application-menu)** (upper left) > **Preferences**.
3. Change the settings you want > **Close**.

**Startup**

- **Update Feeds**: When Preware 2 gets new lists: **Every Launch**, **Once Daily**, **Manually Only** or **Ask At Launch**. **Last Update** shows when it last did.
- **Scan unknown packages**: Fills in details of installed packages that are in no feed.
- **Check .ipk association**: Checks at startup that Preware 2 opens package files.

**Actions**

- **Ignore device compat.**: Also lists packages that say they are not made for your device. They may not work.
- **Use App Tuckerbox**: Also handles apps installed from an app catalog.

**Package display**

- **Search Descriptions**: Searches the description of each package as well as its name.
- **Default sort**: **Category Default**, **Alphabetically** or **Last Updated**.
- **Installed is available**: Also shows installed packages under **Available Packages**.

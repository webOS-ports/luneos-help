---
{
 "id": "software-manager/manage-downloaded-applications",
 "title": "Manage downloaded applications",
 "section": [],
 "order": 441,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/10003",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/ApplicationsPage.qml:156 (Show System Apps)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/ApplicationsPage.qml:174 (Installed)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/ApplicationsPage.qml:252 (Delete)",
  "/usr/palm/applications/org.webosports.app.settings-common/qml/General/ApplicationsPage.qml:343 (swipe to remove)",
  "adb: appinfo.json of org.webosports.app.settings.applications (Applications, visible)",
  "/usr/palm/applications/com.palm.app.preware2/build/app.js (Installed Packages, Remove, Update Feeds)",
  "adb: listLaunchPoints has no Software Manager on either device"
 ]
}
---

Use the Applications app to see what is installed and to remove apps. Use Preware 2 to find and install more. Preware 2 takes the place of the old app catalog.

**See what is installed**

1. **[Open](/basics/open-an-application-in-the-launcher) Applications**.
2. Tap an app to see its details and what it is allowed to do ([learn more](/security/see-what-an-application-may-use)).

To include the parts of the system, turn on **Show System Apps**. These cannot be removed.

**Remove an app**

1. **[Open](/basics/open-an-application-in-the-launcher) Applications**.
2. Swipe the app sideways > **Delete**.

**Install an app**

1. **[Open](/basics/open-an-application-in-the-launcher) Preware 2** > **Available Packages**.
2. Tap a type and then a category, and tap the package.
3. Tap **Install**.

For more, see [Find and install apps with Preware 2](/software-manager/find-and-install-apps-with-preware-2).

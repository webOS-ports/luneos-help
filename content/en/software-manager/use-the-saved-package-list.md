---
{
 "id": "software-manager/use-the-saved-package-list",
 "title": "Use the Saved Package List",
 "section": [],
 "order": 443.3,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "evidence": [
  "/usr/palm/applications/com.palm.app.preware2/build/app.js (Saved Package List, Remove from Saved or Uninstall?, Saved Only, Uninstall, savedPackagesTaken)",
  "preware/source/App.js:72,244-245",
  "preware/source/model/packagesModel.js:575-598 (snapshot, fixed record)",
  "preware/source/PackageDisplay.js:193-194,214-227,407-408"
 ],
 "review": []
}
---

The first time Preware 2 loads its packages, it writes down what you have installed. That list then stays as it is, as a record of what you had. It does not grow when you install more.

1. **[Open](/basics/open-an-application-in-the-launcher) Preware 2**.
2. **[Menu](/basics/open-the-application-menu)** (upper left) > **Saved Package List**.
3. To put a package back, tap it > **Install**.

To take a package off the list:

1. Tap the package > **Remove**.
2. If the package is installed, choose **Saved Only** to take it off the list and keep it installed, or **Uninstall** to remove it from your device.

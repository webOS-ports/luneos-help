---
{
 "id": "software-manager/manage-software-feeds",
 "title": "Manage software feeds",
 "section": [],
 "order": 443.1,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/com.palm.app.preware2/build/app.js (New Feed, Name, URL, Compressed, Add Feed, Third-party Feed, Delete, Close)",
  "preware/source/ManageFeedsDialog.js:26-27,32-51,56-60,63-64,332,416-433",
  "preware/source/App.js:70",
  "preware/README.md:53-56 (shows only its own feeds)",
  "adb: luna-send org.webosports.service.ipkg/getConfigs (empty on both: Preware 2 not yet started there)"
 ],
 "review": []
}
---

A feed is a list of packages on the Internet. Preware 2 gets its packages from feeds.

1. **[Open](/basics/open-an-application-in-the-launcher) Preware 2**.
2. **[Menu](/basics/open-the-application-menu)** (upper left) > **Manage Feeds**.
3. Do one of the following:
   - To turn a feed on or off: Tap the **On** or **Off** button beside it under **Installed**.
   - To add a feed: Under **New Feed**, enter a **Name** and **URL**. If the feed is compressed, set **Compressed** to **Yes**. Tap **Add Feed**.
   - To delete a feed: Swipe it sideways > **Delete**.
4. Tap **Close**.

Add a feed only if you trust who runs it. Preware 2 warns you about this when you add one (**Third-party Feed**), because what you install from a feed can run on your device.

To get the latest lists afterwards: **[Menu](/basics/open-the-application-menu)** (upper left) > **Update Feeds**.

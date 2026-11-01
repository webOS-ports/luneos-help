---
{
 "id": "launcher/use-the-launcher",
 "title": "Use the Launcher",
 "section": [],
 "order": 148,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/21611",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/LaunchBar/LauncherTabs.js:6-14,60-78",
  "qml/LaunchBar/FullLauncher.qml Keys.onPressed",
  "adb: /etc/palm/default-launcher-page-layout.json downloads holds only Preware 2: which apps land on Downloads is unconfirmed",
  "adb: tweaks.prefs/get on TouchPad showAndroidTab true with no Waydroid: empty tab",
  "qml/LaunchBar/FullLauncher.qml:56,102-105"
 ]
}
---

The Launcher shows all the applications on your device, on tabs.

- **Apps:** Applications.
- **Android:** [Android applications](/android-apps/about-android-applications), on devices that have them. On other devices this tab is empty, and you can [turn it off](/android-apps/turn-the-android-tab-on-or-off).
- **Downloads:** Applications that you installed yourself.
- **Favorites:** Empty until you [drag applications here](/launcher/use-the-favorites-tab).
- **Prefs:** The settings applications.

To open the Launcher, see [Open the Launcher](/basics/open-the-launcher).

Flick up or down to see all the icons on a tab. Swipe left or right to change tabs, or tap a tab's name.

You can move icons and move them between tabs ([learn how](/launcher/reorder-launcher-icons)). The tabs themselves are fixed.

{if:keyboard}You can also pick an icon with the arrow keys, and press **Enter** or **Space** to open it.

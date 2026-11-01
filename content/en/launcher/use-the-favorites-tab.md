---
{
 "id": "launcher/use-the-favorites-tab",
 "title": "Use the Favorites tab",
 "section": [],
 "order": 149.5,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum of the cited QML on both devices matches luna-next-cardshell",
  "adb: md5sum qml/LaunchBar/FullLauncher.qml, LauncherTabs.js match repo on both devices",
  "qml/LaunchBar/LauncherTabs.js:25-29 Favorites always there",
  "adb: /etc/palm/default-launcher-page-layout.json has no favorites entry, so it starts empty",
  "qml/LaunchBar/LauncherTabConfig.qml one placement per app, saved in db8",
  "qml/LaunchBar/TabApplicationModel.qml:80-84 placement wins"
 ]
}
---

The **Favorites** tab starts empty. Keep the applications you use most here.

1. [Open the Launcher](/basics/open-the-launcher).
2. Tap and hold an icon until it glows.
3. Drag the icon over the name **Favorites**, or hold it at the left or right edge of the screen until the tab changes.
4. Lift your finger, and then tap **DONE**.

An icon is on one tab at a time, so the application leaves the tab it was on. To take it out of Favorites, [drag it to another tab](/launcher/reorder-launcher-icons).

The tab has nothing to do with [Quick Launch](/basics/line-up-your-favorite-applications-in-quick-launch), which has its own set of icons.

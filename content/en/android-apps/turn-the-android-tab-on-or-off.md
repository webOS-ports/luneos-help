---
{
 "id": "android-apps/turn-the-android-tab-on-or-off",
 "title": "Turn the Android tab on or off",
 "section": [],
 "order": 100013,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: tweaks.prefs/get on TouchPad: showAndroidTab true, and no Waydroid there",
  "qml/LaunchBar/FullLauncher.qml:56,102-105 tab follows the tweak only",
  "qml/LaunchBar/LauncherTabs.js:tabForApp, TabApplicationModel.qml:85-98 Apps tab when off",
  "adb: org.webosports.app.settings-common qml/General/AppearancePage.qml:336,391 Launcher, Android Tab; repo identical",
  "adb: /usr/palm/services/org.webosports.service.tweaks.prefs/preferences/luna-next-cardshell.json md5 matches files/tweaks/luna-next-cardshell.json on both devices"
 ]
}
---

The **Android** tab is on, even on a device with no Android applications. There it stays empty, so you may want to turn it off.

1. [Open the Launcher](/basics/open-the-launcher), and tap **Prefs**.
2. Tap **Appearance**.
3. Under **Launcher**, turn **Android Tab** on or off.

You can also use **Show Android tab** in [Tweaks](/tweaks/use-tweaks).

When the tab is off, Android applications are on the **Apps** tab.

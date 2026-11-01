---
{
 "id": "android-apps/about-android-applications",
 "title": "About Android applications",
 "section": [],
 "order": 100010,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: MindPhone has /usr/palm/applications/Waydroid (1.6.3) and /usr/bin/waydroid; TouchPad has neither",
  "meta-luneos/recipes-core/packagegroups/packagegroup-luneos-extended.bb:194-199 only some machines",
  "qml/LaunchBar/LauncherTabs.js:isAndroidApp, tabForApp",
  "qml/LaunchBar/LaunchableAppIcon.qml Waydroid badge",
  "adb: listLaunchPoints MindPhone waydroid.* Browser, Calculator, Calendar, Clock, Contacts, Files, Gallery, Music, Photos, Recorder, Settings",
  "adb: /var/lib/waydroid/waydroid.cfg system_ota .../VANILLA.json, no app store package in launch points",
  "adb: /usr/lib/waydroid/tools/services/user_manager.py makeLuneosApp writes an icon for each launchable package"
 ]
}
---

Android applications aren't available on every device. You have them if there's a **Waydroid** icon in the Launcher.

Waydroid runs Android on your device, next to LuneOS. Android applications open as cards, like your other applications.

- Android applications are on the **Android** tab. Their icons have a small Waydroid badge, so you can tell them from LuneOS applications with the same name, like Calculator.
- Waydroid has to download Android before you can use it ([learn how](/android-apps/set-up-android)).
- Android comes with basic applications like Browser, Files and Gallery, but no app store.

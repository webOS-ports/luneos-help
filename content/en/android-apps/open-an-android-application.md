---
{
 "id": "android-apps/open-an-android-application",
 "title": "Open an Android application",
 "section": [],
 "order": 100012,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: MindPhone /usr/libexec/waydroid-luneos-app launch paths, full UI vs package",
  "adb: MindPhone /media/cryptofs/apps/usr/palm/applications/waydroid.*/launch.sh",
  "qml/LaunchBar/LauncherTabs.js:isAndroidApp",
  "launching an Android application was not tried"
 ]
}
---

Android applications aren't available on every device ([see if you have them](/android-apps/about-android-applications)).

1. [Open the Launcher](/basics/open-the-launcher), and tap **Android**.
2. Tap an application.

If Android isn't running yet, the application can take a while to open.

To see all of Android in one card, tap **Waydroid**.

To close an Android application, [throw its card](/basics/close-an-application-or-application-screen) off the top of the screen.

---
{
 "id": "android-apps/set-up-android",
 "title": "Set up Android",
 "section": [],
 "order": 100011,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: MindPhone /usr/libexec/waydroid-luneos-download _wd_ask, _wd_status, waydroid_luneos_first_start: all labels and messages",
  "adb: MindPhone /usr/palm/applications/org.webosports.app.waydroid.download/qml/main.qml notification progress",
  "adb: MindPhone /usr/libexec/waydroid-luneos-app first start, then shows Android",
  "adb: /var/lib/waydroid/images system.img 1.4 GB, downloaded 2026-10-30; the flow itself was not run for this page"
 ]
}
---

Android applications aren't available on every device. You need Waydroid ([see if you have it](/android-apps/about-android-applications)) and an internet connection.

1. [Open the Launcher](/basics/open-the-launcher), and tap **Android**.
2. Tap **Waydroid**.
3. Wait for the message **Download Android?**. It shows how much will be downloaded and how much storage Android needs, and warns you if you're on mobile data.
4. Tap **Download**. Tap **Not now** to do it later.

The download can take a long time. You can see how far it is in your [notifications](/basics/view-and-work-with-notifications), and you can keep using your device. Android starts when it's installed.

To stop the download: Tap the notification or **Waydroid**, and then tap **Stop download**. Tap **Keep going** to let it continue.

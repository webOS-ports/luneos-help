---
{
 "id": "basics/touchscreen-the-launcher",
 "title": "Touchscreen - The Launcher",
 "section": [
  "Get to know your device"
 ],
 "order": 2,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/42826",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "adb: screencaptures/20261031075422.png phone Launcher",
  "qml/StatusBar/StatusBar.qml launcher-visible",
  "qml/LaunchBar/LauncherTabs.js",
  "phone drawing launcher_page1b_mrwr removed: it has no Quick Launch"
 ]
}
---

<!-- ui:phone -->

![image](/legacy/device_drawings/launcher_page1b_mrwr.png)

1. **Status bar:** Says **Launcher** in the upper-left corner.
2. **Tabs:** **Apps**, **Downloads**, **Favorites** and **Prefs**, plus **Android** if your device runs Android applications. Tap a tab, or swipe left or right, to change tabs. An arrow shows that there are more tabs that way.
3. **Icons:** Tap an icon to open the application.
4. **Quick Launch:** The same bar as in Card view.
5. **System icons:** Show the battery, wireless connections and more. Tap them to open the [system menu](/basics/open-the-connection-menu).
6. **Notifications:** Appear at the bottom of the screen, above the gesture area. Tap them to see the details.

<!-- ui:tablet -->

![image](/legacy/device_drawings/launcher_to3g.png)

1. **Status bar:** Says **Launcher** in the upper-left corner.
2. **Tabs:** **Apps**, **Downloads**, **Favorites** and **Prefs**, plus **Android** if your device runs Android applications. Tap a tab, or swipe left or right, to change tabs.
3. **Icons:** Tap an icon to open the application.
4. **Quick Launch:** The same bar as in Card view.
5. **System icons:** Show the battery, wireless connections and more. Tap them to open the [system menu](/basics/open-the-connection-menu).
6. **Notifications:** Appear in the status bar. Tap them to see the details.

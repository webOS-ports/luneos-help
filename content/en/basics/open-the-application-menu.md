---
{
 "id": "basics/open-the-application-menu",
 "title": "Open the application menu",
 "section": [
  "Use the menus"
 ],
 "order": 50,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "palm/d400-01/26893",
 "status": "verified-device",
 "review": [],
 "evidence": [
  "adb: md5sum /usr/lib/qml/WebOSCompositor/qml matches repo on both devices",
  "qml/StatusBar/AppMenu.qml toggleState",
  "qml/StatusBar/StatusBar.qml:611-616 top edge flick",
  "adb: screencaptures show app name with arrow on both devices"
 ]
}
---

1. In an application, do one of the following:
   - Tap the application's name in the upper-left corner of the screen.
   - Flick down from the top edge of the screen, over the application's name.
2. Tap a menu item.

Each application has its own items, and some have no menu at all. If the menu is longer than the screen, scroll it to see more items.

To close the menu, tap outside it.

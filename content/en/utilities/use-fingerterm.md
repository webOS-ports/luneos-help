---
{
 "id": "utilities/use-fingerterm",
 "title": "Use Fingerterm",
 "section": [],
 "order": 100103,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "evidence": [
  "/usr/palm/applications/org.mer.app.fingerterm/Main.qml:261-272 (menu button, upper right)",
  "/usr/palm/applications/org.mer.app.fingerterm/MenuFingerterm.qml:122-288 (menu items)",
  "adb: ls /usr/share/translations (fingerterm_eng_en.qm)",
  "adb: listLaunchPoints (Fingerterm on both)"
 ],
 "review": []
}
---

Fingerterm is a second terminal app, with its own large keyboard on the screen. Like [Terminal](/utilities/use-the-terminal), it is meant for people who know Linux, and a wrong command can damage your system.

1. **[Open](/basics/open-an-application-in-the-launcher) Fingerterm**.
2. Type a command with the keyboard on the screen.
3. To open the menu, tap the button in the upper-right corner. It has **Copy**, **Paste**, **URL grabber**, **Font size**, **UI Orientation** and **Drag mode**.

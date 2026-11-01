---
{
 "id": "tweaks/use-tweaks",
 "title": "Use Tweaks",
 "section": [],
 "order": 100001,
 "devices": [
  "phone",
  "tablet"
 ],
 "origin": "luneos",
 "status": "needs-device-test",
 "review": [],
 "evidence": [
  "adb: /usr/palm/services/org.webosports.service.tweaks.prefs/preferences/luna-next-cardshell.json md5 matches files/tweaks/luna-next-cardshell.json on both devices",
  "adb: tweaks app source/Main.js, Config.js md5 match tweaks/enyo-app/source on MindPhone",
  "adb: listLaunchPoints has Tweaks on both devices; /etc/palm/default-launcher-page-layout.json prefs has it",
  "tweaks/enyo-app/source/Main.js categories, CSS capitalize",
  "tweaks/enyo-app/source/Config.js:65 help toggle, :171 Yes/No, :190 groups",
  "files/tweaks/luna-next-cardshell.json all labels, restart \"none\"",
  "qml/AppTweaks/AppTweaks.qml",
  "adb: org.webosports.app.settings-common qml/General/AppearancePage.qml covers all but Disable animations, Hardware navigation keys, Use New Device Menu",
  "adb: on MindPhone tweaks.prefs/get answers \"More than 1 preferences object found\", see docs/audit/shell-new.md"
 ]
}
---

Tweaks changes how the screens around your applications look and act. The most common options are also in **Appearance**, on the **Prefs** tab of the Launcher.

1. [Open the Launcher](/basics/open-the-launcher), and tap **Prefs**.
2. Tap **Tweaks**.
3. Tap **Luna**.
4. Change the options. They take effect right away.

To see what each option does, tap the help button at the bottom of the screen.

**ui**

- **Visual support for tap ripple:** Shows a ripple where you tap.
- **Show virtual gesture area:** Shows the [gesture area](/basics/front-view).
- **Disable animations:** Turns off animations. They're always off on an E Ink screen.
- **Hardware navigation keys:** See [Turn hardware navigation keys on or off](/tweaks/turn-hardware-navigation-keys-on-or-off).
- **Enable stacked cards:** Lets you [stack cards](/basics/stack-cards).
- **Display date, time or both:** Sets what the status bar shows: **Date Only**, **Time Only** or **Date & Time**.

**launcher**

- **Tab title case:** Sets how tab names are written: **UPPERCASE**, **lowercase** or **Capitalized Case**.
- **Show Android tab:** See [Turn the Android tab on or off](/android-apps/turn-the-android-tab-on-or-off).
- **Tab indicators per page:** Sets how many tab names fit on the screen.

**Status Bar**

- **Show battery icon, percentage or both:** Sets how the battery level is shown.
- **Battery Percentage Color Option:** Shows the percentage in **White** or **Color**.
- **Use New Device Menu:** See [Use the New Device Menu](/tweaks/use-the-new-device-menu).
- **Use Custom Carrier String:** Shows your own text in place of the carrier name.
- **Carrier String:** The text to show.
